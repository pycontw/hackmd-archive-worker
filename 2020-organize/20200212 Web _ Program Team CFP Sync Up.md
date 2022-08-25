---
tags: 2020-organize, program
---

🔙 Back to [PyCon TW 2020 Organizing 共筆](/5u84SOprTUeQYBR57TH49w)


# 20200212 Web / Program Team CFP Sync Up

## Participants
Tom, Wei, Pochun, Peihusan, Winnie


## Discussions
* [PR 630](https://github.com/pycontw/pycon.tw/pull/630)
    * tutorial 不轉 community track 
    * CoC 新增欄位要求講者勾選
    * 同意的部分記載年份，今年同意不代表明年同意
        * 可能格式： varchar: 2019,2020
        * TP: 我做的話會把同意這塊單獨做成一個 table，foreign key 到 user
* Run Through [網站上稿](https://docs.google.com/document/d/1C74rBemwp-S1ceAbuAUCZA2ihfM0fHITgW-NCOTOo9s/edit)
    * 確認網站組、議程組各自需要改動的地方
        * 先弄 event & speaking（先）
        * 預計2月底完成
* CFP Detail Related
    * 時區使用 [Anywhere on Earth](https://www.timeanddate.com/time/zones/aoe) 
    * CFP 宣傳? 3/1
    * 預計到4/19
    * 宣傳請各個 meetup organizer 協助announce,公關組網路宣傳
* 網站設定相關
    * 演講長度 (2019 是 沒有偏好/30/45)，上次開會好像只剩下 30 這一個選項
        * 2020: 15 & 30 & 沒有偏好
    * 分類
        * 2019 年分類如下：
            * Best Practices & Patterns
            * Community
            * Databases
            * Data Analysis
            * Education
            * Embedded Systems
            * FinTech
            * Gaming
            * Graphics
            * Other
            * Python Core (language, stdlib, etc.)
            * Python Internals
            * Internet Of Things
            * Python Libraries
            * Science
            * Security
            * Systems Administration
            * Testing
            * Web Frameworks
* 新欄位：
    * _若最後並未錄取 PyCon，可選擇是否願意到在地社群進行分享，PyCon 將提供部分交通補助_
        * 這是一個 Boolean，跟著 TalkProposal 的 /Tutorial的不要 \
    * CoC 要存到 DB
        * 在 New TalkProposal/Tutorial 的時候 check 有沒有同意過 2020CoC，沒有的話他要先打勾同意下一步才能繼續。
        * 2020CoC 的記錄跟著 User Model，額外資訊看前面 PR630 下面
* 過去的文件 (內容有要改嗎?)
    * [https://github.com/pycontw/pycon.tw/tree/master/src/reviews](https://github.com/pycontw/pycon.tw/tree/master/src/reviews)
    * [Introduction · GitBook](https://pycontw.github.io/reviewer-guidebook/) 
        * [https://github.com/pycontw/reviewer-guidebook](https://github.com/pycontw/reviewer-guidebook)

## Action Items
* 網站組: [Feature] 自動 close CfP (4/19 AoE) 
* 網站組: [Test] CfP 上之前測試一下
* 網站組: [選項調整] Topic / Length
* 網站組: [Feature] 欄位新增 - CoC & 社群分享
* 網站組: 截圖 Talk / Tutorial 的所有要填的格子欄位
* 議程組: speaking pages before 2/20
    * [更新 Call For Proposal 內文](https://trello.com/c/hqZh0Sr6/16-%E6%9B%B4%E6%96%B0-call-for-proposal-%E5%85%A7%E6%96%87)
* PoChun: Topic diff
    * 檢查過後2020僅新增 IoT 與 HW 子項目於 CFP 中，但這兩項已經在網頁列表中，不需更動。
* 議程組: check 過去的文件
    * [Run through review documents](https://trello.com/c/bYTjVlFm/43-run-through-review-documents)
* 2/23 大測試 😱 taipei.py sprint


## Reference:


### 2019 Talk Submission Form

#### Part 1

題目 [Text]

分類 [Dropdown]

* Best Practices & Patterns
* Community
* Databases
* Data Analysis
* Education
* Embedded Systems
* FinTech
* Gaming
* Graphics
* Other
* Python Core (language, stdlib, etc.)
* Python Internals
* Internet Of Things
* Python Libraries
* Science
* Security
* Systems Administration
* Testing
* Web Frameworks

時間長度 [Dropdown]

* 無偏好
* 偏好30分鐘
* 偏好45分鐘

語言 [Dropdown]

* 英文演講
* 中文演講/英文投影片
* 中文演講/中文投影片
* 台灣閩南語

Python 難易度

* 入門
* 中階
* 進階

議程錄影

* 是
* 否


#### Part 2

題目* [Text]

分類* [Dropdown]

時間長度* [Dropdown]

語言* [Dropdown]

摘要* [Textarea]

Python 難易度* [Dropdown]

演講目標* [Textarea]

詳細說明 [Textarea]

大綱 [Textarea]

補充資訊 [Textarea]

議程錄影 [Dropdown]

投影片連結 [Text]


### 2019 Tutorial Submission Form

#### Part 1

題目 [Text]

分類 [Dropdown]

時間長度 [Dropdown]

* 半天
* 全天

語言 [Dropdown]

Python 難易度

議程錄影


#### Part 2

題目* [Text]

分類* [Dropdown]

時間長度* [Dropdown]

語言* [Dropdown]

摘要* [Textarea]

Python 難易度* [Dropdown]

演講目標* [Textarea]

詳細說明 [Textarea]

大綱 [Textarea]

補充資訊 [Textarea]

議程錄影 [Dropdown]

投影片連結 [Text]


### Screenshot (這樣比較好喚起記憶)


![](https://i.imgur.com/MAoisZc.png)
