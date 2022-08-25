---
tags: 2022-organize, dev, 2022-venue
---

# 2022 開發組志工衝刺開發 Development Sprints
* 日期 Date: 2022/01/16 10:00–17:00（臺北標準時間 TST）
* Gather 連結: https://gather.town/app/6NKcuFatDrrfpAgY/PyCon%20TW%20Sprint%20Venue
* Rundown: 

[TOC]

## 如何組織一個衝刺開發 Organizing your Sprints

* 介紹你的專案 Introduce your project

    你可以在 HackMD 中詳述你的專案內容與特色，以及想要參與者協助的地方。你也可以錄製一個小影片給無法參與實體聚會的參與者，讓他們能夠迅速瞭解你的專案內容。例如一個簡短的教學影片，包括專案介紹與操作、如何佈建、測試，觀看 Issue、Pull Request 等等。讓參與者可以很快上手，並瞭解可以從哪開始著手貢獻。
    
    You can detail your project description and features in HackMD, as well as where you need participants to help. You can also provide a pre-recorded video for participants who cannot participate in the physical Sprints meetup so that they can quickly pick up the knowledge of your project. For example, a short tutorial video, including project introduction and functionality, how to deploy, test, view Issue, Pull Request, etc. Make participants get started quickly and understand where to start contributing.

* 與參與者互動 Interact with participants

    專案主持人可以透過實體聚會分享、信件、聊天群組 (Slack, discord) 等等與參與者互動，交流意見，並協助參與者貢獻你的專案。如此一來，貢獻開源便不受限於時間與地點，而是一個長期的社群經營。
    
    The project host can interact with participants, share ideas with each other, and help participants contribute to your project through physical meetup sharing, email, chat groups (slack, discord), etc. In this way, contributing to open source is not limited to time and place, but a long-term community promotion.

* 提供參與者貢獻的方向 Provide direction for participants to contribute

    你可以從專案中現有需要幫忙的 Issue 或是需要幫助的 Pull Request 中提供參與者貢獻的方向，也可以透過與參與者相互討論，尋找可以更好的方向。
    
    You can provide the direction for participants from the existing issues or pull requests that need help in your project, and you can also discuss with participants to find a better direction.



---

## 2022 專案列表 Projects List

### Pycon News Feed

- **專案描述 Project description**:
    **今天的 [Agenda](https://hackmd.io/Aah_fCbgSUqHO11gfV75Ww)**

    來做推薦系統吧！

    PyconTW 提供的有趣服務越來越多了，如 `PySafe`、`PyCast`、`徵才`等廣告，以及我們的本業也就是`演講`。
    所以我們想在 FB Messenger 上提供一個 news feed，用 ML 的方式來推薦用戶適合他的資訊。

    在本場 Sprint 的實作分成三個部分，歡迎大家加入！
    1. BE-side：Flask + FB API
    2. Recommendation-side：algorithm to design
    3. ELT-side（負責整理用戶的 feature、event，並蒐集文章來推薦）：Airflow + Crawler

- **專案連結 Project link**:
    - GitHub: https://github.com/pycontw/pycon-fb-chatbot
    - [推薦系統](https://heliotrope-podium-fc5.notion.site/Sprint-0e46144427484a78ac86ebada23cdd5c)
- **專案聯絡人 Project Contact**: @davidtnfsh 
- **先需知識**: 推薦系統、Git、Backend、ML、想學的心（擇二）

* 專案房間: Room 1 

---

### [pycontw-website-archive](https://github.com/pycontw/pycon_archive_past_website)

- **專案描述 Project description**: 

    從 2012 年起，PyConTW 已經舉辦多年並且為每年架設專屬的網站頁面，然而隨著舉辦次數越多及向下相容的需求，網站組對於資料庫所可以進行的調整逐漸受到限制，因此為了有效保存過去 PyCon TW 的籌辦經驗，及增加資料庫的調整彈性，此專案專注於爬取並封存歷年的官方網站，將靜態網站頁面架設於 GitHub Page 服務上，以供網站組更方便進行開發。
    此專案從 2021 年已爬取了 2016-2020 年的頁面並且轉移完成，此次衝刺開發將繼續進行 2012 至 2014 年的官方網站，歡迎初學者加入！

- **專案連結 Project link**: [PyCon TW Archived Websites](https://github.com/pycontw/pycon_archive_past_website)
- **專案聯絡人 Project Contact**: @Josix 
- **先需知識**: 簡單的 HTML, CSS, JS, 和爬蟲概念

* 專案房間: Room 2


---
### PyCon TW Web 權限、身分驗證機制

- **專案描述 Project description**: 
    PyCon TW 網站從 2021 年開始走向前後端分離，從前後端合併走到前後端分離，除了重新刻頁面之外的另一大難題就是權限及身分驗證的問題了！
    在 PyCon TW 的網站中，除了單純的顯示大會資訊之外，另外一個很重要的功能就是投稿系統，這次 dev sprint 會從 survey 各種前後端分離常見的身分驗證機制開始，最後到將 PyCon TW Web 的身分驗證機制實作完畢！
    
- **專案連結 Project link**: [PyCon TW FE](https://github.com/pycontw/pycontw-frontend)、[PyCon TW BE](https://github.com/pycontw/pycon.tw)
- **專案聯絡人 Project Contact**: @setmao
- **先需知識**: Python、基礎 web、一點點的 Django

* 專案房間: Room 3 

