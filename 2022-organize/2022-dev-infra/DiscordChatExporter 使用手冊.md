---
tags: 2022-organize, organize, 2022-dev-infra
---

🔙 Back to [歷年 PyCon TW Organizing 共筆](/ryPr7SFyP/%2FHM5mHCFKQCu7-W5ea8ITcw%3Fview)
🔙 Back to [PyCon TW 2022 Organizing 共筆](/rkk3KQ_VY)


# DiscordChatExporter 使用手冊

## 目的
這份教學手冊將帶您瞭解如何使用 DiscordChatExporter
提供匯出 Discord 伺服器所有頻道對話紀錄的教學

## 使用時機
每屆大會結束後，原則上一年一次

## 步驟
### 在 Discord Developer Portal 中進行設定
1. 進入 [Developer Portal連結](https://discord.com/developers/applications)，並點選右上角「New Application」。輸入名稱按下確認後來新增一個 Application。
![](https://i.imgur.com/1D1DtRu.png)

2. 點擊左邊「OAuth2」並點選「URL Generator」。並在右方選取「bot」的選項
![](https://i.imgur.com/qVWNLQn.png)

3. 拉到此頁下方，為這個 bot 選取必要的權限（可以如圖所示選取）。並按下「Copy」按鈕來複製這個 URL。
![](https://i.imgur.com/CeNgUN9.png)

4. 將這個 URL 貼到網址列並前往，選取你要把 bot 加入的伺服器。並按下「Continue」來加入 bot 身分組到伺服器中。
![](https://i.imgur.com/hrVyvFy.png)

5. 回到 Developer Portal，在左方點到「Bot」，並在右方按下「Add Bot」來新增一個 Bot。
![](https://i.imgur.com/kNxvOuO.png)

6. 成功新增後，按下「Copy」按鈕來將 bot token 複製起來，等一下會需要使用到。
![](https://i.imgur.com/BbRT6xM.png)


### 設置並使用 DiscordChatExporter (GUI)
1. 到 [Github repo](https://github.com/Tyrrrz/DiscordChatExporter) 下載並按照指示安裝 DiscordChatExporter。
2. 打開 DiscordChatExporter，確認頁面已經切換到要輸入 bot token 的地方（輸入的地方的左側是一個機器人的圖樣）。並在此輸入您在[上一節](https://hackmd.io/bx3dgM1NQOmeO0ByaRW06w#%E5%9C%A8-Discord-Developer-Portal-%E4%B8%AD%E9%80%B2%E8%A1%8C%E8%A8%AD%E5%AE%9A)第6步驟中所複製的 bot token。最後按下 Enter 以繼續。
![](https://i.imgur.com/jybY1ov.png)
3. 進入後您應該可以看到在[上一節](https://hackmd.io/bx3dgM1NQOmeO0ByaRW06w#%E5%9C%A8-Discord-Developer-Portal-%E4%B8%AD%E9%80%B2%E8%A1%8C%E8%A8%AD%E5%AE%9A)第4步驟中所選定的伺服器，並看到其中的所有頻道。按下 Ctrl + A 可以一次選取所有頻道，按住 shift 可以選取多個頻道。選取完後按下右下方的下載圖樣來進行下載前參數設定。
![](https://i.imgur.com/zm9u8zp.png)
4. 在設定中可以選取想要匯出的格式：json, html...等，以及其他的設定。
（2022年初的匯出的設定為：JSON、Before 2021/12/31、Download media）
接著按下「EXPORT」並選取目標資料夾，就會開始進行下載。
![](https://i.imgur.com/yynNciI.png)


### 備份完成後
[Optional]
由於一年僅需使用一次，因此有長時間我們不會使用到這個 App。因此備份完成後，我們可以到 Discord 的伺服器設定中，左方選取「Integrations」並在右方選擇你的 Bot 並按下「Manage」。
![](https://i.imgur.com/KkxgHg3.png)

接著拉到最下面可以看到「Remove Integration」，點選後即可刪除 Integrations 以及 Bot 在伺服器中的身分組。
![](https://i.imgur.com/1MvqgCh.png)
