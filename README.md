# CLEC Episode Organizer

「CLEC投资理财频道」由旅美退休华人 James Chen 老师创办，以非营利方式分享长期投资、资产配置、退休规划与人生经验。

这个 Skill 把 CLEC 相关节目从多平台来源统整成可查证、可阅读、可人工审核的简体中文 Obsidian 知识页。

## 它能做什么

- 盘点用户指定的日期区间，依五位数编号合并同一集内容。
- 收集并标示 X、pCloud、Google Drive、Bilibili、Odysee、RSS／Podcast 等来源。
- 把已确认、待确认与未找到的来源分开。
- 创建「30 秒内看懂、3–5 分钟理解主要论证、愿意深读的人」三层内容。
- 优先采用平台人工字幕、自动 CC 或 Podcast transcript。
- CC 不清楚时，只截取同集局部音频补正；字幕大量缺漏时才重跑全长语音辨识。
- 保留原始字幕／ASR、简体稿与整理版，不互相覆写。
- 依用户确认的 CLEC 词库，批量校对指定文件夹内的多份 Markdown 整理稿。
- 对 `QQ／QQM／OD／ODC` 等短代号使用完整词界，避免改坏其他 ETF 或英文单字。
- 批量修改前后以 SHA-256 验证 TXT、SRT、VTT 等源文件完全没有改动。
- 将学员匿名为「学员 1、学员 2……」。
- 把整理版逐字稿嵌入单集主页，阅读时仍在同一页。
- 缺省 `publish_to_website: false`，先保留人工审核。

## 与语音转文本工具的分工

所有字幕取得、媒体下载与语音辨识统一交给 `media-transcript`。本 skill 专注于 CLEC 的来源判定、简体转换、词汇校对、内容分层、匿名化与 Obsidian 整并，不另建重复的 ASR 流程。

建议顺序：

1. 使用 `media-transcript` 探测来源，缺省由工具自动选择可用方式。
2. 人工字幕优先，其次是平台 CC 或 Podcast transcript。
3. 少数疑义以同集音频前后 10～20 秒局部转录核对。
4. 只有字幕大量缺漏、时间轴失效或整体不可读，才重跑全长 ASR。

比较方法时，以「产出可人工审阅初稿的总时间」为准，不只看取得第一份文本的速度。整理版还必须补自然中文标点与分段，只移除不影响语意的语赘词及机械重复，并检查最后两位学员、节目最后 30 秒、尾端重复及无音频依据的续写。完整规则见 `references/transcript-quality-gates.md`。

## 安装方式

将整个 `clec-episode-organizer` 文件夹放入 Codex skills 目录：

```text
clec-episode-organizer/
├── SKILL.md
├── README.md
├── RELEASE_NOTES.md
├── agents/
├── assets/
│   └── episode-page-template.md
├── references/
│   ├── 00574-transcript-config.json
│   ├── 00574-verified-example.md
│   ├── clec-transcription-lexicon.md
│   └── transcript-quality-gates.md
└── scripts/
    ├── build_readable_transcript.py
    └── build_readable_transcript.mjs（旧设置兼容）
```

使用范例：

```text
使用 $clec-episode-organizer 整理 00573，先读 X 的 CC 字幕，
不清楚的地方才用同集 Podcast 音频局部核对，最后整并到 Obsidian。
```

也可以指定期间：

```text
使用 $clec-episode-organizer 盘点 2026-07-01 到 2026-07-31 的 CLEC 内容，
依五位数编号合并来源，先回报缺口，不发布网站。
```

也可以批量校对既有整理稿：

```text
使用 $clec-episode-organizer，依 CLEC 常用词数据库校对
「30 逐字稿」内所有整理版 Markdown；保留待核对词，
不要修改 TXT、SRT、VTT 或其他原始稿。
```

## 固定页面结构

```markdown
> [!abstract] 30 秒内看懂
> **一句话重点：……**

## 3–5 分钟理解主要论证
### 可以带走的问题或行动

## 愿意深读的人：证据、限制与延伸数据
### 这集在讲什么，也没有讲什么
### 名词说明
### 逐字稿
#### 整理版逐字稿
```

内容相关的小标题可以依单集调整，但上述固定章节、标点与层级不变。

## 逐字稿原则

- 原始字幕、原始 ASR 与原始简体稿不覆写。
- 原始字幕、ASR、模型与处理纪录只留在后端产物，不显示于节目主页。
- 节目主页的逐字稿区只嵌入整理版逐字稿。
- 整理进度、待办与内部审核状态不显示于节目主页正文。
- 来源对照、来源状态与证据限制只留在内部纪录，不显示于节目主页正文。
- 同号不同内容或短篇后缀可能误并时，例外保留「编号重复」警示，说清楚本页实际涵盖范围。
- 整理版只调整段落、主题标题、标点、已确认名词与明显相邻重复。
- 不按固定分钟数硬切章节。
- 先保留 James 老师主讲顺序，再整理主持人与学员问答。
- 学员按第一次上台顺序匿名编号。
- 主持人姓名必须有来源或经用户确认。
- 听不清楚的词标示 `〔需核对〕`，不自行猜测。
- 批量校对只使用 `user-confirmed` 或 `verified` 词形；候选词不自动替换。
- 长词优先、短代号使用完整词界，并检查 UTF-8 乱码。
- 批量前后比对源文件 SHA-256，任何差异都视为验证失败。

## 发布与数据安全

- 缺省 `publish_to_website: false`。
- 找到但无法确认的来源标示为待确认。
- 搜索不到不等于不存在，不创建猜测性链接。
- 不把投资内容改写成获利保证或个人投资建议。
- 不在 skill 中写死用户家目录、密码、Token 或 API Key。

## 版本

目前版本：`v1.3.1`

版本内容请见 [RELEASE_NOTES.md](RELEASE_NOTES.md)。
