#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";

function usage() {
  console.error("Usage: node build_readable_transcript.mjs --input transcript.json --config config.json --output readable.md");
  process.exit(2);
}

const args = process.argv.slice(2);
const value = (flag) => {
  const index = args.indexOf(flag);
  return index >= 0 ? args[index + 1] : undefined;
};

const inputPath = value("--input");
const configPath = value("--config");
const outputPath = value("--output");
if (!inputPath || !configPath || !outputPath) usage();

const input = JSON.parse(fs.readFileSync(inputPath, "utf8"));
const config = JSON.parse(fs.readFileSync(configPath, "utf8"));
if (!Array.isArray(input.segments)) throw new Error("Input JSON must contain a segments array");
if (!config.episode || !Array.isArray(config.headings)) throw new Error("Config requires episode and headings");

const headings = new Map(config.headings.map((entry) => [Number(entry.segment_id), String(entry.markdown)]));
const replacements = (config.replacements || []).map((entry) => [new RegExp(entry.pattern, entry.flags || "g"), entry.replacement]);
const fillerOnly = new Set(config.filler_only || ["嗯", "呃", "啊", "哦"]);

function normalizeText(inputText) {
  let text = String(inputText || "").trim();
  if (!text || fillerOnly.has(text)) return "";
  text = text
    .replace(/\s*,\s*/g, "，")
    .replace(/\s*\?\s*/g, "？")
    .replace(/\s*!\s*/g, "！")
    .replace(/，{2,}/g, "，")
    .replace(/\s+/g, " ")
    .trim();
  for (const [pattern, replacement] of replacements) text = text.replace(pattern, replacement);
  return text;
}

function closeParagraph(parts, output) {
  if (!parts.length) return;
  let paragraph = parts.join("，")
    .replace(/，([。！？])/g, "$1")
    .replace(/，{2,}/g, "，")
    .replace(/^[，。！？\s]+|[，\s]+$/g, "");
  if (paragraph && !/[。！？]$/.test(paragraph)) paragraph += "。";
  if (paragraph) output.push(paragraph);
  parts.length = 0;
}

const output = [];
const paragraph = [];
let previous = "";
for (const segment of input.segments) {
  if (headings.has(segment.id)) {
    closeParagraph(paragraph, output);
    output.push(headings.get(segment.id));
  }
  const text = normalizeText(segment.text);
  if (!text || text === previous) continue;
  previous = text;
  paragraph.push(text);
  if (paragraph.length >= (config.segments_per_paragraph || 8) || /[。！？]$/.test(text)) closeParagraph(paragraph, output);
}
closeParagraph(paragraph, output);

const title = config.title || `${config.episode}｜整理版逐字稿`;
const frontmatter = `---
title: ${title}
type: clec-transcript-readable
canonical_id: clec-${config.episode}
episode: "${config.episode}"
language: zh-Hans
status: generated-needs-review
source_segments: ${input.segments.length}
speaker_labels: partially-structured
publish_to_website: false
tags:
  - clec
  - clec/逐字稿
---

# ${title}

> [!warning] 阅读版仍需人工校对
> 本页根据完整 AI 逐字稿整理。原始逐字稿另行保留；本页仅加入段落、标题、学员编号及已确认的文本修正。

> [!info] 讲者标示方式
> 若原始辨识没有逐句讲者数据，每个学员区块包含该学员与 James 老师的完整往返，不强行替每一句猜测讲者。

`;

fs.mkdirSync(path.dirname(outputPath), { recursive: true });
fs.writeFileSync(outputPath, frontmatter + output.join("\n\n") + "\n", "utf8");
