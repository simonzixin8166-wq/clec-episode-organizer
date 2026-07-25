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
language: zh-Hant
status: generated-needs-review
source_segments: {len(segments)}
speaker_labels: partially-structured
publish_to_website: false
tags:
  - clec
  - clec/逐字稿
---

# {title}

> [!warning] 閱讀版仍需人工校對
> 本頁以平台 CC 為原始文字層，只加入繁體轉換、段落、標題、匿名學員及有證據的詞彙修正。原始 CC 與繁體原稿另行保留。

> [!info] 講者標示方式
> 原始 CC 沒有逐句講者資料。每個學員區塊包含該學員與 James 老師的完整往返，不強行替每一句猜測講者。

"""
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(frontmatter + "\n\n".join(output) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
