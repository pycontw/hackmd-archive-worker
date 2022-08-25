---
tags: 2021-organize, 2021-web, web, dev team
---


# OPass Integration

## What's OPass?

以下引用自 [OPass 官方網站](https://opass.app/)：

> OPass 是整合活動資訊的解決方案，報到、活動時程、大會公告…等第一手資訊盡在 OPass！
> OPass 原本是是為了台灣開源資訊社群研討會所開發的報到 App，在 SITCON 學生計算機年會及 COSCUP 開源人年會已多次使用，為了各活動的使用需求便啟動了整合計畫，成為了 OPass 大平台來繼續提供給大家最好的報到體驗，並提供第一手的年會資訊。

## Integration



### 報到頁面

報到畫面要顯示什麼是由一份 config file 決定，每一年都會在 GitHub PyCon TW organization 底下新建一份 repo（可參考 [2020 版本](https://github.com/pycontw/PyConTW2020-CCIP-config)）並交給 OPass 團隊。

### 側邊欄

側邊欄的連結列表（如下圖）亦是由一份 config file 來決定，必須發 PR 到 OPass Portal （可參考 [2020 config](https://github.com/CCIP-App/Portal/pull/2)）並聯絡 OPass 團隊 review PR，若後續有需要改動也請聯絡 OPass 團隊。


<img src="https://i.imgur.com/ngqWS58.png" style="width:200px">

#### 快速通關

會眾報到用

#### 議程

PyCon 必須建立一個 endpoint 提供 json 格式的議程資訊，可參考 [2020 版本](https://tw.pycon.org/2020/ccip/)，但 2021 年官網上這部分仍在開發當中。

#### 大會公告

會期期間可以將想要佈達給會眾的資訊以推播通知形式傳送（提供訊息給 OPass 團隊操作）。

#### 大地遊戲 (WIP)

PyCon TW 會期期間都有個大地遊戲的活動，也就是各個贊助商會在現場擺攤，而會眾可以到各個攤位完成贊助商制定的任務(打卡、填寫問卷、或也可以是但純聊聊，這部分由贊助商決定)，通過後就可以用手機掃描攤位上的 QR code，完成夠多攤位就有資格參加抽獎 (獎品通常是天瓏提供的書)。

[CCIP-Puzzle-Chocolate](https://github.com/pycontw/CCIP-Puzzle-Chocolate) 是我們在 2020 使用的 大地遊戲 (forked project)。

部署方式待補。

#### 社群軌

2020 專屬活動，2021 已取消。

#### YouTube 直播

2021 版本開發中，請見 [Trello ticket](https://trello.com/c/vYNToMLT/50-revamp-ext2020-app)。

#### 健康聲明書 (WIP)

因應新冠肺炎疫情，OPass 團隊在 2020 年出了一個讓會眾簽署健康聲明的 app，我們同樣是 forked 了一份拿來跑 ([repo link](https://github.com/pycontw/CCIP-HDP))。

部署方式待補。

#### Discord

提供官網上引導會中加入 Python Taiwan Discord server 的頁面 ([2020 版本](https://tw.pycon.org/2020/zh-hant/ext/discord/))。

#### 會場 WiFi

會場 WiFi 帳號密碼

#### 會場地圖

會將會場地圖的圖片 checkin 到[這個 repo](https://github.com/pycontw/ccip-files) 並將網址填入這個 config。

#### 工作人員 & 贊助

官網上必須為工作人員列表和贊助商列表製作一頁沒有 header & footer 的頁面，方便在手機上呈現。 2021 網頁製作當中，可先參考 2020 版本：

- [staff](https://tw.pycon.org/2020/ccip/staff/)
- [sponsor](https://tw.pycon.org/2020/ccip/sponsors/)

## Plans in 2021


新冠肺炎在今年五月爆發，PyCon TW 籌備團隊目前仍無法確定大會會維持實體還是改為線上舉辦。若改為線上舉辦，網站組在 OPass 整合作法上勢必會針對使用者體驗來做調整，同時也必須和 OPass 團隊密切溝通確保 PyCon TW 的開發計畫是可行的。