# CLEC Episode Organizer

把 CLEC 節目從多平台來源整理成可查證、可閱讀、可人工審核的繁體中文 Obsidian 知識頁。

這個 skill 以 CLEC 五位數編號作為單集的唯一識別，同一集即使同時出現在 X、pCloud、Google Drive、Bilibili、Odysee 與 Podcast，也只建立一篇節目主頁。

## 它能做什麼

- 盤點使用者指定的日期區間，依五位數編號合併同一集內容。
- 收集並標示 X、pCloud、Google Drive、Bilibili、Odysee、RSS／Podcast 等來源。
- 把已確認、待確認與未找到的來源分開。
- 建立「30 秒內看懂、3–5 分鐘理解主要論證、願意深讀的人」三層內容。
- 優先採用平台人工字幕、自動 CC 或 Podcast transcript。
- CC 不清楚時，只截取同集局部音訊補正；字幕大量缺漏時才重跑全長語音辨識。
- 保留原始字幕／ASR、繁體稿與整理版，不互相覆寫。
- 將學員匿名為「學員 1、學員 2……」。
- 把整理版逐字稿嵌入單集主頁，閱讀時仍在同一頁。
- 預設 `publish_to_website: false`，先保留人工審核。

## 與語音轉文字工具的分工

所有字幕取得、媒體下載與語音辨識統一交給 `media-transcript`。本 skill 專注於 CLEC 的來源判定、繁體轉換、詞彙校對、內容分層、匿名化與 Obsidian 整併，不另建重複的 ASR 流程。

建議順序：

1. 使用 `media-transcript --engine auto` 探測來源。
2. 人工字幕優先，其次是平台 CC 或 Podcast transcript。
3. 少數疑義以同集音訊前後 10～20 秒局部轉錄核對。
4. 只有字幕大量缺漏、時間軸失效或整體不可讀，才重跑全長 ASR。

## 安裝方式

將整個 `clec-episode-organizer` 資料夾放入 Codex skills 目錄：

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
│   └── clec-transcription-lexicon.md
└── scripts/
    ├── build_readable_transcript.mjs
    └── build_readable_transcript.py
```

使用範例：

```text
使用 $clec-episode-organizer 整理 00573，先讀 X 的 CC 字幕，
不清楚的地方才用同集 Podcast 音訊局部核對，最後整併到 Obsidian。
```

也可以指定期間：

```text
使用 $clec-episode-organizer 盤點 2026-07-01 到 2026-07-31 的 CLEC 內容，
依五位數編號合併來源，先回報缺口，不發布網站。
```

## 固定頁面結構

```markdown
> [!abstract] 30 秒內看懂
> **一句話重點：……**

## 3–5 分鐘理解主要論證
### 可以帶走的問題或行動

## 願意深讀的人：證據、限制與延伸資料
### 這集在講什麼，也沒有講什麼
### 名詞說明
### 來源對照
### 證據限制
### 逐字稿
#### 整理版逐字稿
#### 原始繁體稿
### 整理進度
```

內容相關的小標題可以依單集調整，但上述固定章節、標點與層級不變。

## 逐字稿原則

- 原始字幕、原始 ASR 與原始繁體稿不覆寫。
- 整理版只調整段落、主題標題、標點、已確認名詞與明顯相鄰重複。
- 不按固定分鐘數硬切章節。
- 先保留 James 老師主講順序，再整理主持人與學員問答。
- 學員按第一次上台順序匿名編號。
- 主持人姓名必須有來源或經使用者確認。
- 聽不清楚的詞標示 `〔需核對〕`，不自行猜測。

## 發布與資料安全

- 預設 `publish_to_website: false`。
- 找到但無法確認的來源標示為待確認。
- 搜尋不到不等於不存在，不建立猜測性連結。
- 不把投資內容改寫成獲利保證或個人投資建議。
- 不在 skill 中寫死使用者家目錄、密碼、Token 或 API Key。

## 版本

目前版本：`v1.1.0`

版本內容請見 [RELEASE_NOTES.md](RELEASE_NOTES.md)。
