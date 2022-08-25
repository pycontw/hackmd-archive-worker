---
title: '2022 開發組 Infra Squad Meeting Minutes'
tags: 2022-dev-infra, 2022-organize
disqus: hackmd
---

🔙 Back to [歷年 PyCon TW Organizing 共筆](/ryPr7SFyP/%2FHM5mHCFKQCu7-W5ea8ITcw%3Fview)
🔙 Back to [PyCon TW 2022 Organizing 共筆](/F4qRbwIsQXWH5B6cZ6Pzyw)
🔙 Back to [PyCon TW 2021 Organizing 共筆](/Wb9vQrfJQk-5tPoPR23hwA)

# 2022 開發組 Infra Squad Meeting Minutes

[TOC]

---
## Internal Development Sprint #5 (08/21/2022)
:::info
- **Location:** In-place Happ. 小樹屋 - 馬告 604， 地址：羅斯福路二段70號6樓之1-604
- **Link**:
- **Date:** 14:00 - 18:00 Jun 12, 2022 (TST)
- **Agenda:**
    - Check Progress
        - Official Website Archive
        - Session Video Uploader
        - Talk Preview Image Builder
    - Development Time
- **Online Participants:**
    - Josix
    - Li-Ying
    - Sean
:::

### Current Project Status
#### Official Website Archive
- Tech: **#Nuxt, #VueJS**
- Repo: https://github.com/pycontw/pycon_archive_past_website
- Tasks:
    - Update to use SSG method to build 2021 website
        - [Reference](https://github.com/pycontw/pycontw-frontend/pull/315) `WIP` @Sean

#### Talk Preview Image Builder
- Repo: https://github.com/pycontw/talk-preview-img-builder
- Tasks
    - [Fix issues according the review comments](https://github.com/pycontw/talk-preview-img-builder/pull/5) `DONE` @LY

#### Session Video Publisher
- Tech: **#google-auth-oauthlib #requests**
- Repo: https://github.com/pycontw/session-video-publisher
- Tasks
    - Create an API endpoint for listing all the infomation of talks
        - Solution1 (use original endpoint) `DONE`  @Sean
            - Fix 500 error from https://pycon.tw/prs/ccip 
        
    - 確認 video 腳本上架的 visibility issue https://discord.com/channels/752904426057892052/752923161149833287/776366271829639169


## Internal Development Sprint #4 (07/23/2022)
:::info
- **Location:** In-place Happ. 小樹屋 - 馬告 604， 地址：羅斯福路二段70號6樓之1-604，門鎖密碼：5620 ＊（活動前五分鐘生效）
- **Link**:
- **Date:** 18:30 - 21:30 Jun 12, 2022 (TST)
- **Agenda:**
    - Check Progress
        - Official Website Archive
        - Session Video Uploader
        - Talk Preview Image Builder
    - Development Time
- **Online Participants:**
    - Josix
    - Luke
    - Li-Ying
    - Sean
:::

### Current Project Status
#### Official Website Archive
- Tech: **#WebCrawler, #requests #beautifulsoup4**
- Repo: https://github.com/pycontw/pycon_archive_past_website
- Tasks:
    - 研究如何使用 nuxt 來產生靜態頁面取代 crawler 失效 `WIP`
        - survey `nuxt generate`/`nuxt build` to generate static site
            - References 
                - https://nuxtjs.org/docs/get-started/commands#list-of-commands
                - https://nuxtjs.org/docs/features/deployment-targets/
                - https://nuxtjs.org/docs/concepts/static-site-generation

#### Talk Preview Image Builder
- Repo: https://github.com/pycontw/talk-preview-img-builder
- Tasks
    - [Hints when missing export folder](https://github.com/pycontw/talk-preview-img-builder/issues/3) `DONE`
    - Build slides/iamges for talks of this year `DONE`
        - Materials
            - [Talk Info](https://discord.com/channels/752904426057892052/874539284810575912)
            - Background Image (@anan)

#### Session Video Publisher
- Tech: **#google-auth-oauthlib #requests**
- Repo: https://github.com/pycontw/session-video-publisher
- Tasks
    - Create an API endpoint for listing all the infomation of talks
        - Solution1 (use original endpoint) `WIP`
            - Fix 500 error from https://pycon.tw/prs/ccip
        - ~~Solution2 (use another one endpoint)~~
            - ~~Check if /api/speeches is enough for use.~~
            - ~~If not -> 需要重建一隻 talks list API 在現在的 API server~~
                - ~~2020 年的 api view https://github.com/pycontw/pycon.tw/blob/pycontw-2020/src/ccip/views.py#L201~~
    - 確認 video 腳本上架的 visibility issue https://discord.com/channels/752904426057892052/752923161149833287/776366271829639169


## Internal Development Sprint #3 (06/12/2022)
:::info
- **Location:** Online @ Gather Town
- **Link**: https://app.gather.town/invite?token=b7UHAi8otVI-hSpZ01WwM-d9rwKzkk8s
- **Date:** 19:30 - 21:30 Jun 12, 2022 (TST)
- **Agenda:**
    - Check Progress
        - Official Website Archive
        - Session Video Uploader
        - Talk Preview Image Builder
    - Development Time
- **Online Participants:**
    - Josix
    - Luke
:::

### Current Project Status
#### Official Website Archive
- Tech: **#WebCrawler, #requests #beautifulsoup4**
- Repo: https://github.com/pycontw/pycon_archive_past_website
- Tasks:
    - Crawling Talk detail page
    - Certain images resources are not found
- Next actions: 
    - 研究如何使用 nuxt 來 
        - survey `nuxt generate`/`nuxt build` to generate static site
            - References 
                - https://nuxtjs.org/docs/get-started/commands#list-of-commands
                - https://nuxtjs.org/docs/features/deployment-targets/
                - https://nuxtjs.org/docs/concepts/static-site-generation

#### Talk Preview Image Builder
- Repo: https://github.com/pycontw/talk-preview-img-builder
- Tasks
    - [Hints when missing export folder](https://github.com/pycontw/talk-preview-img-builder/issues/3)
    - Nice to have
        - Responsive styling to fit-in title and talke description

#### Session Video Publisher
- Tech: **#google-auth-oauthlib #requests**
- Repo: https://github.com/pycontw/session-video-publisher
- Tasks
    - 由於 2021 年 web team 後端改寫，需要重建一隻 talks list API 在現在的 API server 
        - 2020 年的 api view https://github.com/pycontw/pycon.tw/blob/pycontw-2020/src/ccip/views.py#L201
    - 確認 video 腳本上架的 visibility issue https://discord.com/channels/752904426057892052/752923161149833287/776366271829639169


## Internal Development Sprint #2 (05/15/2022)
:::info
- **Location:** Online @ Gather Town
- **Link**: https://app.gather.town/invite?token=b7UHAi8otVI-hSpZ01WwM-d9rwKzkk8s
- **Date:** 19:30 - 21:30 May 15, 2022 (TST)
- **Agenda:**
    - Self Introduction
    - Project Introduction
        - HackMD Archive
        - Official Website Archive
        - Session Video Uploader
        - Talk Preview Image Builder
- **Online Participants:**
    - Josix
    - Sean
    - Luke
    - LiYing
:::
### Project Introduction 
#### Official Website Archive
- Tech: **#WebCrawler, #requests #beautifulsoup4**
- Repo: https://github.com/pycontw/pycon_archive_past_website
- Help Wanted
    - [Archive PyCon APAC 2014 Website](https://github.com/pycontw/pycon_archive_past_website/issues/32) [name=Jay]
        - 目前已經有一個存儲所有 PyCon APAC 2014 HTML, CSS, JS 的 Repo。可以先檢查存 repo 中的是否正常運作。再將其將內容搬到 gh-pages 上。
   - [Archive PyConTW 2021 Website](https://github.com/pycontw/pycon_archive_past_website/issues/37) [name=Luke]
       - 基於 2020 crawler class 修改，因為蠻多URL 是 /2021 開頭，因此在前面都加上 https://tw.pycon.org
       - 2020 年的 /events/warmup-session/ Not Found, 只留 sponsor/prospectus/
       - URL 中路徑少一個 "/", 所以會出現 ...about/historyindex.html. 在DFS中在 URL 尾端補上 '/', 前端也補上 https://tw.pycon.org
       - 修改爬取 script 的 re: 改為只抓.js
       - 好像沒抓到 css, image 目前還有 error

#### Hackmd Archive Worker
- Tech: **#requests #SearchEngine**
- Repo: https://github.com/pycontw/hackmd-archive-worker
- Help Wanted
    - Automatically extract tags from md files
    - Deploy meilisearch by docker-compose
    - ~~- Automatically download all notes from HackMD by using HackMD API~~
        ~~- [Create Token](https://hackmd.io/@docs/HackMD_API_Book/https%3A%2F%2Fhackmd.io%2F%40hackmd-api%2Fdeveloper-portal)~~
        ~~- Export All Notes API (`GET team/pycontw/exportAllNotes`)~~

#### Talk Preview Image Builder
- Tech: **#pillow #python-pptx**
- Repo: https://github.com/pycontw/talk-preview-img-builder
- Help Wanted
    - [Hints when missing export folder](https://github.com/pycontw/talk-preview-img-builder/issues/3)
    - Nice to have
        - Responsive styling to fit-in title and talke description

#### Session Video Publisher
- Tech: **#google-auth-oauthlib #requests**
- Repo: https://github.com/pycontw/session-video-publisher
- Help Wanted:
    - 由於 2021 年 web team 後端改寫，需要重建一隻 talks list API 在現在的 API server 
        - 2020 年的 api view https://github.com/pycontw/pycon.tw/blob/pycontw-2020/src/ccip/views.py#L201
    - 確認 video 腳本上架的 visibility issue https://discord.com/channels/752904426057892052/752923161149833287/776366271829639169

## Internal Development Sprint #1 (03/13/2022)
:::info
- **Location:** [小樹屋 馬告 604 (羅斯福路二段70號6樓之1-604)](https://www.google.com.tw/maps/place/%E7%BE%85%E6%96%AF%E7%A6%8F%E8%B7%AF%E4%BA%8C%E6%AE%B570%E8%99%9F6%E6%A8%93%E4%B9%8B1-604) (password: 1320)
- **Link**:  https://meet.google.com/pvw-bqmn-kgy
- **Date:** 19:00 - 21:00 Mar 13, 2022 (TST)
- **Agenda:**
    - 叫晚餐 
    - Self Introduction
    - Project Introduction 
        - Official Website Archive
        - Hackmd Archive
    - Coding time
- **Participants:**
    - Josix
    - Luke
    - Jordan
    - Jay
    - David Jr.
- **Online Participants:**
:::
### Project Introduction 
#### Official Website Archive
- Tech: **#WebCrawler, #requests #beautifulsoup4**
- Repo: https://github.com/pycontw/pycon_archive_past_website
- Help Wanted
    - [Archive PyCon APAC 2014 Website](https://github.com/pycontw/pycon_archive_past_website/issues/32)
        - 目前已經有一個存儲所有 PyCon APAC 2014 HTML, CSS, JS 的 Repo。可以先檢查存 repo 中的是否正常運作。再將其將內容搬到 gh-pages 上。
   - [Archive PyConTW 2021 Website](https://github.com/pycontw/pycon_archive_past_website/issues/37)
       - 現在 PyConTW 2021 年的網站有點問題，可以先熟悉 codebase，嘗試爬取看看 (Luke)

#### Hackmd Archive Worker
- Tech: **#requests #SearchEngine**
- Repo: https://github.com/pycontw/hackmd-archive-worker
- Help Wanted
    - Automatically extract tags from md files
    - Automatically download all notes from HackMD by using HackMD API
        - [Create Token](https://hackmd.io/@docs/HackMD_API_Book/https%3A%2F%2Fhackmd.io%2F%40hackmd-api%2Fdeveloper-portal)
        - Export All Notes API (`GET team/pycontw/exportAllNotes`)