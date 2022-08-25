---
tags: 2021-organize, 2021-web, dev team
---

<style>
.red {
  color: red;
}
</style>

# PyCon TW website document

## Header
![](https://i.imgur.com/i1eDKFG.png)
1. 語系切換
2. Navbar
    1. 關於(About)
    2. 議程(Conference)
        1. 時間表(Schedule)
        2. 基調演講(Keynotes)
        3. 一般演講(Talks)
        4. 專業課程(Tutorials)
        5. ~~社群軌(Community Track)~~
    3. 活動(Events)
        1. 總覽(Overview)
        2. 暖身活動(Warm-Up Session)
        3. 開放空間(Open Spaces)
        4. 衝刺開發(Sprints)
        5. 徵才資訊(Job Listing)
    5. 註冊(Registration)
        1. 會議門票(Conference Ticket)
        2. 財務補助(Financial Aid)
    7. 會場(Venue)
    8. COVID-19 防疫守則(COVID-19 Guidelines)
3. Social media link
    1. Blog
    2. Facebook
    3. Twitter
    4. Email
4. My PyCon

## Footer
![](https://i.imgur.com/hg3ce4Z.png)
1. 歷年網站連結
2. 行為準則
3. 工作人員
4. 社群
5. 個人資料保護聲明

## Pages
1. [首頁](https://tw.pycon.org/2020/zh-hant/)
    - API: [/sponsors/](https://hackmd.io/pio2HdWXRZiMPKXOANe-FQ?view#sponsors)
2. [關於(About)](https://tw.pycon.org/2020/zh-hant/about/pycontw/)
3. [贊助主頁(Sponsor)](https://tw.pycon.org/2020/zh-hant/sponsor/sponsor/)
4. [贊助方案(Sponsor Prospectus)](https://tw.pycon.org/2020/zh-hant/sponsor/prospectus/)
5. [投稿募集(CFP)](https://tw.pycon.org/2020/zh-hant/speaking/cfp/)
6. [錄影釋出(Recording)](https://tw.pycon.org/2020/zh-hant/speaking/recording/)
7. [如何投稿演講(Talk Proposal)](https://tw.pycon.org/2020/zh-hant/speaking/talk/)
8. [如何投稿專業課程(Tutorial Proposal)](https://tw.pycon.org/2020/zh-hant/speaking/talk/)
9. [時間表(Schedule)](https://tw.pycon.org/2020/zh-hant/conference/schedule/)
    - API: [/conference/schedule/](https://hackmd.io/pio2HdWXRZiMPKXOANe-FQ?view#ScheduleView)
10. [基調演講(Keynotes)](https://tw.pycon.org/2020/zh-hant/conference/keynotes/)
11. [一般演講(Talks)](https://tw.pycon.org/2020/zh-hant/conference/talks/)
    - API: [/conference/talks/](https://hackmd.io/pio2HdWXRZiMPKXOANe-FQ?view#TalkListView)
12. 演講詳細頁
    - API: [/conference/talk/{id}/](https://hackmd.io/pio2HdWXRZiMPKXOANe-FQ?view#TalkDetailView)
13. [專業課程(Tutorials)](https://tw.pycon.org/2020/zh-hant/conference/tutorials/)
    - API: [/conference/tutorials/](https://hackmd.io/pio2HdWXRZiMPKXOANe-FQ?view#TutorialListView)
14. 課程詳細頁
    - API: [/conference/tutorial/{id}/](https://hackmd.io/pio2HdWXRZiMPKXOANe-FQ?view#TutorialDetailView)
15. ~~[社群軌(Community Track)](https://tw.pycon.org/2020/zh-hant/conference/community-track/)~~
16. [總覽(Overview)](https://tw.pycon.org/2020/zh-hant/events/overview/)
17. [暖身活動(Warm-Up Session)](https://tw.pycon.org/2020/zh-hant/events/warmup-session/)
18. [開放空間(Open Spaces)](https://tw.pycon.org/2020/zh-hant/events/open-spaces/)
15. [衝刺開發(Sprints)](https://tw.pycon.org/2020/zh-hant/events/sprints/)
16. [徵才資訊(Job Listing)](https://tw.pycon.org/2020/zh-hant/events/job-listings/)
    - API: [/events/job-listings/](https://hackmd.io/pio2HdWXRZiMPKXOANe-FQ?view#Job-Listings)
17. [會議門票(Conference Ticket)](https://tw.pycon.org/2020/zh-hant/registration/ticket-info/)
18. [財務補助(Financial Aid)](https://tw.pycon.org/2020/zh-hant/registration/financial-aid/)
19. [會場(Venue)](https://tw.pycon.org/2020/zh-hant/venue/)
20. [COVID-19 防疫守則(COVID-19 Guidelines)](https://tw.pycon.org/2020/zh-hant/covid-19/guidelines/)


---

## 開發順序

### [P1](deadline: 2021/1/31)
 1. [首頁](https://tw.pycon.org/2020/zh-hant/)
    - API: [/sponsors/](https://hackmd.io/pio2HdWXRZiMPKXOANe-FQ?
 2. [關於(About)](https://tw.pycon.org/2020/zh-hant/about/pycontw/)
    - content: copy from 2020
 4. [贊助主頁(Sponsor)](https://tw.pycon.org/2020/zh-hant/sponsor/sponsor/)
    - content: copy from 2020
 5. [贊助方案(Sponsor Prospectus)](https://tw.pycon.org/2020/zh-hant/sponsor/prospectus/)
    - content: [zh-hant](https://hackmd.io/@pycontw/BJdBx0f2P), [en-us](https://hackmd.io/@pycontw/HyOJeEI-O)
 6. [投稿募集(CFP)](https://tw.pycon.org/2020/zh-hant/speaking/cfp/)
 7. [錄影釋出(Recording)](https://tw.pycon.org/2020/zh-hant/speaking/recording/)
 8. [如何投稿演講(Talk Proposal)](https://tw.pycon.org/2020/zh-hant/speaking/talk/)
 9. [如何投稿專業課程(Tutorial Proposal)](https://tw.pycon.org/2020/zh-hant/speaking/talk/)


### [P2](deadline: ？)
 1. [時間表(Schedule)](https://tw.pycon.org/2020/zh-hant/conference/schedule/)
    - API: [/conference/schedule/](https://hackmd.io/pio2HdWXRZiMPKXOANe-FQ?view#ScheduleView)
 2. [基調演講(Keynotes)](https://tw.pycon.org/2020/zh-hant/conference/keynotes/)
 3. [一般演講(Talks)](https://tw.pycon.org/2020/zh-hant/conference/talks/)
    - API: [/conference/talks/](https://hackmd.io/pio2HdWXRZiMPKXOANe-FQ?view#TalkListView)
 4. 演講詳細頁
    - API: [/conference/talk/{id}/](https://hackmd.io/pio2HdWXRZiMPKXOANe-FQ?view#TalkDetailView)
 5. [專業課程(Tutorials)](https://tw.pycon.org/2020/zh-hant/conference/tutorials/)
    - API: [/conference/tutorials/](https://hackmd.io/pio2HdWXRZiMPKXOANe-FQ?view#TutorialListView)
 6. 課程詳細頁
    - API: [/conference/tutorial/{id}/](https://hackmd.io/pio2HdWXRZiMPKXOANe-FQ?view#TutorialDetailView)
 7. [暖身活動(Warm-Up Session)](https://tw.pycon.org/2020/zh-hant/events/warmup-session/)
 8. [開放空間(Open Spaces)](https://tw.pycon.org/2020/zh-hant/events/open-spaces/)
 9. [衝刺開發(Sprints)](https://tw.pycon.org/2020/zh-hant/events/sprints/)
10. [徵才資訊(Job Listing)](https://tw.pycon.org/2020/zh-hant/events/job-listings/)
    - API: [/events/job-listings/](https://hackmd.io/pio2HdWXRZiMPKXOANe-FQ?view#Job-Listings)
11. [會議門票(Conference Ticket)](https://tw.pycon.org/2020/zh-hant/registration/ticket-info/)
12. [COVID-19 防疫守則(COVID-19 Guidelines)](https://tw.pycon.org/2020/zh-hant/covid-19/guidelines/)
13. [財務補助(Financial Aid)](https://tw.pycon.org/2020/zh-hant/registration/financial-aid/)
 9. [總覽(Overview)](https://tw.pycon.org/2020/zh-hant/events/overview/)
10. [會場(Venue)](https://tw.pycon.org/2020/zh-hant/venue/)
