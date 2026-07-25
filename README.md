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
- 依使用者確認的 CLEC 詞庫，批次校對指定資料夾內的多份 Markdown 整理稿。
- 對 `QQ／QQM／OD／ODC` 等短代號使用完整詞界，避免改壞其他 ETF 或英文單字。
- 批次修改前後以 SHA-256 驗證 TXT、SRT、VTT 等原始檔完全沒有改動。
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

比較方法時，以「產出可人工審閱初稿的總時間」為準，不只看取得第一份文字的速度。整理版還必須補自然中文標點與分段，只移除不影響語意的語贅詞及機械重複，並檢查最後兩位學員、節目最後 30 秒、尾端重複及無音訊依據的續寫。完整規則見 `references/transcript-quality-gates.md`。

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
│   ├── clec-transcription-lexicon.md
│   └── transcript-quality-gates.md
└── scripts/
    ├── build_readable_transcript.py
    └── build_readable_transcript.mjs（舊設定相容）
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

也可以批次校對既有整理稿：

```text
使用 $clec-episode-organizer，依 CLEC 常用詞資料庫校對
「30 逐字稿」內所有整理版 Markdown；保留待核對詞，
不要修改 TXT、SRT、VTT 或其他原始稿。
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
### 逐字稿
#### 整理版逐字稿
```

內容相關的小標題可以依單集調整，但上述固定章節、標點與層級不變。

## 逐字稿原則

- 原始字幕、原始 ASR 與原始繁體稿不覆寫。
- 原始字幕、ASR、模型與處理紀錄只留在後端產物，不顯示於節目主頁。
- 節目主頁的逐字稿區只嵌入整理版逐字稿。
- 整理進度、待辦與內部審核狀態不顯示於節目主頁正文。
- 來源對照、來源狀態與證據限制只留在內部紀錄，不顯示於節目主頁正文。
- 同號不同內容或短篇後綴可能誤併時，例外保留「編號重複」警示，說清楚本頁實際涵蓋範圍。
- 整理版只調整段落、主題標題、標點、已確認名詞與明顯相鄰重複。
- 不按固定分鐘數硬切章節。
- 先保留 James 老師主講順序，再整理主持人與學員問答。
- 學員按第一次上台順序匿名編號。
- 主持人姓名必須有來源或經使用者確認。
- 聽不清楚的詞標示 `〔需核對〕`，不自行猜測。
- 批次校對只使用 `user-confirmed` 或 `verified` 詞形；候選詞不自動替換。
- 長詞優先、短代號使用完整詞界，並檢查 UTF-8 亂碼。
- 批次前後比對原始檔 SHA-256，任何差異都視為驗證失敗。

## 發布與資料安全

- 預設 `publish_to_website: false`。
- 找到但無法確認的來源標示為待確認。
- 搜尋不到不等於不存在，不建立猜測性連結。
- 不把投資內容改寫成獲利保證或個人投資建議。
- 不在 skill 中寫死使用者家目錄、密碼、Token 或 API Key。

## 版本

目前版本：`v1.2.0`

版本內容請見 [RELEASE_NOTES.md](RELEASE_NOTES.md)。
