---
title: '2021 開發組 Infra Squad Meeting Minutes'
tags: 2021-dev-infra, 2021-organize
disqus: hackmd
---
🔙 [PyCon TW 2021 Organizing 共筆](/Wb9vQrfJQk-5tPoPR23hwA)
🔙 [PyCon TW 2021 dev-infra 主頁](/@pycontw/Bkp2vRQEu)
# 2021 開發組 Infra Squad Meeting Minutes

[TOC]

---
## Bi-Weekly Sprint (09/05/2021)
:::info
- **Location:** Gather Town
- **Link**: https://gather.town/i/WJwUbc5v (password: pycontw2021)
- **Date:** 16:30 - 18:00 Sep 5, 2021 (TST)
- **Agenda:**
    - 說明 sprint 開發項目
    - Coding time
- **Participants:**
- **Online Participants:**
    - Josix
    - Where
:::
### Projects
#### [HackMD Archive](https://github.com/pycontw/hackmd-archive-worker)
- Indexing notes in MeiliSearch - Josix `wip`
- Implement HackMD api client for fetching `{hackmd_host}/exportAllNotes` - Gary
- Implement HackMD notes classsifier for put different teams' notes to different folders. - Where

#### [Session Video Uploder](https://github.com/pycontw/session-video-publisher)
- [add new feature: generate pyvideo data](https://github.com/pycontw/session-video-publisher/pull/7) - Gary `wip`

#### [Mail Handler](https://github.com/pycontw/mail_handler)
- [Feat: Add csv to json conversion module for supporting csv format input in the future](https://github.com/pycontw/mail_handler/pull/29)

#### [PyConTW Past Websites Archive](https://github.com/pycontw/pycon_archive_past_website)
- 需要協助測試目前的靜態網站有無問題
    - 可參考 https://discord.com/channels/752904426057892052/833237663070158858/880698985923350529

#### Other projects
可以參照 Issues 認領
- [宣傳圖自動生成](https://github.com/pycontw/talk-preview-img-builder)

## Bi-Weekly Meeting/Sprint (08/22/2021)
:::info
- **Location:** Gather Town
- **Link**: https://gather.town/i/WJwUbc5v (password: pycontw2021)
- **Date:** 16:30 Aug 22, 2021 (TST)
- **Agenda:**
    - Review action items
    - Sprint time
- **Participants:**
- **Online Participants:**
    - Josix
    - Gary
    - Mozix
:::
### Discussion
#### Previous Action Itmes
- Josix
    -  Talk Preview Image Autogen
        -  Export PPT/Images `done`
        -  Code: https://github.com/pycontw/talk-preview-img-builder
    - HackMD Full Text Search
        - Indexing notes in MeiliSearch `wip`
        - Complete codebase skeleton `done`
        - Code: https://github.com/pycontw/hackmd-archive-worker
- Mozix
    - Archive Past Websites
        - [ ] Scrape background-image and favicon -> Transfer to Josix
        - [x] Fixing 404 issue when switching local
        - [ ] Refactoring code
- Gary
    - Session Video Uploder
        - [x] Fixing PR https://github.com/pycontw/session-video-publisher/pull/7
    - HackMD Full Text Search
        - [ ] Implement HackMD api client for fetching `{hackmd_host}/exportAllNotes`
- Where
    - HackMD Full Text Search
        - [ ] Implement HackMD notes classsifier for put different teams' notes to different folders.
- Jacky
    - [ ] Fixing PR  https://github.com/pycontw/mail_handler/pull/29 -> Transfer to Josix
## Bi-Weekly Meeting/Sprint (07/11/2021)
:::info
- **Location:** Gather Town
- **Link**: https://gather.town/i/WJwUbc5v (password: pycontw2021)
- **Date:** 16:30 July 11, 2021 (TST)
- **Agenda:**
    - 公告待解的任務&認領 (16:30 - 16:45)
    - 一起寫 code 來開發 (16:45 - 18:00)
- **Participants:**
- **Online Participants:**
    - Josix
    - Where
    - Mozix
- **Minutes Taker:**
:::
### Discussion
#### Issues/PRs to be solved
- Mail Handler
    - Jacky
        - [Feat: Add csv to json conversion module for supporting csv format input in the future](https://github.com/pycontw/mail_handler/pull/29)
    - Where
        - [x] [new user guide document](https://github.com/pycontw/mail_handler/pull/30)
- Archive Past Websites
    - Refactoring codes
    - Build CD for deploy different websites on different branch
- PyVideo Configuration File
    - Josix
        - [Build: Adding CI for validating coding style](https://github.com/pycontw/session-video-publisher/issues/8)
    - Gary
        - [add new feature: generate pyvideo data](https://github.com/pycontw/session-video-publisher/pull/7)
- New Project Kick-off
    - HackMD Full Text Search
        - Discussion with HackMD Team (Josix)
        - Build an auto sync scripts to github repo
    - Repo Stats Visualization
        - Make the speed of fetching Github API result faster
        - Resolve access limits of GitHub API 
    - Talk Preview Image Autogen
        - Volunteer wanted
            - Josix
            - Where

## Bi-Weekly Meeting (06/27/2021)
:::info
- **Location:** Gather Town
- **Link**: https://gather.town/i/WJwUbc5v (password: pycontw2021)
- **Date:** 16:30 June 27, 2021 (TST)
- **Agenda:**
    - Commitee Info
    - Task Update
        - Mail Handler
        - Archive Past Websites
        - PyVideo Configuration File
    - New Project Kickoff

- **Participants:**
- **Online Participants:**
    - Josix
    - Mozix
    - tai (臨時有事情晚一點進來)
    - where
    - GaryPai
- **Minutes Taker:**
:::

### Discussion
- Commitiee
    - Josix
        - 大會確定轉為線上會議,不管會不會清零
        - 互動
            - Gather.town
        - 延期到 10/2 ~ 10/3
        - T-shirts https://forms.gle/Xsu8wnwHJcdN86Wq5
- Mail Handler
    - Jacky
        - 有關帶入 CSV 格式的參數 PR 再麻煩 Jacky 開
    - Where
        - 確認使用文件撰寫方式及格式是否可行，沒有問題可以傳到 Repo 上了
- Archive Past Websites
    - Josix
        - 等待開發組部署
        - Refactoring
        - 目前已轉移至 pycontw 下感謝 Mozix 
            - https://github.com/pycontw/Pycon_archive_past_website
- PyVideo Configuration File
    - Josix
        - PR Reviewing completed
    - Gary
        - Solving PyVideo-data CI Failure See https://github.com/pyvideo/data/blob/master/Makefile
- New Project Kick-off
    - HackMD Full Text Search
        - Discussion with HackMD Team (Josix)
        - Build data source
        - Jacky
    - Repo Stats Visualization
        - Volunteer wanted
            - Mozix
            - Gary
    - Talk Preview Image Autogen
        - Volunteer wanted
            - Josix
## Bi-Weekly Meeting (05/29/2021)
:::info
- **Location:** Gather Town
- **Link**: https://gather.town/i/WJwUbc5v (password: pycontw2021)
- **Date:** 16:30 May 30, 2021 (TST)
- **Agenda:**
    - Commitee Info
    - Task Update
        - Mail Handler
        - Archive Past Websites
        - PyVideo Configuration File

- **Participants:**
- **Online Participants:**
    - Josix
    - GaryPai
    - Mozix
    - Where
- **Minutes Taker:**
:::
### Discussion
- Commitiee
    - 官網需要放上大家的大頭照，需要到上傳到 drive https://drive.google.com/drive/u/2/folders/1kSACZT5aeKSzbA4JJdsBwnK9xlWD2bS9 頭貼命名格式如 `infra_<your_name>.png`
    - PSF membership promoting https://discord.com/channels/752904426057892052/847798435843538974/847799672872501249
    - New Life Style Channel Opening: [#netflix](https://discord.com/channels/752904426057892052/845309924376444988), [#switch](https://discord.com/channels/752904426057892052/845313231702720572), #cook, #stock,....
- Mail Handler
    - PR Reviewing: 
    - 新 Issue 需要幫忙: https://github.com/pycontw/mail_handler/issues/26
    - Where 確認使用文件撰寫方式及格式是否可行
        - https://hackmd.io/@pycontw/BJy4WRgqO
- Archive Past Websites
    - Code Reviewing and Testing
    - Repo 需要轉到 PyConTW 下面
- PyVideo Configuration File
    - PR Reviewing
    - 2020 影片 confiugration 可以在 PyVideo-data 開 PR 了
### A.O.B. （臨時動議）

## Bi-Weekly Meeting (05/02/2021)
:::info
- **Location:** [杯盃 PuiBui Cafe](https://g.page/PuiBui-Daan?share)
- **Link**: https://meet.google.com/enp-ufnw-nqh
- **Date:** 16:30 May 02, 2021 (TST)
- **Agenda:**
    - Task Update
        - Mail Handler
            - 行前信相關需求確認
            - 開發 mail_handler 可以吃 csv
            - mail_handler 使用教學
            - 寫 Jinja File formating 的教學文件
            - 需要壓測看有沒有信件會進 Spam 每次寄件數量可能是原因
        - Archive Past Websites
            - 2016 官網封存進度
        - PyVideo Configuration File

- **Participants:**
    - Josix
    - cloudy
    - Leila
    - Anan
- **Online Participants:**
    - Gary
    - Jacky
    - Where
    - Mozix
    - Ray
- **Minutes Taker:**
:::
### Discussion
- Mail Handler
    - 行前信相關需求確認
        - Josix 進行中，等待 Tom 回覆
    - 開發 mail_handler 可以吃 csv
        - Jacky 先撰寫 `csv2json.py`作為使用 可以開PR
    - mail_handler 使用教學
        - where 目前先了解 mail_handler 使用方式、邊紀錄使用方法
    - 寫 Jinja File formating 的教學文件
        - Cloudy 先了解 mail_handler 使用方式，再研究看看 Jinja 如何帶入樣式
    - 需要壓測看有沒有信件會進 Spam 每次寄件數量可能是原因
- Archive Past Websites
    - 2016 官網封存進度
        - Mozix 完成 css, js archive，測試有無問題
- PyVideo Configuration File
    - Gary 已完成功能，準備進入 review 階段
    - 待開 PR
### A.O.B. （臨時動議）



## Bi-Weekly Meeting (04/18/2021)
:::info
- **Location:** [德佈Debut Cafe 台北店](https://goo.gl/maps/4ZHYT5qc85uX2ia89)
- **Link**: https://meet.google.com/enp-ufnw-nqh
- **Date:** 16:30 Apr 18, 2021 (TST)
- **Agenda:**
    - Task Update
        - Mail Handler
        - Archive Past Websites
        - PyVideo Configuration File

- **Participants:**
    - Josix
    - Matt
    - David Jr
    - Jacky
    - Mozix
    - Juihsiang
- **Online Participants:**

- **Minutes Taker:**
:::

### Discussion
- PyVideo 確認目前狀況
    - 約 5/14 前完成
- Mail Handler 確認目前狀況
    - Jacky 了解大致 codebase
    - 發起會議了解各組需求
- Archive Past Websites
    - 先從 2016 開始爬看看
- Project Channel 已經開了要討論的東西可以丟在上面
~~Discord Backup Bot~~


### A.O.B. （臨時動議）



## Bi-Weekly Meeting (03/31/2021)
:::info
- **Location:** Online
- **Link**: https://meet.google.com/kfm-ujpf-pbq
- **Date:** 21:00 Mar 31, 2021 (TST)
- **Agenda:**
    - 21:00 - 21:10
        - 自我介紹（背景、想要獲得什麼、一週貢獻的時間）
    - 21:10 - 21:30
        - 確認基本資訊及權限、介紹 Infra Team 是什麼 & 要進行的工作 (Josix)
    - 21:30 - 21:40
        - 認領工作，討論之後運作模式
- **Participants:** (None)
- **Online Participants:**
    1. Josix
    2. Cloudy
    3. Gary
    4. Jacky
    5. Mozix
- **Minutes Taker:**
:::

### Discussion
- 各項工作認領 https://hackmd.io/jLT9hPryQ6aPcj03iEMU2Q?view#%E7%9B%AE%E5%89%8D%E9%96%8B%E7%99%BC%E9%A0%85%E7%9B%AE%E5%8F%8A%E4%BA%BA%E5%8A%9B%E5%88%86%E9%85%8D
    - Josix (10hrs/week)
        - PyVideo Configuration Auto-Generationm
        - Mail Handler
        - Archive the past websites
    - Cloudy (6hrs/week)
        - Bot
    - Gary (8 hrs/week):
        - PyVideo Configuration Auto-Generation
        - Archive the past websites
        - HackMD Full Text Search
    - Jacky(8 hrs/week)
        - Registration Mail Handler
    - Mozix(8hrs/week)
        - Mail Handler
        - Archive the past websites
    - Ray(8hrs/week)
        - Archive the past websites

- 初心者向讀書會 & Sharing Session
    - Sharing Session
        - Time
            - 開會時間後
    - 讀書會 
        - Time
            - (TBD)
        - Stuff
            - [The Python Tutorial](https://docs.python.org/3/tutorial/) (也許順便翻譯一下 https://github.com/python/python-docs-zh-tw)
            - [精通 Python｜運用簡單的套件進行現代運算](https://www.tenlong.com.tw/products/9789865024864)


- 定期聚會時間
    - 頻率: 兩週一次
    - 實體開發 or 線上：星期日下午

### A.O.B. （臨時動議）
