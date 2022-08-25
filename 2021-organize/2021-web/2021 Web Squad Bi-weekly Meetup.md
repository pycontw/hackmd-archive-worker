---
tags: 2021-organize, 2021-web, dev team
---

🔙 [PyCon TW 2021 Organizing 共筆](/Wb9vQrfJQk-5tPoPR23hwA)

# 2021 Web Squad Bi-weekly Meetup

[TOC]

- retro, plan, & develop
- reimbursement budget: 150NTD per person (統編：38552170)
- links:
  - [trello](https://trello.com/b/JCt5GqHH/web-squa)
  - [Google Meet](https://meet.google.com/asu-tvnw-nbz)
  - [Gather](https://gather.town/i/WJwUbc5v)
  - [Figma](https://www.figma.com/file/1za4uYNpSonvgxdcLoHAzs/)
      {%figma https://www.figma.com/file/1za4uYNpSonvgxdcLoHAzs/ %}
  - [hackmd](https://hackmd.io/@pycontw/SyG5_GrED/%2F%40pycontw%2Fr1ZFvJWiw)
  - main repos
    - [frontend repo](https://github.com/pycontw/pycontw-2021)
    - [backend repo](https://github.com/pycontw/pycon.tw)

<details>
    <summary>Member Overview</summary>
    

| Name   | Fields                                 |
| ------ | -------------------------------------- |
| Matt   | lead                                   |
| Flynn  | frontend                               |
| Josix  | frontend, `infra` (lead)               |
| Phil   | frontend                               |
| Ethan  | frontend, backend, `podcast`           |
| Alice  | frontend, backend                      |
| YuYang | frontend, backend, `sponsor`           |
| Set    | backend                                |
| Maliao | backend, frontend                      |
| Max    | backend, `data`                        |
| Kaka   | backend                                |
| Benson | backend, `podcast`                     |

    
</details>


## Sept. 25th 2021

:::info
- Time: 17:30 - 19:00
- Place: 大安小樹屋（臺北市大安區信義路四段341號9樓之2-A房）[](https://thehapp.com/space/showpassword/Z8L6g)
- Participant: Matt, Benson, Set, Alice, Ethan
:::

- **Tasks (Must Done before Conf)**
    - OPass [name=matt]
    - Add info on schedule page [name=ethan]
    - speech meta tag [name=flynn]
    - schedule API for i18n [name=set]
- **Discussion**
    - 慶功宴時間地點選項
        - 地點
            - 旭集 (>1000)
            - 格萊天漾大飯店（抄贊助組）
            - 泰市場 (周末晚餐1050)
            - 饗食天堂
            - Hooters (?)
            - Fridays
        - 時間
            - 優先考慮十月的某個週末（避開國慶連假）
    - Retrospective
        - team
        - conf

## Sept. 12th 2021

:::info
- Time: 15:00 - 16:30
- Place: Online (Gather Town)
- Participant: Matt, Phil, Benson, Set, yuyang, max
:::

- **Sharing**
- **Tasks (Must Done before Conf)**
    - `frontend`
        - bugfix: attendee-only pages API calling issue [name=josix]
        - update hovering style on schedule [name=yuyang,flynn]
        - fix og meta tag of speech detail page [name=ethan]
        - add sprint page (need reviewer for [#165](https://github.com/pycontw/pycontw-2021/pull/165)) [name=matt,benson]
        - add an job listing page with new layout (see [discord](https://discord.com/channels/752904426057892052/795202959377956894/882915583350407228)) [name=phil]
        - add more info (lang, level, recording) on schedule and speech overview (see [discord](https://discord.com/channels/752904426057892052/753841328198254642/885106793422938132)) [name=matt]
    - `backend`
        - open role api: unify fields for GA metrics counter [name=matt,max]
    - `general`
        - OPass [name=matt]
        - support notification letter (see [discord](https://discord.com/channels/752904426057892052/866230224055959552/885782564357431296)) [name=matt,max]
        - create slido for each keynote/talk/tutorial [name=phil]
- **Tasks (Can be done after Conf)**
    - `frontend`
        - enable closing sponsor modal by clicking outside of it [name=alice,matt]
    - `backend`
        - Adopt django simple jwt [name=benson,maliao,matt]
- **Discussion**
    - 2022 Web squad lead 
    - Epic failure on GA integration (see [discord](https://discord.com/channels/752904426057892052/884005111448342559/884254959397376011))
- **Misc**
    - we need hosts (see [discord](https://discord.com/channels/752904426057892052/752906199715807293/885854360242913280))
    - As usual, any kind of feedback is welcome [name=matt]

## Aug. 28th 2021

:::info
- Time: 15:00 - 16:30
- Place: Online (Gather Town)
- Participant: Matt, Maliao, Set, Kaka, Alice, yuyang, phil, josix, ethan
:::
- **Sharing**
- **Task Update**
    - `frontend`
        - bugfix: attendee-only pages API calling issue [name=josix]
        - render speech description in markdown syntax [name=matt,flynn]
        - fix style of bulletin page [name=phil,flynn]
        - Slido tab displaying issue [name=phil,matt]
        - enable closing sponsor modal by clicking outside of it [name=alice,matt]
        - update hovering style on schedule [name=yuyang]
        - fix og meta tag of speech detail page [name=ethan]
    - `backend`
        - Adopt django simple jwt [name=benson,maliao,matt]
        - Any other plans XD?? [name=set] 
    - `general`
        - OPass [name=benson,yuyang,matt]
        - ~~行前信 [name=phil,set]~~
- **Tasks in Queue**
    - `general`
        - Document your knowledge in any kind of format [name=everyone]
            - e.g. [Max's blogpost](https://www.maxlist.xyz/2021/03/14/pycon-tw-web-squad/)
        - design draft for proposal system migration [name=??]
            - login/logout mechanism
    - `frontend`
        - unify coding style [name=ethan]
        - sliding navbar (as [coscup website](https://coscup.org/2021/zh-TW/)) [name=yuyang]
        - host with GCS (& CD with github action) [name=matt]
    - `backend`
        - enhence development environment
            - Amend test cases [name=phil]
            - Add mock data/fixture [name=maliao]
        - cleanup codebase [name=josix,??]
            - rm unused code
            - rm unused dependencies
        - upgrade python [name=set,phil]
        - better CI (e.g. github action) [name=set]
    - `infra`
        - expose db for ETL jobs [name=maliao]
- **Discussion**
    - Meeting in-person next time? [name=matt]
- **Misc**
    - 持續徵明年組長
      - 如果有興趣擔任 backend/frontend 小組長也歡迎報名 [name=matt]
      - 自從當了組長後我考試都考 100 分呢 :thumbsup: 


## Aug. 14th 2021

:::info
- Time: 16:30 - 18:00
- Place: Online (Gather Town)
- Participant: Matt, Alice, Phil, YuYang, Benson, Set, Kaka, Maliao, Max, Ethan, Josix
:::

- **Sharing**
    - Run frontend locally with dev backend server [name=matt]
- **Task Update**
    - `frontend`
        - roadmap 87% done (checkout [progress track](https://hackmd.io/Df_A4GStQ12PSfW1ESMKrQ)) [name=matt].
        - event overview page [name=matt]
- **Volunteer Wanted**
    - `frontend`
        - Refine readme [name=phil]
        - schedule page -- style update [name=matt]
        - fix talk/tutorial pages
            - rendering markdown syntax in detail page [name=matt]
            - category filter for talk overview [name=yuyang]
            - slido rendering issue [name=phil]
            - fail to insert og meta tag in detail page [name=Ethan]
    - `general`
        - OPass integration -- simple version [name=benson, yuyang]
            - no need to import user ID, 沒有大地遊戲, etc
            - ref. [COSCUP 2021](https://portal.opass.app/events/COSCUP_2021/)
- **Discussion**
    - 所以我說那個下一屆組長呢？[name=matt]
    - OWNERSHIP [name=matt]
- **Misc**

## July 25th 2021

:::info
- Time: 14:00-
- Place: Online (Gather Town)
- Participant: Matt, Phil, Benson, Maliao, Ethan, Set, Flynn, Kaka, Alice
:::
- **Sharing**
    - API auth token is online. What's next? [name=matt]
- **Task Update**
    - talk/tutorial page [name=matt]
    - schedule API & page [name=flynn,set]
    - SEO optimization [name=phil]
    - backend repo cleanup [name=kaka]
    - implement new style for staff list [name=ethan]
- **Volunteer Wanted**
    - `frontend`
        - fix sponsor modal [name=alice]
        - fix banner on homepage [name=yuyang]
        - fix broken style on iOS/Safari [name=??]
    - `backend`
        - planning
- **Discussion**
    - **強力徵求明年組長**
        - plans?
        - Why so early?
            - web squad never stop
            - we'll have a bunch of works to do before next CFP
            - frontend for proposal system, CI/CD, repo cleanup
- **Misc**


## July 11th 2021

:::info
- Time: 14:00-
- Place: Online (Gather Town)
- Participant: Matt, Benson, Phil, YuYang, Set, Max, Alice, Josix, Anan, Maliao
:::
- **Sharing**
    - SEO optimization todo list [name=max]
    - DRF API auth [name=benson]
- **Task Update**
    - schedule page (please finish it before the end of July) [name=set,flynn]
    - FRONTEND: we resolved 10 issues in past two weeks!
- **Volunteer Wanted**
    - `frontend`
        - Add API token in headers [name=maliao]
        - i18n for sponsor title [name=benson]
        - style: staff list [name=ethan]
        - youtube/discord page [name=Josix]
        - talk/tutorial pages [name=matt]
        - fix: disable scrolling when sponsor modal is opened [name=josix]
        - fix: og meta tag ([#102](https://github.com/pycontw/pycontw-2021/issues/102),[#103](https://github.com/pycontw/pycontw-2021/issues/103)) [name=phil]
    - `backend`
        - translation for sponsor title [name=benson]
- **Discussion**
    - 依舊還沒辦法有進度的 OPass & 大地遊戲
- **Misc**
    - 麻煩更新工作人員名單上的 discord id ([discord](https://discord.com/channels/752904426057892052/752906486581035048/863281149105930270))
    - 各位是有貢獻者票滴，先別急著訂票 (請幫忙確認[名單](https://docs.google.com/spreadsheets/d/1takXdiUFr7hy8z7YK4kvVveEp5gzp7NrL8Dk3tSOyCY/edit#gid=0))
    - [python-docs-zh-tw](https://github.com/python/python-docs-zh-tw) is calling for volunteers

## June 27th 2021

:::info
- Time: 14:00-
- Place: Online (Gather Town)
- Participant: Matt, Maliao, YuYang, Phil, Flynn, kaka, Set, Josix, Benson, Alice, Ethan
:::

- **Sharing**
    - Assign/adopt issue & close issue with PR [name=matt]
    - Deploy archived website [name=maliao]
    - API for KKTIX token auth [name=kaka]
- **Task Update**
    - `general`
        - PyCon TW 2021 has postponed to Oct. 2nd & 3rd
        - waiting for venue team [name=matt]
            - co-organizer data
            - covid19 guideline
    - `frontend`
        - keynote page is almost done [name=matt]
        - CoC page implementation [name=josix]
    - `backend`
        - keynote api is almost done [name=yuyang]
        - API auth [name=benson,set]
- **Volunteer Wanted**
    - `frontend`
        - ticket info [name=phil]
        - sponsor prospectus styling [name=yuyang]
        - youtube & discord page [name=matt]
    - `backend`
        - clean up deprecated code [name=matt, set]
- **Discussion**
    - KKTIX API meeting is at 4pm (after this meeting) ([discussion](https://discord.com/channels/752904426057892052/845976899846275083/853635345706516541))
- **Misc**
    - 距離第一次聚會已經屆滿半年惹啊～
    - T-Shirt size ([link](https://docs.google.com/forms/d/e/1FAIpQLSf7K9tllMG53FBnwUi2u_VRwoQsPpxkPLWwaKLiKdb8KSiNgg/viewform))
    - 上傳大頭貼ＲＲＲ([discord thread](https://discord.com/channels/752904426057892052/753841328198254642/845949787283128340))

## June 13th 2021

:::info
- Time: 16:00-
- Place: Online (Gather Town)
- Participant: Matt, Alice, Phil, Benson, Set, Flynn, YuYang, Maliao, Ethan, Josix, Anan
:::

- **Sharing**
- **Task Update**
    - PyCon TW 2021 will be held online
        - OPass: in discussion with sponsor team [name=benson,yuyang]
        - COVID19 guideline: the content will be modified by venue team [name=phil]
        - ticket info: registration team is planning new ticket info [name=??]
        - etc
    - Meeting with design team ([ticket](https://trello.com/c/YVHRRZ7u))
        - Zeplin or Figma: use Figma only but transfer to Zeplin next year
        - Organize the flow/config [name=flynn] 
        - Inform design team after every frontend deployment
    - `frontend`
        - PR ongoing
            - Keep follow up!
        - PR next week
            - about pages (last two) [name=josix]
            - talk/tutorial overview & detail page [name=matt]
            - schedule page [name=flynn, set]
- **Volunteer Wanted**
    - `frontend`
        - ticket info [name=matt]
        - PyCon TW intro on index page [name=phil]
        - sponsor prospectus styling [name=alice]
        - 404 page [name=phil]
    - `backend`
        - GET API for keynote [name=yuyang, set]
- **Discussion**
- **Misc**
    - remember to check message on discord once every couple days
    
![](https://i.imgur.com/12N2iyu.png)


## May 30th 2021

:::info
- Time: 20:00-
- Place: Online (Gather Town)
- Participant: Matt, Set, Flynn, Phil, Alice, Max, Maliao, Benson, Ethan
:::

- **Sharing**
- **Task Update**
    - `general`
    - `backend`
        - Need to be done this week
            - Review event APIs [name=set]
        - Before next meetup
            - API authentication [name=set, benson]
            - Revamp the attendee-related app ([ticket](https://trello.com/c/vYNToMLT)) [name=kaka]
                - [design doc](https://hackmd.io/oaue82LKTkC-KjHKxNvZhg)
    - `frontend`
        - Reviewing
            - (by matt) Image gallery on index page [name=Ethan]
            - (by matt) Add COVID-19 guideline page [name=Phil]
            - (by matt) Card component for event overview [name=Ethan]
        - Need to be done this week
            - About pages (first 2) [name=Josix]
        - Before next meetup
            - Card component for bulletin on index page [name=Alice]
            - About pages (last 2) [name=Josix]
            - Job listing page [name=flynn]
    - `OPass`
        - OPass note ([link](https://hackmd.io/HqCx4jBPQHuJZAsqov8NjQ)) [name=matt,benson,yuyang]
- **Volunteer Wanted**
    - `general`
        - Test & deploy archived historical static website [name=maliao]
    - `backend`
        - TBD
    - `frontend`
        - add og tag [name=ethan]
- **Discussion**
    - What's changed after COVID-19 outbreak?
- **Misc**
![](https://i.imgur.com/i1Eb6oO.jpg)


## Apr. 30th 2021

:::info
- Time: 17:00-20:00
- Place: 小樹屋-南京復興A (南京東路三段200號5樓507室-A)
- Participant: Matt, Benson, Phil, Josix, Flynn, Alice, Anan, Kaka, Set, Maliao
:::

- **Sharing**
    - Let's change how we go through this part [name=matt]
        1. Talk about what you've done in the past two weeks (talk to matt in advance if you can't make it)
        2. Share anything you want (it doesn't have to be something related to pycon)
    - Data studio for Linkedin data analysis ([link](https://datastudio.google.com/reporting/a08116b7-3ab1-4623-b981-e77e4d64094d/page/vaWFC)) [name=max]
    - Auto-deployment template for Azure AIoT services ([link](https://github.com/kaka-lin/azure-intelligent-edge-patterns/tree/feat/change-custom-arm-template)) [name=kaka]
- **Task Update**
    - `general`
        - New member YuYang!
            - Developer with Vue & GCP experience but would like to learn about Django
            - Deal with requests from sponsor team (especially OPass part) -> work with Benson
    - `backend`
        - Need to be done in this weekend
            - Review event APIs [name=set]
        - Before next meetup
            - API authentication [name=set, benson]
    - `frontend`
        - Need to be done in this weekend
            - Sponsor list on index page [name=matt, flynn]
            - Revamp banner on index page [name=flynn]
        - Before next meetup
            - Card component for event overview [name=Ethan]
            - Image gallery on index page [name=Ethan]
            - (??) Card component for bulletin on index page [name=Alice]
            - Add COVID-19 guideline page [name=Phil]
            - About pages (2 out of 4) [name=Josix]
    - `OPass`
        - Before next meetup
            - Finish document & sync with benson & yuyang [name=matt]
- **Volunteer Wanted**
    - `backend`
        - Revamp the attendee-related app (previously called `ext2020`) ([ticket](https://trello.com/c/vYNToMLT)) [name=kaka]
- **Discussion**
    - `backend`
        - bugfix: mistery queryset issue ([PR](https://github.com/pycontw/pycon.tw/pull/1010)) [name=matt]
- **Misc**
    - 1-on-1 section: Max & Alice
    - Let's take a photo!

## Apr. 18th 2021

:::info
- Time: 11:30 A.M.
- Place: 鈾咖啡（[台北市大安區復興南路一段253巷32號](https://www.google.com/maps/place/Uranium+Cafe/@25.0367044,121.5428418,17z/data=!3m1!4b1!4m5!3m4!1s0x3442abd17ba55aab:0x994b55a06d2abe5a!8m2!3d25.0366996!4d121.5450305)）B1
- Participant: Matt, Benson, Phil, Set, Maliao, Ethan, Max, Pinchun
:::

- **Sharing**
    - Update sponsor logo on GCS [name=max, sponsor team]
- **Task Update**
    - `frontend`
        - Basic styling for new layout ([PR](https://github.com/pycontw/pycontw-2021/pull/29)) [name=flynn, matt]
        - Canonical URL for better SEO ([PR](https://github.com/pycontw/pycontw-2021/pull/29)) [name=matt]
    - `backend`
        - API design [name=max]
        - Remove deprecated code (WIP) [name=matt]
        - Adopt flake8 ([PR](https://github.com/pycontw/pycon.tw/pull/1006)) [name=matt]
        - hotfixes:
            - CoC agreement page redirection failed after set languange ([pycon.tw#1003](https://github.com/pycontw/pycon.tw/pull/1003))
            - Migration scripts sequence changed ([pycon.tw#1004](https://github.com/pycontw/pycon.tw/pull/1004))
            - Failed to generate token for password reset link ([pycon.tw#1005](https://github.com/pycontw/pycon.tw/pull/1005))
    - `podcast`
        - Progress sync [name=benson, ethan]
            - ref: https://podcast.overbuild.io/
- **Volunteer Wanted**
    - `frontend`
        - pages styling
    - `backend`
        - Grant GCS permission to GCE VM ([ticket](https://trello.com/c/ffq5ZMXX))
- **Discussion**
    - OPass integration (will be kicked-off soon) [name=matt]
- **Misc**
    - 1-on-1 section [name=matt]


## Apr. 5th 2021

:::info
- Time: 20:30
- Place: Online ([Google Meet](https://meet.google.com/asu-tvnw-nbz))
- Participant: Matt, Alice, Ethan, Kaka, Flynn, Phil, Josix, Maliao, Benson
:::

- **Sharing**
    - `frontend`
        - How to run local dev server [name=Matt]
            - simply run `docker-compose -f ./docker-compose-dev.yml up`
    - `general`
        - travis CI update [name=alice]
- **Task Update**
    - `general`
        - New frontend & backend URLs ([discord link](https://discord.com/channels/752904426057892052/753841328198254642/826536426162094112))
            - frontend: [`pycon.tw/2021`](https://pycon.tw/2021)
            - backend: [`pycon.tw/prs`](https://pycon.tw/prs)
    - `frontend`
        - Implementation of new pages [name=alice,maliao] 
    - `backend`
        - Remove deprecated code [name=kaka]
        - API design [name=max]
- **Volunteer Wanted**
    - Change the style for Proposal & Review System ([figma](https://www.figma.com/file/1za4uYNpSonvgxdcLoHAzs/PyCon-Taiwan-2021-Web?node-id=1117%3A0)) [name=]
    - Backend API Authentication [name=set, benson]
    - Add FA page [name=josix]
    - Dispatch styling tasks based on [Figma](https://www.figma.com/file/1za4uYNpSonvgxdcLoHAzs/) [name=flynn, matt]
- **Discussion**
    - Q&A time
- **Misc**
    - Live code review

## Mar. 21st 2021

:::info
- Time: 17:30
- Place: 鈾咖啡（[台北市大安區復興南路一段253巷32號](https://www.google.com/maps/place/Uranium+Cafe/@25.0367044,121.5428418,17z/data=!3m1!4b1!4m5!3m4!1s0x3442abd17ba55aab:0x994b55a06d2abe5a!8m2!3d25.0366996!4d121.5450305)）B1
- Participant: Matt, Flynn, David, Wei, Ethan, Max, Kaka, Phil, Set, Josix
:::

- **Sharing**
    - Remove old website routes ([pycon.tw/#989](https://github.com/pycontw/pycon.tw/pull/989)) [name=kaka]
    - Newbie doc for backend project ([link](https://hackmd.io/@pycontw/HJlGuL1Nu)) [name=max]
- **Task Update**
    - `frontend`
        - [Frontend wireframe beta version](https://www.figma.com/file/1za4uYNpSonvgxdcLoHAzs/) 
            - 我說你各位都該看看這個
        - Now we have a wrapper for page RWD 🚀 ([pycontw-2021/#17](https://github.com/pycontw/pycontw-2021/pull/17)) [name=flynn]
        - Implementation of new pages [name=alice,maliao]
    - `backend`
        - Remove deprecated code [name=kaka]
        - API design [name=max]
- **Volunteer Wanted**
    - `frontend`
        - Add `font awesome` (design team needs it) [name=flynn]
    - `backend`
        - Test & deploy following PRs today
            - new database is opened [name=set]
            - remove old routes ([#989](https://github.com/pycontw/pycon.tw/pull/989)) [name=kaka]
            - add new field for sponsor model ([#990](https://github.com/pycontw/pycon.tw/pull/990)) [name=max] 
            - fix how-to links ([#985](https://github.com/pycontw/pycon.tw/pull/985)) [name=set]
        - ideas: archiving websites rather than running the servers ([discord](https://discord.com/channels/752904426057892052/753841328198254642/821574164145111090)) [name=matt]
            - will kickoff around 2 weeks later
- **Discussion**
    - Q for data team: whether `tw.pycon.org` is better than `tw.pycon.org/2021`
- **Misc**
    - Please do 1-on-1 in person rather than on Discord (~~matt 不想努力了~~) [name=matt]
    - Podcast will be online soon (around the end of April)
    
## Mar. 6th 2021

:::info
- Time: 17:30
- Place: [ALL DAY ROASTING COMPANY](https://www.facebook.com/alldayroastingcompany)（[台北市松山區延壽街329號](https://www.google.com/maps/place/All+Day+Roasting+Company/@25.0568318,121.5580683,17z/data=!3m1!4b1!4m5!3m4!1s0x3442ab92d6b3634f:0x7b063d11bea47c46!8m2!3d25.056827!4d121.560257)）
- Participant: Matt, Alice(Online), Flynn, Maliao, Kaka, Max, Set
:::

- **Sharing**
- **Task Update**
    - `frontend`
        - RWD: WIP ([ticket](https://trello.com/c/wSM2MMNe)) [name=flynn, matt, ??]
    - `backend`
        - bugfixes ([ticket](https://trello.com/c/7C46zlJQ))
        - GCS migration
- **Volunteer Wanted**
    - Add a new field for subtitle of sponsor ([ticket](https://trello.com/c/vICfFVL6)) [name=max]
    - Remove old templates in `pycon.tw` ([ticket](https://trello.com/c/XwSMahbb)) [name=matt, kaka, ethan]
    - Add privacy policy page ([ticket](https://trello.com/c/pJZiIM6D)) [name=maliao]
    - Bugfix for `pycon.tw`: failed to link to zh-hant page on `pycontw-2021` ([ticket](https://trello.com/c/DfwIewtL)) [name=set]
    - API desgin for conference ([ticket](https://trello.com/c/6NTbQkif)) [name=set, kaka, max]
    - Fixtures for offline testing ([ticket](https://trello.com/c/u8iJUhRd)) [name=flynn]
- **Misc**
    - Who's responsible for podcast-related stuff? ([ticket](https://trello.com/c/JJkX50zE)) [name=ethan]
    - Our next goal: self-functioning team

## Feb. 21st 2021

:::info
- Time: 14:00
- Place: 鈾咖啡（[台北市大安區復興南路一段253巷32號](https://www.google.com/maps/place/Uranium+Cafe/@25.0367044,121.5428418,17z/data=!3m1!4b1!4m5!3m4!1s0x3442abd17ba55aab:0x994b55a06d2abe5a!8m2!3d25.0366996!4d121.5450305)）
- Participant: Matt, Max, Maliao, Alice, Set, Ethan
:::

- **Sharing**
    - Learning Vue/Nuxt during CNY ([PR](https://github.com/pycontw/pycontw-2021/pull/9)) [name=Matt]
    - CFP stage change ([ticket](https://trello.com/c/ktAYKJg3)) [name=Matt]
    - GitHub Action 上傳 github repo 至 GCP Storage https://github.com/hsuanchi/update-storage-by-github-action/tree/main [name=Max]
- **Task Update** 
    - Codebase Restruction
        - deployed and the landing page is retired
    - Architecture Restruction: [Draft](https://hackmd.io/WQXHi6QvSs-aXViXKdVV9w) (volunteers wanted)
    - Fix CFP bugs ([ticket](https://trello.com/c/j0ezAODh), volunteers wanted)
    - Upload img to GCS ([ticket](https://trello.com/c/TKTeVtlI))
- **Misc**
    - Anyone ever played with CMS?
        - 隔壁棚議程組: 「與開發網頁組討論，將podcast丟到官網上的可能性(包含錄音、筆記)」
    - [Asked for feedback last month](https://hackmd.io/xjv30HsdQyKeq0w-AEcPGA?view#Jan-17th-2021) but no one replied [name=Matt]
        - Will pm each squad member for feedback on discord in recent days
    
## Jan. 31st 2021

:::info
- Time: 14：00
- Place: 上樓看看 (台北市信義區忠孝東路五段165巷3弄6號)
- Participant: Matt, Josix, Flynn, Set, Max, Alice (online)
:::

- **Sharing**
    - Codebase Restruction: Intro of current frontend repo [name=Flynn]
    - The forgotten `makemigrations` & `makemessages` commands [name=Matt]
    - Intro i18n best practice ([link](https://www.maxlist.xyz/2020/10/04/hreflang-seo-optimize/)) [name=Max]
- **Task Update** 
    - Closing 2020
        - [branch `pycontw-2020`](https://github.com/pycontw/pycon.tw/tree/pycontw-2020) & [release tag `2020-final`](https://github.com/pycontw/pycon.tw/releases/tag/2020-final) are created.
    - Codebase Restruction
        - Try deploying to GCS
    - CFP
        - Add 1st-time speaker tickbox ([#973](https://github.com/pycontw/pycon.tw/pull/973))

## Jan. 17th 2021

:::info
- Time: 14:00
- Place: 上樓看看 ([台北市信義區忠孝東路五段165巷3弄6號](https://goo.gl/maps/JV8skvF2Zrnvg8Nu6))
- Participant: Matt, kaka, Alice, Flynn, Max, Set
:::

- **Who Need GCP Access?** [name=Matt]
    - Flynn & Set for [codebase restruction](https://trello.com/c/Xj8wj3yd)
        - SSH to staging/production GCE
        - GCE & GCS
    - Ethan for [SSL bug investigation](https://trello.com/c/Fe5FknSc)
        - SSH to sstaging/production GCE
    - Max & Set for [firewall rule adjustment](https://trello.com/c/cN5xsdWd)
        - GCE
    - Max, Kaka, & Maliao for Landing Page
        - GCS
- **Sharing**
    - Landing page ([ticket](https://trello.com/c/YLvopA2u))
        - [Redirection with Nginx](https://github.com/pycontw/pycontw-nginx/pull/2) & hosting website with GCS ([name=Maliao & Max])
    - Codebase Restruction
        - [use_drf_to_implement_api](https://github.com/setmao/pycon.tw/commits/use_drf_to_implement_api)
- **Task Update** 
    - Closing 2020
        - steps:
            - merge 2020 PR
            - release tag for 2020
            - merge 2021 backend templates
            - deploy 2021 frontend
    - Codebase Restruction ([ticket](https://trello.com/c/Xj8wj3yd))
        - DEADLINE: Feb. 1st!!!
    - Recruiting Info ([ticket](https://trello.com/c/CE0Q7Nxk))
        - Need helpers who good at writing QQ
    - Review the documents we wrote ([ticket](https://trello.com/c/Nnb1a05e))
- **Misc**
    - It's been a quarter since our 1st meetup
        - Please talk to Matt if you got any feedback!
        - What has changed

## Jan. 3rd 2021

:::info
- Time: 16:00
- Place: [和貓咪有約](https://www.facebook.com/%E5%92%8C%E8%B2%93%E5%92%AA%E6%9C%89%E7%B4%84-265408243983824/) (105台北市松山區三民路3巷21號)
- Participant: Matt, Alice, Max, Maliao, Set, Flynn, Ethan, Kaka
:::

- **Chit-chat** [name=Matt]
  - We're working in the community. We need over-communication.
    - Development: 
      - Design first. Always make sure you're on the right track. Write the design doc if needed.
      - Try to [write good PR](https://google.github.io/eng-practices/review/developer/) & [good commit messages](https://chris.beams.io/posts/git-commit/).
    - Collaboration:
      - It's always ok to ask for help.
      - It's encouraged to show your code (even it's shitty) before sending PR (you can make it a [draft](https://github.blog/2019-02-14-introducing-draft-pull-requests/)).
      - It's not ok to say that you cannot make it couple days before deadlines (& we mostly have deadlines).
- **Sharing**
  - Landing page ([ticket](https://trello.com/c/YLvopA2u))
  - Codebase Restruction ([ticket](https://trello.com/c/Xj8wj3yd))
  - [This ticket](https://trello.com/c/oMKrB2gj) [name=Matt]
    - How we currently deal the data dump from DB? What can be improved?
- **Needs Reviewing**
  - Review the [recruiting info](https://hackmd.io/0cY9xO9HQ1K44Oq5ARlbhw?view#Web) [name=Matt]
  - Review the documents we wrote ([ticket](https://trello.com/c/Nnb1a05e)) -> nothing done yet
- **Call for help**
  - [SSL expiration issue](https://trello.com/c/Fe5FknSc)

## Dec. 5th 2020

:::info
- 18:30 @ [羊毛與花‧永康](https://maps.app.goo.gl/ZX3GX2yWPBAZWmwY6) (台北市大安區永康街37巷12號)
- Participant: Matt, Flynn, Set, Kaka, Max, Alice 
:::

- **Landing page** ([ticket](https://trello.com/c/YLvopA2u))
    -  Code review for the [beta version](https://github.com/Maliaotw/pycon.tw/tree/pr_2021_landing) -> still WIP [name=Kaka, Max]
- **Repo reconstruct** ([ticket](https://trello.com/c/Xj8wj3yd))
    - Pin down 1st edition schedule -> WIP [name=Flynn, Set, Matt]
    - Decided that we keep the Reviews and Proposals apps as Django, but build the official website in Vue.js
    - Pinned down a rough schedule [name=Set, Flynn]:
        * ~12/31 Scaffolded project structure for the frontend website -> CI/CD for embedding transpiled files into Django template -> Backend + Frontend integration test
        * ~2/1 Complete everything designed except for the event schedule
- **Back stage** ([#782](https://github.com/pycontw/pycon.tw/pull/782))
    - Review current progress & issues [name=Matt & Alice]
    - ~~[optional] find a volunteer helper~~ Matt will help out on this task
- **Documents** ([ticket](https://trello.com/c/Nnb1a05e))
    - _volunteers wanted_
