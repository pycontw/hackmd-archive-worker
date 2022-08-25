---
title: 'PyConTW 開發組 Infra (Tooling) 小隊'
tags: 2021-dev-infra, 2021-organize, 
disqus: hackmd
---
🔙 [PyCon TW 2021 Organizing 共筆](/Wb9vQrfJQk-5tPoPR23hwA)
# PyConTW 開發組 Infra (Tooling) 小隊


[TOC]

--- 

## 宗旨

開發組 Infra 小隊成員致力於透過技術能力改善 PyConTW 團隊流程運作：
- 開發工具常為試驗性質，我們需要**重視學習/嘗試錯誤大於最終有沒有成功完成**
- 開發有助於減少組織**重複性高的例行性事務**（如上傳影片、寄信等）的工具
- 不完美主義：交付最小可運行工具，先求有再求好
- 玩得開心最重要（歡迎跨組找各組大大聊聊天）


## 2021 目標
- 優先改善註冊組、開發組、大會文件流程如寄信、歷年網站 archive、文件查找等


## Member Checklist
- [ ] 確認已填寫[通訊錄](https://docs.google.com/spreadsheets/d/19uZnyrcSgW78LB0MnRjZv5ab_0UIzm524cBIN0kjfOU/edit#gid=668333332)
- [ ] 加入 PyConTW Discord
- [ ] 和組員們打聲招呼 ([#team_dev_infra_sustaining](https://discord.com/channels/752904426057892052/752923161149833287)) 
    > 可以稍微介紹一下自己經歷或講講自己來的目的
- [ ] DM 組長 @Josix  討論自己來的目的與希望嘗試的事物
- [ ] 確認已開啟相關權限如 HackMD, Calendar, Trello, Google Mailing List...
- [ ] 訂閱 [PyConTW Calendar](https://calendar.google.com/calendar/embed?src=t9r9qd19ju6760neai5gilt1v8%40group.calendar.google.com&ctz=Asia%2FTaipei) 
- [ ] 閱讀 [PyCon TW 2021 Organizing 共筆](https://hackmd.io/@pycontw/SyG5_GrED/https%3A%2F%2Fhackmd.io%2FocZL4XTsTIi00ucx2wCjdA%3Fview)
## 目前開發項目及人力分配

- PyVideo Configuration Auto-Generation [name=x1~2 (Gary, Josix)]
    - 議程組工具，每年會期結束會上傳影片至 YouTube (現已有[Session Video Publisher](https://github.com/pycontw/session-video-publisher)處理上傳事務) 及 PyVideo，為上傳至 PyVideo 需要生成一個配置檔案如[pycontw-2019 configurations](https://github.com/pyvideo/data/tree/master/pycon-tw-2019) 發送至 [PyVideo Data Repo](https://github.com/pyvideo/data)
        > Note. 新增功能至 Session video publisher 中
- Registration Mail Handler [name=x1~2 (Jacky, Josix, Mozix)]
    - 註冊組工具（但應該有寄信需求就可以用），動態帶入參數至已寫好範本的信件中並寄出，如帶入寄出邀請碼和收件人位址至不同收件人，自動化寄出信件流程。
    - 可參考 [Mail handler tool](https://github.com/pycontw/mail_handler) 多新增註冊相關流程
    - 4/18(進度update) 
        - 與註冊組討論需求
        - 驗證碼可直接在JSON file加變數
        - 要了解tasks file code

- Archive the past websites [name=x1~2 (Gary, Mozix, Ray)]
    - 將歷年網站轉為靜態網頁，減少開發組維運成本
    - 可參考 [pycontw-2012-2013 archive](https://github.com/pycontw/pycontw-2012-2013-archive)
- Discord Text Backup Bot [name=x1~2 (Cloudy)]
    - 大會使用，紀錄各組在 discord 上的討論，方便後續幾年大會籌辦時參考
- HackMD Full Text Search [name=x2~3 (Gary, Josix)]
    - 將同步於 HackMD 的文件串接檢索功能，預期最後提供一個 web 介面讓想要查找文件的志工方便查詢，由於 HackMD 本身的搜索僅限於標題和 tag，另外提供的檢索頁面應該會比較方便新進/舊志工查找資訊和文件傳承
    - Related techique
        - GitHub API Survey
        - Search Engine
- Repo Contributions Statistics  [name=x1 (Josix)]
    - 開發組使用，統計 GitHub Repo 上的 Commits, PRs, Issues, Comments 數量及資訊視覺化，並從中觀察有無什麼 insights
    - 可參考 [github-readme-stats](https://github.com/anuraghazra/github-readme-stats)
    - Related techique
        - GitHub Graph API Survey
        - SVG Server
- Talk Preview Image Auto-Generation [name=x1~2] (Josix)
    - 議程組工具，PyConTW20 有在會期前幾週在粉專發了一些會期的議程 Summary 的圖片，想嘗試看看是否可以拿議程資料及背景圖片自動生成這件事 (或減少製作負擔）

## Portal
### [許願池](/@pycontw/HJQ15L54v)
### [Meetig Minutes](/@pycontw/HyQYHoeBd)
### [Available Time](https://www.when2meet.com/?11509652-QTicS)
## Reference
- [Automate the boring stuff with Python](https://automatetheboringstuff.com/2e/chapter0/)
    - 可能是本讓非工程師的人上手的書，它不會講怎麼寫高深的程式，而是把重點放在如何用最簡單的方法解決眼前的問題
- [Practical Business Python](https://pbpython.com/)
    - 裡面分享了一些使商業流程自動化的 Python 腳本