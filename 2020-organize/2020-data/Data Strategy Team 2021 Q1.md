---
tags: 2021-organize, 2020-organize, 2020-data, data team, data strategy, data-team, meeting minutes
---

Data Strategy Team 2021 Q1
===

願景：前三個月 infra 後九個月做 growth
* Airflow (沒權限請找 @davidtnfsh ):
    * UI: http://airflow.pycon.tw/admin/
    * Repo: [PyConTW ETL](https://github.com/pycontw/PyCon-ETL)
* Trello: https://trello.com/b/Rxtrpqxi/data-squad (沒權限請找 @clleew XD)
    * @davidtnfsh 你應該也可以加xD


[TOC]

## Infra 架構(TBD)

![img](https://i.imgur.com/x5Hhrfl.png)
## OKR 四象限

| 目標 | OKR 當前狀況 |
| -------- | -------- |
| 有個完整的 Infra 可以取用資料，不會有 garbage data |架好 great expectations (data cleaning tool)，套用到 big query 上會新增資料的 table `zzz%`
| |確保 Facebook Data 的 accessibility `zzz%`
| |確保 GA 的 accessibility  `zzz%`
| |至少一個 function 的人能把資料存進 Warehouse `zzz%`
| 有好的團隊氛圍 |2週一次分享會 `100%`
|  |每季跟每個人做一次 1-on-1 `100%`


### 例行進度回報（範本）
1. [name=David Jr.]
    * 這兩週： 
    * 未來兩週：
    * Blocker：
3. [name=Lee Wei]
    * 這兩週：
7. [name=Grimmer]
    * 這兩週：
    * 未來兩週：
    * Blocker：
9. [name=Tai]
    * 這兩週:
    * 未來兩週:
    * Blocker:
9. [name=Max]
    * 這兩週：
    * 未來兩週：
    * Blocker：
9. [name=Hane]
    * 這兩週：
    * 未來兩週：
    * Blocker：
9. [name=睿祥]
    * 這兩週：
    * 未來兩週：
    * Blocker：
10. [name=Jacker]
    * 這兩週：
    * 未來兩週：
    * Blocker：
10. [name=Howard]
    * 這兩週：
    * 未來兩週：
    * Blocker：

## 會議記錄 20210303

:::info
- **簡報網址:** [A Brief History of Containers
](https://docs.google.com/presentation/d/1mumsPkUkGYT83Am8qA99Uie_KTELCKYk5eidZPuvwP8/edit?usp=sharing)
- **講者:** David Jr.
:::


### 分享共筆
- [name=tai] 剛好看到幾個相關的
    - docker CTO Justin Cormack 投 kubeconf 被拒絕生氣氣 https://twitter.com/justincormack/status/1366780253180489733
    - 50 Reasons Kubernetes Sucks
 https://www.teamblind.com/post/50-Reasons-Kubernetes-Sucks-S77O8VZ8

1. [name=David Jr.]
    * 這兩週： 
        * 投影片
        * 跟 Howard, 睿祥 1-on-1，確定了 Howard 對 SQL, BI 算有興趣；睿祥對 data pipeline, ETL 有興趣
        * 完成 BigQuery 的新手教學：https://trello.com/c/hjLttNN5/27-%E3%80%8Cbigquery-%E6%96%B0%E6%89%8B%E8%AB%8B%E7%9C%8B%E9%80%99%EF%BC%81%E3%80%8D
    * 未來兩週：
        * 持續約 1-on-1 了解大家的興趣
        * 嘗試把 GA 串起來
        * 嘗試把完成一張 dashboard 的需求給新進組員看，新人可以依樣畫葫蘆~
    * Blocker：Airflow 的 SSL 還在請
3. [name=Lee Wei]
    * 這兩週：
7. [name=Grimmer]
    * 這兩週：
    * 未來兩週：
    * Blocker：
9. [name=Tai]
    * 這兩週:
        * 東看西看，像是評估 Great Expectations https://greatexpectations.io/
        * 被工作吃掉了 qq
    * 未來兩週: (同上次）給 rg-cli 加新功能去讀 bigquery 中會眾資料來 render 結案報告
    * Blocker: no (一天只有 24hr qq)  (荷蘭要宵禁了 qq)
9. [name=Max]
    * 這兩週：
    * 未來兩週：
    * Blocker：
9. [name=Hane]
    * 這兩週：
    * 未來兩週：
    * Blocker：
9. [name=睿祥]
    * 這兩週：終於把拖稿的補上了XD
    * 未來兩週：
    * Blocker：
10. [name=Jacker]
    * 這兩週：
    * 未來兩週：
    * Blocker：
10. [name=Howard]
    * 這兩週：
    * 未來兩週：
    * Blocker：

## 會議記錄 20210217

:::info
- **簡報網址:** [https://docs.google.com/presentation/d/11BQcWR1WCSpTF5mQfTyOe2NydKMRPQisW3KEFLBjM4I/edit?usp=sharing](https://docs.google.com/presentation/d/11BQcWR1WCSpTF5mQfTyOe2NydKMRPQisW3KEFLBjM4I/edit?usp=sharing)
- **講者:** Juihsiang
:::

1. [name=David Jr.]
    * 這兩週： 
        * Airflow 的 Google OAuth
        * 整合 Github webhook 到 channel
        * 新增每週 sync 前的 hackmd reminder
        * 跟新朋友約 1-on-1 了解一下大家的興趣和目標
    * 未來兩週：
        * 跟 grimmer, 傑奇、howard、睿祥 約 1-on-1
    * Blocker：
3. [name=Lee Wei]
    * 這兩週：
        * review David's pull request
        * join Tai's github discussion
    * 未來兩週：
        * do we want to upgrade airflow to 2.0? if no one aginst this idea, I'd like to try.
    * Blocker：
        * None
9. [name=Tai]
    * 這兩週：
        * 繼續 [post-event airflow DAG](https://trello.com/c/yRGq1sZ3/11-kktix-%E7%9A%84%E8%B3%87%E6%96%99%EF%BC%8C%E7%94%A8-airflow-%E5%AF%A6%E4%BD%9C-etl-%E4%B8%A6%E5%AD%98%E9%80%B2-bigquery)
            * 評估了拉資料的方式, [see github discussion](https://github.com/pycontw/PyCon-ETL/discussions/17)
        * [team working flow 整合中 (git, github, gitlab flow)](https://github.com/pycontw/PyCon-ETL/discussions/15)
    * 未來兩週：
        * 繼續 post-event airflow DAG
            * 根據 github discussion, 會去改 post-event-generator
        * 評估 Great Expectations https://greatexpectations.io/
    * Blocker：
        * 對 ETL 的 working idiom 實在太不熟悉啦啊啊啊

## 會議記錄 Template

:::info
- **簡報網址:** 
- **講者:** 
:::

1. [name=David Jr.]
    * 這兩週： 
    * 未來兩週：
    * Blocker：
3. [name=Lee Wei]
    * 這兩週：
    * 未來兩週：
    * Blocker：
7. [name=Grimmer]
    * 這兩週：
    * 未來兩週：
    * Blocker：
9. [name=Tai]
    * 這兩週：
    * 未來兩週：
    * Blocker:
9. [name=Max]
    * 這兩週：
    * 未來兩週：
    * Blocker：
9. [name=Hane]
    * 這兩週：
    * 未來兩週：
    * Blocker：
9. [name=睿祥]
    * 這兩週：
    * 未來兩週：
    * Blocker：
10. [name=Jacker]
    * 這兩週：
    * 未來兩週：
    * Blocker：
10. [name=Howard]
    * 這兩週：
    * 未來兩週：
    * Blocker：

## 會議記錄 210120

:::info
- **簡報網址:** 
- **講者:** Hane
:::

- 今日出席
    - new buddy: 睿祥  Grimmer 瑋明 Howard
    - DavidJr tai Gobby Hane wei stacy
- self introduction
    - grimmer: 名稱來自動畫 (https://zh.wikipedia.org/zh-tw/MONSTER_(%E6%BC%AB%E7%95%AB))，叫 grimmer 或本名康登傑都可以，是 tai lab 學長 （什麼都會）
    - 睿祥: 目前主要做圖像類的Deep learning相關，想了解數據類相關的pipeline或者相關應用。
    - 瑋明 (Jacker): wei 系上學長, 去年有幫忙場務，今年想看看別的
    - Gobby: 在「光和感知」上班，剛來台北半年。暫時沒在寫 code ~~~
    - howard: 去年也幫場務，在台南當工程師做 layer2 switch
    - stacy: SEO 廣告相關公司從業人員
    - tai: 多年志工   來 data 完成「幫 pycontw 量化各種指標」的遺願
    - hane: 資料工程師 莫名身兼 PM 中
    - lee wei: 總召 + 資料工程師，有看懂千年女優
    - david: 前 dcard data engineer，是個一直在做 ETL 清資料的清潔工
- 組長 announcement
    - 根據上一季 OKR 討論結果，這季 bi-weekly 重點改成分享 + social, 線下再做專案
- hane 分享對話機器人
- among us https://play.google.com/store/apps/details?id=com.innersloth.spacemafia&hl=en&gl=US


9. [name=Max] 病假



## Hane's Sharing
key words: Dialogflow (company provides API) includes Agent (to bubild intent)

dialogflow.cloud.google.com

## OKR Template

1. 建立願景:
    1. 你現在為什麼想參加 PyCon TW 社群？
        1. david: 想社交；也想學 PM 的技巧
        3. Hane: 習慣（？ 想社交，覺得聽大家的經驗分享很有趣
        4. Max: 社交，寫扣
        5. Wei: 遠端工作者需要社交 😆 技術能力不夠 😢 想點一點溝通技能，斜槓一下比較不會被淘汰 😱
        6. tai: 持續增加知識廣度、和人協作寫 code 很有趣(找人一起寫 code)
    3. 你現在大可以參加其他 team，為什麼是 Data Team？
        1. david: 因為本身就是 data engineer，this is my area of expertise
        3. Hane: 感覺可以學到很多沒有接觸過的事物
        4. Max: 學習利用 Data 發揮價值，和接觸平常更多與 Data 相關的事物
        5. Wei: 因為正職是 machine learning engineer ，想來觀摩大大們怎麼做事（但其實我也在其他 team 啦xD）
        6. tai: 想了解相關的專業知識、剛好自己公司也用得到
    5. 你現在希望這個 team 為 PyCon TW 社群做出怎樣的貢獻？
        1. david: 希望讓 PyCon 做到 data-driven
        3. Hane: 讓大家都能方便地找到需要的資訊
        4. Max: 希望利用 Data 讓 PyCon 變得更好
        5. Wei: 減少組長決策壓力
        6. tai: 在數位世界音量夠大、減少決策壓力
    7. 如果現在 Data Team 不存在了，對 PyCon TW 社群有什麼損失？
        1. david: 決策只能拍腦袋，不能用 data 作輔助
        3. Hane: 無法透過過往資訊調整未來方向
        4. Max: 將沒有 Data 可以參考
        5. Wei: 組長決策壓力++ 😢 找未來的組長難度++ 😱
        6. tai: 同上；而且我們會跟其他 PyCon XX 一樣
2. Giving Feedback: 實名制，用下列格式跟 teammate 說，you should start, stop or continue doing something~
    
    1. Stop
        1. david: 開會才寫要講的內容~
        3. Hane: 有時候會議時間比較長，可能要控制一下時間（？
        4. Max: 六頂思考帽好長
        5. Wei: 花過多的時間取得或無法取得共識 -> Possible Solution: 先提出 good enough solution 沒反對就可執行
        6. tai: 同上所有人 XD
    2. Start
        1. david: 開會前先把上週進度填完~
        3. Hane: 多花點時間學習&嘗試大家分享的技術
        4. Max: 更多交流，和互相學習，提升開會效率，像是簡化版思考帽 (?)
            1. define 怎樣的問題是用六頂思考帽: xxx
            2. 待 Max proposal
            3. 預先思考，開會就直接做決策
            4. 開會前十分鐘想好發言內容
        6. Wei: 用 reminder bot 提醒大家先填進度（like tag data team at 9:00 p.m.）、用 Project Management tool (like trello) 讓該做的事被明確的追蹤
        7. tai: 大家多送 PR 啦; 或許可以來小專案 sprint
    3. Continue
        1. david: 繼續雙週會跟 OKR 的實體聚~
        2. Hane: 雙週會 & OKR
        3. Max: 更多交流活動，分享會
        4. Wei: 雙週會跟 OKR 頻率kkk、嘗試新工具
        5. tai: 同上所有人 XD
4. OKR:
    1. 回顧上次的 OKR (use stop, start, continue to optimize our OKR)
    2. 訂這次的 OKR:
        1. 先頭腦風暴（自下而上）
            1. David:
                * 讓大家都能開心的 data team 當志工：Q1 使用 CFR + OKR
                * 引入好的 PM 流程：學會 RICE + scrum
                * 打造團隊透明的文化：一季完成一次 1-on-1
            2. Hane: 
                * 學習用 Airflow 定期抓資料
            3. Max: 
                * 督促分享會進行 (確認講者、主題、時間)
            5. Wei:
                * 用 great expectations 減少 garbage data (e.g., proposal submission date < 2000-01-01)
                * seo data / fan page message 收進來 -> generalize to fit other purpose (e.g., office site) -> help other team to leverage data infra
            6. tai: data warehouse 和 growth 都想做
                * 實做與維護一到兩個 airflow dag
                * 參與實做與維護 GTM and GA tag，最好是能夠直接操作 GTM/GA dashboard 後直接給 web squad 送 PR 來落實這件事情。  
        2. 決定完團隊的 OKR 後再細分到個人（自上而下）
            1. Object: 有個完整的 Infra 可以取用資料，不會有 garbage data
                1. Key Result: 架好 great expectations，套用到 big query 上會新增資料的 table
                2. Key Result: 確保 Facebook Data 的 accessibility
                3. Key Result: 確保 GA (google analytics) 的 accessibility 
                4. Key Result: 至少一個 function 的人能把資料存進 Warehouse
            3. 有好的團隊氛圍
                1. Key Result: 2週一次分享會
                2. Key Result: 每季跟每個人做一次 1-on-1
                3. Key Result: 把所有的任務搬到 Trello 上
4. Action Item:
    1. Facebook 資料串接的 Survey @hane1818 
    2. GA 的資料串接 @MaxWu 
    3. 研究一下 Web Event Tracking 的串接工具: FullStory @MaxWu 
    4. 規劃一下 Infra 的 roadmap @davidtnfsh 
    5. 把這些工作搬到 trello 上

## 1-on-1 固定問題

1. 你對這一季 data team 的規劃有什麼想法或問題？ https://hackmd.io/LLcaglX0Szed-AsHUdC3bg#OKR-Template
2. 你現在為什麼想參加 PyCon TW 社群？
3. 你現在大可以參加其他 team，為什麼是 Data Team？
4. 你現在希望這個 team 為 PyCon TW 社群做出怎樣的貢獻？
5. 如果現在 Data Team 不存在了，對 PyCon TW 社群有什麼損失？
