---
name: clec-episode-organizer
description: Organize one numbered CLEC episode into a traceable Traditional Chinese Obsidian knowledge page, combining verified X, pCloud, Google Drive, Bilibili, Odysee, and RSS/Podcast sources with layered summaries and preserved transcripts. Use when the user asks to整理、合併、補來源、建立逐字稿閱讀版、匿名學員問答，或更新 CLEC 單集知識頁。
---

# CLEC Episode Organizer

把一個 CLEC 編號當成單一內容主體。平台只是來源、附件或備份，不要各自建立重複文章。

## 必守原則

1. 一次只處理使用者指定的單集；不要掃描整個專案。
2. 以 `canonical_id: clec-<五位編號>` 合併資料，不能只憑發布日期或內容相似度判斷。
3. 找到但無法證明屬於該集的資料，標示「尚未確認」並詢問使用者，不要硬合併。
4. 保留原始來源、原始轉錄、繁體轉錄、整理版、摘要與人工修訂的分層。
5. 預設 `publish_to_website: false`。除非使用者明確要求，不同步網站、CMS 或 Supabase。
6. 寫入使用者實際使用的 Obsidian Vault。若路徑不明，先從目前工作區或使用者提供的資料確認，不要假設固定的家目錄。
7. 使用繁體中文與台灣用語。語氣自然、清楚，不寫成嚴肅報告。

## 工作流程

### 1. 盤點必要檔案

只讀以下必要資料：

- 該集現有草稿與 metadata。
- 該集 raw／zh-Hant JSON、TXT、SRT 或 VTT。
- 使用者提供的來源連結。
- 與該編號直接相關的本機目錄或清單。

先檢查目標檔是否已存在及是否有未預期修改。不得覆寫原始逐字稿。

### 2. 建立來源清單

為每個來源記錄：

- `platform`：X、pCloud、Google Drive、Bilibili、Odysee、RSS／Podcast 等。
- `relationship`：`original-post`、`slides`、`video-archive`、`video-backup`、`audio-edition`、`transcript`、`related-post` 或 `unknown`。
- `verification`：`verified`、`user-confirmed`、`needs-review` 或 `not-found`。
- URL 與簡短說明。

同一頁展示所有已確認來源。搜尋不到不等於不存在；只能寫「目前尚未確認」。平台搜尋結果若只是學員整理頁，放入延伸資料，不能冒充原始來源。

### 3. 建立單集主頁

使用 `assets/episode-page-template.md`。頁面固定採三層閱讀：

1. **30 秒看懂**：一句話重點、3～5 個重點、觀看與閱讀入口。
2. **3～5 分鐘理解**：依內容寫背景、主要論證、策略或可思考的問題，不硬套格式。
3. **深入閱讀**：術語解釋、來源狀態、完整整理版逐字稿、原始稿、證據限制與審核進度。

標題與摘要以國中閱讀程度撰寫。一般正文可使用高中程度概念，但要用日常中文。深度內容可以更進階，所有術語第一次出現時都要解釋。

「一句話重點」使用 Obsidian callout：

```markdown
> [!summary] 一句話重點
> 一至兩句直接說清楚本集主旨。
```

摘要先交代這集在回答什麼問題，再依內容選用段落或列點。避免抽象句、罐頭結論與過度免責語氣；不能替 James 老師發明立場或故事。

### 4. 整理逐字稿

永遠保留原始繁體逐字稿不動，另建 `<編號>｜整理版逐字稿.md`。

先從逐字稿找實際結構，不按固定分鐘數硬切。常見順序是：

1. 課前補充（有則保留）。
2. James 老師依講義主講。
3. 主講結束的明確語句，例如「我今天的分享就先到這裡」。
4. 主持人接手。
5. 學員分享與問答。

不要自動加入 `00:05`、`00:10` 之類的時間章節。只有經人工核對且使用者需要時才加入時間碼。

整理版只做：

- 加入段落與主題標題。
- 統一繁體中文和全形標點。
- 移除沒有承接作用的單獨語氣詞與完全相鄰重複。
- 修正使用者已確認的專有名詞。
- 保持原意、內容順序與口語節奏。

不確定的辨識詞保留並標示 `〔需核對〕`，不要猜。

### 5. 匿名學員

依第一次上台順序標為「學員 1、學員 2……」。同一輪追問沿用相同編號。

- 刪除或替換學員帳號、暱稱與非必要姓名。
- James 老師保留姓名。
- 主持人只在來源或使用者確認後保留姓名；不要沿用上一集主持人。
- 沒有 diarization 時，以「一位學員一個對話區塊」呈現，並註明區塊包含該學員與 James 老師的往返；不要硬猜每一句講者。

需要批次產生閱讀版時，先人工建立該集的分段與替換設定，再執行 `scripts/build_readable_transcript.mjs`。腳本不得自行判斷學員身分。

### 6. 嵌入同一頁

主頁預設嵌入整理版：

```markdown
![[00574｜整理版逐字稿]]
```

並保留原始繁體稿連結：

```markdown
[[00574｜繁體中文逐字稿.txt]]
```

逐字稿可以拆成實體檔以便維護，但 Obsidian 閱讀頁必須透過 embed 呈現在同一頁。

### 7. 驗證與交付

至少檢查：

- canonical ID、標題、日期、語言及 `publish_to_website`。
- 每個已確認來源的 URL 與角色。
- 原始繁體逐字稿未被修改。
- 整理版有課前補充／主講／問答的正確分界。
- 學員編號連續，已知帳號未殘留。
- 使用者確認過的名詞已修正；未知名詞仍有提醒。
- 主頁可連到並嵌入整理版，也能回到原始稿。
- 不把投資觀點寫成獲利保證或個人建議。

完成後只回報實際建立或更新的檔案、已確認來源、待確認來源與發布狀態。

## 參考資料

- 處理 00574 或需要具體範例時，讀取 `references/00574-verified-example.md`。
- 建立主頁時使用 `assets/episode-page-template.md`。
- 從 Whisper JSON 產生段落化閱讀版時，讀取並使用 `scripts/build_readable_transcript.mjs`；00574 可直接參考 `references/00574-transcript-config.json`。
