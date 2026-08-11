#!/usr/bin/env python3
"""Build a conservative CLEC readable transcript from timestamped JSON segments."""

import argparse
import json
import re
from pathlib import Path


def normalize(text, replacements, filler_only):
    text = str(text or "").strip()
    if not text or text in filler_only:
        return ""
    text = re.sub(r"\s*,\s*", "，", text)
    text = re.sub(r"\s*\?\s*", "？", text)
    text = re.sub(r"\s*!\s*", "！", text)
    text = re.sub(r"\s+", " ", text).strip()
    for item in replacements:
        text = re.sub(
            item["pattern"],
            item.get("replacement", ""),
            text,
            flags=re.IGNORECASE if "i" in item.get("flags", "") else 0,
        )
    return text.strip()


def close_paragraph(parts, output):
    if not parts:
        return
    paragraph = "，".join(parts)
    paragraph = re.sub(r"，([。！？])", r"\1", paragraph)
    paragraph = re.sub(r"，{2,}", "，", paragraph)
    paragraph = paragraph.strip("，。！？ ")
    if paragraph and paragraph[-1] not in "。！？":
        paragraph += "。"
    if paragraph:
        output.append(paragraph)
    parts.clear()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--config", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    source = json.loads(args.input.read_text(encoding="utf-8"))
    config = json.loads(args.config.read_text(encoding="utf-8"))
    segments = source.get("segments")
    if not isinstance(segments, list):
        raise ValueError("Input JSON must contain a segments array")

    headings = {int(item["segment_id"]): item["markdown"] for item in config["headings"]}
    overrides = {int(key): value for key, value in config.get("segment_overrides", {}).items()}
    replacements = config.get("replacements", [])
    filler_only = set(config.get("filler_only", ["嗯", "呃", "啊", "哦"]))
    size = int(config.get("segments_per_paragraph", 8))

    output = []
    paragraph = []
    previous = ""
    for segment in segments:
        if int(segment["id"]) in headings:
            close_paragraph(paragraph, output)
            output.append(headings[int(segment["id"])])
        source_text = overrides.get(int(segment["id"]), segment.get("text"))
        text = normalize(source_text, replacements, filler_only)
        if not text or text == previous:
            continue
        previous = text
        paragraph.append(text)
        if len(paragraph) >= size or text.endswith(("。", "！", "？")):
            close_paragraph(paragraph, output)
    close_paragraph(paragraph, output)

    episode = config["episode"]
    title = config.get("title", f"{episode}｜整理版逐字稿")
    frontmatter = f"""---
title: "{title}"
type: clec-transcript-readable
canonical_id: clec-{episode}
episode: "{episode}"
language: zh-Hans
status: generated-needs-review
source_segments: {len(segments)}
speaker_labels: partially-structured
publish_to_website: false
tags:
  - clec
  - clec/逐字稿
---

# {title}

> [!warning] 阅读版仍需人工校对
> 本页以平台 CC 为原始文本层，只加入简体转换、段落、标题、匿名学员及有证据的词汇修正。原始 CC 与简体原稿另行保留。

> [!info] 讲者标示方式
> 原始 CC 没有逐句讲者数据。每个学员区块包含该学员与 James 老师的完整往返，不强行替每一句猜测讲者。

"""
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(frontmatter + "\n\n".join(output) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
