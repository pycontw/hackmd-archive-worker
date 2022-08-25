---
tags: organize, dev, web
---

[TOC]

# Website
網站有幾個重要的時間點需要配合整個大會
* [新的 Landing Page](#新的-Landing-Page)
* [Call for Proposals (CfP)](#Call-for-Proposals-CfP)
* [Review Process (Stage 1 / 2)](#Review-Process-Stage-1--2)
* [Talk Announcement](#Talk-Announcement)
* [Final (行前信之前)](#Final-行前信之前)

2020 年網站的跑法，是以 2019 年網站的內容當作是依據，再根據 20 年的需求，將上述每一個 milestone 回推時間。每個時間點大概只能顧及最近的 milestone 的事情，而比較難以一個整體的面向來考量，這也許是 21 年可以改善的地方。例如，以一個非籌備者的角度來審視 CfP、審稿、報名研討會這些事項，網站或者是相關資訊的揭露是否已經都完備。

## 環境
**當年度**都是使用 `master` branch。所以換了新年度時，確認一下前一年度是否有把最後的 repository tag 起來，例如 `2020-final`。

網址的規則是 https://tw.pycon.org [(ref)](https://github.com/pycontw/pycontw-nginx/blob/master/conf/tw-pycon-org.conf) 以及 https://pycon.tw [(ref)](https://github.com/pycontw/pycontw-nginx/blob/master/conf/pycon-tw.conf) 都會 302 redirect 到**當年度**，例如 [http://tw.pycon.org/**2020**](http://tw.pycon.org/2020)。

總括來說，新的一年度，例如 2021，要開始時，確保前一年度的 repository 有 tag 起來，接著就可以在 production 開新的資料夾，起新的 docker，接著再來設定 nginx 的轉址規則。當然，也要確保開發環境可以跑得起來，這也需要花些時間。

### 需要交接的東西
* Github Organisation / pycon.tw 權限
* Transifex 權限 (project maintainer) <-- 這個其實可以不用
* Google Cloud 權限
* 怎麼 Deploy / 連線進入機器
* Google Drive 權限
* Slack / Telegram (or Discord)
* Web SMTP credentials
* Mailchimp 權限 (行前信使用)


## 新的 Landing Page
上線時間：前一年結束大概兩週後到一個月就可以上了。但最慢可以拖到 CfP 之前一兩週。

很快速的搭建一個新的頁面，很簡陋沒有關係，但重點是要有志工報名，一個連到 Google Form 的連結。

## Call for Proposals (CfP)
上線時間：CfP 開始之前

這一段時間工作會蠻繁重的，以 2020 年為例，CfP 上線時，是連同新一年的視覺一起上線的。工作項目表列如下：
* CfP 介紹的相關頁面 ([Talk](https://tw.pycon.org/2020/zh-hant/speaking/talk/), [Tutorial](https://tw.pycon.org/2020/zh-hant/speaking/tutorial/), [Recording](https://tw.pycon.org/2020/zh-hant/speaking/recording/), [CfP](https://tw.pycon.org/2020/zh-hant/speaking/cfp/))
* Submit Proposal (Talk/Tutorial) 功能
* 大會相關簡介頁面 ([About](https://tw.pycon.org/2020/zh-hant/about/pycontw/), [CoC](https://tw.pycon.org/2020/zh-hant/about/code-of-conduct/), [Community](https://tw.pycon.org/2020/zh-hant/about/community/))
* 贊助簡易頁面 ([Sponsor](https://tw.pycon.org/2020/zh-hant/sponsor/sponsor/), [Prospectus](https://tw.pycon.org/2020/zh-hant/sponsor/prospectus/))
* [Financial Aid](https://tw.pycon.org/2020/zh-hant/registration/financial-aid/) 以及[場地](https://tw.pycon.org/2020/zh-hant/venue/)
* 新一年的視覺 & front end engineering

內外需要協調的有：
* 視覺設計師的設計要全部出來 --> 前端工程
* 議程組提供相關文案，例如 Talk/Tutorial 長度、哪些分類、如何投稿等說明文件 (雖然來年的資料都有，但仍要確認是否適用於該年度之規劃)
* 確認議程組在 CfP 所需要的欄位是否有異動，以及 My Dashboard、表單等後台功能正常運作
* 贊助組需要拉贊助的方案以及文案需要提供

以上工作項目以 CfP 為目標回推，約莫兩個月前就要開始準備了。

## Review Process (Stage 1 / 2)
時間點：CfP close，開始 review 之前

這邊的重點是要確保 review 的相關功能都可以正常運作。Repository 上的 reviews 有個[鉅細靡遺的說明文件](https://github.com/pycontw/pycon.tw/tree/master/src/reviews)，說明整個 review process 所需要做的設定。

### Export TalkProposals
這邊沒有特別說明的，是在 First Round Review (3) 結束時，議程組長通常需要做一次**針對 TalkProposals 這個 Model** 匯出的動作。主要是看各個階段 +1 +0 -0 -1 的人數 [(source)](https://github.com/pycontw/pycon.tw/blob/master/src/proposals/resources.py)。

### Snapshot
再來是從 First Round Review (3) 進到 Modification Stage (4) 之前，需要做一次 snapshot [(source)](https://github.com/pycontw/pycon.tw/blob/master/src/reviews/management/commands/snaptalks.py)。也就是需要進到 production 裡面下指令
```shell
$ ./manage.py snaptalks
```

註解：請仍然詳細閱讀 snaptalks 的原始碼。2020 年由於應該要執行這個指令時，已經錯過時間了，導致實際執行方式是把過去的 DB 在別的地方還原過後，使用 [dumpdata](https://docs.djangoproject.com/en/3.0/ref/django-admin/#dumpdata) 的方式把 TalkProposals 全部倒出來，再使用下列指令做 snaptalks 的
```shell
$ ./manage.py snaptalks --dump dumpdata.TalkProposals.0508.json
```
或說
```shell
$ docker exec -it pycontw-2020 ./manage.py snaptalks --dump ...
```

snapshot 主要的用途是在於先把所有送出提案的講者，在他們第一次提交後做一次 snapshot，當他們在第一輪審查結束，看到審稿委員們的意見，修改提案之後，在第二輪審查時，審稿委員們可以看得出 diff。

### Export TalkProposals Again
第二輪結束後，議程組長會再一次的需要投稿提案的匯出表單，以作為最後決定的依據。


## Talk Announcement
上線時間：確認已接受的講題後，以及公佈售票左右

由於 CfP 階段時很有可能只將當時所需的頁面做前端工程，因此這個階段的下面頁面也需要
* [Keynotes](https://tw.pycon.org/2020/zh-hant/conference/keynotes/)
* [Talk List](https://tw.pycon.org/2020/zh-hant/conference/talks/)
* [Talk Detail](https://tw.pycon.org/2020/zh-hant/conference/talk/1126732952315625799/)
* [Tutorial List](https://tw.pycon.org/2020/zh-hant/conference/tutorials/)
* [Tutorial Detail](https://tw.pycon.org/2020/zh-hant/conference/tutorial/1138520345397952532/) (這個跟 Talk Detail 其實是同一個 template)
* [Ticketing](https://tw.pycon.org/2020/zh-hant/registration/ticket-info/)

這一段頁面的公佈邏輯，是因應準備開始售票，所以這個研討會有哪些 Talks、Keynotes、Tutorials 等就應該要先行公佈，連帶公佈售票的細節。

## Final (行前信之前)
*Talk Announcement* 到 *Final (行前信之前)* 之間，有下列事項會需要陸續上路
* 主議程表 (主議程表是一個大項目，一些說明[請見下方](#主議程表))
* 首頁贊助商 Logo 與細節露出
* 場地交通車細節
* 剩下此時才能確定的活動，如 [Open Spaces](https://tw.pycon.org/2020/zh-hant/events/open-spaces/), [Sprints](https://tw.pycon.org/2020/zh-hant/events/sprints/), PyNight 等


以上最後上線的細節，一個建議的搭配方式，是以**會眾**的角度從[活動總覽](https://tw.pycon.org/2020/zh-hant/events/overview/)頁面出發，一項一項檢視該出現的資訊是否完備。然後可以用同樣的模式來看最後大魔王 Deadline -- **行前信**，也就是以行前信為所有總覽的內容，一項一項檢視網站或行前信內容是否有遺漏。

### 行前信
上線時間：**行前信之前**

**行前信大概是最重要的日程**。行前信會有所有活動的最詳細細節，因此上面幾乎會列出所有的事項。而在寄出的時候，**幾乎等於是網站上面所有在行前信上面會被提到的事情，都要全數 ready**。

因此要特別注意的是與 OPass 的串接，以及相關活動頁面。基本上大概在會期前的兩個月就要開始跟 OPass 的人員打個照面，對接所有事宜。

#### OPass 串接頁面
下列前三個是一個去頭去尾的特殊頁面，整合在 OPass 的側邊攔 (功能列表) 之中的。
* [贊助商](https://tw.pycon.org/2020/ccip/sponsors/)
* [工作人員列表](https://tw.pycon.org/2020/ccip/staff/)
* [場地圖](https://tw.pycon.org/2020/static/pycontw-2020/assets/venue.png)
* [議程 API](https://tw.pycon.org/2020/ccip/)

### 主議程表
議程表不太可能在 Talk Announcement 的時候可以同時出來，原因是 Talk 被接受是一回事，但講者有可能會有變動，但最重要的是時間點還沒有安排。

當時間點安排好了過後，就可以準備根據議程組先行列的議程表來產出該頁面。通常議程表的頁面會是一個工程浩大的事情，因此通常的作法是會先擺一個 temp 的連結指向某個公開的 Google Spreadsheet。等到 Final 網頁版製作好之後，再變成這個最終的版本。

###### tags: `organize` `dev`