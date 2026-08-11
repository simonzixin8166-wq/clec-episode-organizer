---
name: clec-episode-organizer
description: Organize user-scoped CLEC episodes into traceable Traditional Chinese Obsidian pages. Use when Codex must group X, pCloud, Google Drive, Bilibili, Odysee, and RSS or Podcast sources by five-digit episode number; obtain and review transcripts through media-transcript; clean readable transcripts with the confirmed CLEC lexicon; anonymize students; or build the standard three-layer episode page.
---

# CLEC Episode Organizer

把一个 CLEC 五位数编号视为一集。平台只是来源、附件或备份；同一编号只创建一篇节目主页。

## 内核规则

1. 只处理用户指定的集数或日期范围，不扩大扫描其他项目或 Vault。
2. 以 `canonical_id: clec-<五位编号>` 合并来源；日期相近或内容相似都不足以证明是同一集。
3. 无法确认归属、标题或角色时，标示「尚未确认」或 `〔需核对〕`，不要猜。
4. 分层保存原始来源、原始字幕／ASR、简体原稿、整理版与人工修订，不互相覆写。
5. 缺省 `status: pending-editorial-review`、`publish_to_website: false`；未经用户明确要求，不发布网站或外部数据库。
6. 使用简体中文、台湾用语与日常中文。一般正文使用「台湾、平台、台币」；正式名称例外。
7. 先使用目标 Vault 的 `CLEC｜常用词与逐字稿校对数据库.md`；没有时才读 `references/clec-transcription-lexicon.md`。词库只能协助查证，不能代替音频。

## 运行顺序

### 1. 确认范围与现况

- 确认集数、日期范围、目标 Vault 与交付内容。
- 只读该集现有主页、metadata、来源纪录及逐字稿文件。
- 修改前确认文件是否已存在及是否有其他未预期变更。

若用户指定日期范围，先列出期间内可见项目，再依五位数编号分组。没有编号、编号冲突或短篇后缀无法判定者，放入「尚未确认」，先回报后再逐集整理。

### 2. 创建来源清单

每个来源至少记录：

- `platform`：X、pCloud、Google Drive、Bilibili、Odysee、RSS／Podcast 等。
- `relationship`：`original-post`、`slides`、`video-archive`、`video-backup`、`audio-edition`、`transcript`、`related-post` 或 `unknown`。
- `verification`：`verified`、`user-confirmed`、`needs-review` 或 `not-found`。
- URL 与简短说明。

同一集的已确认来源合并展示。搜索不到只能写「目前尚未确认」；学员整理页只能列为延伸数据。

### 3. 取得并判断逐字稿

字幕取得、媒体处理与语音辨识交给 `media-transcript`：

1. 人工字幕优先，其次是平台自动 CC 或 Podcast transcript。
2. 来源字幕只有少数不清楚处时，保留字幕并用同集局部音频核对。
3. 主讲与问答多个区段都不可读、时间轴失效或大量缺漏时，保留原字幕作证据，再用完整音档 ASR 重建。
4. 原始字幕／ASR、简体转换与整理版分开保存。

选择与验收细节必须读 `references/transcript-quality-gates.md`。至少抽查开场、主讲中段、主持人转场、两段问答、最后两位学员、节目收尾与最后 30 秒。

### 4. 创建单集主页

使用 `assets/episode-page-template.md`，固定三层阅读：

1. `30 秒内看懂`：一句话重点、3～5 个重点、本集数据。
2. `3–5 分钟理解主要论证`：背景、主要论证、策略或行动。
3. `愿意深读的人：证据、限制与延伸数据`：范围、名词与整理版逐字稿。

标题与摘要以国中阅读程度撰写；一般正文使用高中程度概念与日常中文；深度内容可以更高端，但术语第一次出现时要解释。

主页只嵌入整理版逐字稿，不显示原始稿、模型、segment 数量、转录指令、内部待办或技术验证。若同一编号可能对应不同内容，保留简洁的「编号重复」警示。

### 5. 统一标题与文件名

以用户确认的 00574 格式为准：

`00574｜消费才是经济之母，有钱人消费是道德.md`

- 主页固定为 `<五位编号>｜<标题>.md`。
- 使用全角 `｜`，前后不加空格。
- YAML `title`、H1 与文件名去除 `.md` 后必须完全一致。
- 索引与相关页使用完整 Wiki link。
- 标题以用户确认版本优先；来源互相冲突时先询问，不自行缩写。
- 附属档使用相同分隔方式，例如 `<编号>｜整理版逐字稿.md`。

### 6. 制作整理版逐字稿

保留原始简体稿不动，另建 `<编号>｜整理版逐字稿.md`。

依实际内容辨认课前补充、James 主讲、主持人接手、学员分享与问答；不按固定分钟数硬切，也不自动加入 `00:05`、`00:10` 等时间章节。

整理版只做：

- 补自然标点、分段与主题标题。
- 统一简体中文与全角标点。
- 移除不影响语意的独立语赘词与可确认的相邻机械重复。
- 修正用户或可靠来源已确认的专有名词。
- 保持原意、论证顺序、数字、标的与口语节奏。

无法确认的词保留原辨识并标 `〔需核对〕`。

H1 后固定依序放三个备注：

1. `> [!warning] 阅读版仍需人工校对`
2. `> [!info] 讲者标示方式`
3. `> [!note] 专有名词校正`

三个标题与顺序固定；底本、主持人、学员数与证据说明依该集事实填写。专有名词备注连到 `[[CLEC｜常用词与逐字稿校对数据库]]`。

### 7. 讲者与匿名化

- James 老师保留姓名。
- 学员依第一次上台顺序标为「学员 1、学员 2……」，同一轮追问沿用编号。
- 主持人姓名只能依自我介绍、James 称呼、节目说明或用户确认。
- 超过三小时的长片可把 James 视为主讲人候选、Kate 或 Dona 视为主持人候选，但候选不能当成单集证据。
- 没有逐句讲者分离数据时，以一位学员一个对话区块呈现，不硬猜每一句讲者。
- 匿名化只替换已确认的完整身分字符串；不使用宽松姓名规则扫描全文。

### 8. 批量校对

只有用户明确指定文件夹时才批量处理：

1. 分开整理版 Markdown 与 raw、JSON、TXT、SRT、VTT。
2. 修改前后对所有非 Markdown 源文件计算并比对 SHA-256。
3. 只修改整理版／阅读版 Markdown，只套用 `user-confirmed` 或 `verified` 词形。
4. 长词优先；`QQ`、`QQM`、`OD`、`ODC` 等短词使用完整词界。
5. 依上下文才能判断的词不可机械取代。
6. 出现 UTF-8 乱码立即停止并修复。
7. 完成后扫描误辨词、乱码与短代号残留，并抽查每个有修改的文件。

需要从时间段 JSON 产生阅读版时，使用 `scripts/build_readable_transcript.py`。设置必须由人工提供分段、来源说明、匿名对照及替换规则；脚本不得自行判断学员身分。`scripts/build_readable_transcript.mjs` 仅保留旧设置兼容性。

### 9. 验证与交付

交付前确认：

- canonical ID、日期、语言、状态与来源角色正确。
- 主页文件名、YAML `title`、H1 与 Wiki link 一致。
- 原始稿及原始媒体衍生档未被覆写。
- 主讲、主持人与问答分界合理，学员编号连续且身分字符串未残留。
- 已确认名词已修正；未知词仍标 `〔需核对〕`。
- 最后两位学员、节目最后一句、实际音频结尾及最后 30 秒已抽查。
- 疑似重复幻觉或收尾后无音频依据的文本不进入衍生稿。
- 主页只显示整理版逐字稿。
- 不把投资观点写成获利保证或个人建议。

只回报实际更新的文件、已确认来源、待确认来源、仍需人工审阅项目与发布状态。

## 按需读取

- 需要完整主页骨架：`assets/episode-page-template.md`
- 判断 CC、局部 ASR、完整 ASR 或验收逐字稿：`references/transcript-quality-gates.md`
- 校对专有名词：优先读 Vault 词库，否则读 `references/clec-transcription-lexicon.md`
- 需要已确认案例：`references/00574-verified-example.md`
- 从时间段 JSON 产生阅读版：`scripts/build_readable_transcript.py`
