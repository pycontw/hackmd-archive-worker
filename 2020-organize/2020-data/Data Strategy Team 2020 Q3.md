---
tags: 2021-organize, 2020-organize, 2020-data, data team, data strategy, data-team, meeting minutes
---

Data Strategy Team 2020 Q3
===

==願景：幫 PyCon TW 做到 data strategy driven==
* Airflow (沒權限請找 @davidtnfsh ):
    * UI: 
    * Repo: [PyConTW ETL](https://github.com/pycontw/PyCon-ETL)

[TOC]


## OKR 四象限

| 這兩週關注的任務 | OKR 當前狀況 |
| -------- | -------- |
| xxx      | 目標：優化問卷，收到更優質的資料且自動化產出報表
| xxx      | Key Result: 11/5 前可以看到結案報告 @davidtnfsh `65%` |
| xxx      | Key Result: 確保資料權限的控管 @davidtnfsh `90%` |
| xxx      | Key Result: 確定想透過問卷知道的會眾資訊 @RainWu `110%` |
| xxx      | Key Result: 確定想透過問卷知道的贊助商資訊 @tinachuchu  `90%` |
| xxx      | Key Result: 簡單視覺化 @tinachuchu `50%`
| 徵才牆實做與初步 SEO      | Key Result: 徵才牆 @tai271828 stacy `100%`


## 許願牆

1. Tom: like 今年進了多少 commit, 多少 line changes... 分布在多少不同的人身上... 大家怎麼 contribute 到這個 conference 的? 發 Issue/PR
    * <https://developer.github.com/v3/repos/statistics/#get-all-contributor-commit-activity>
    * `curl -u "<username>" https://api.github.com/repos/pycontw/Pycon-ETL/stats/commit_activity`
2. Wei: 每個 Media Post 為我們期望的效益（e.g., 購票數、投稿數）帶來多少影響

## 10/18 Agenda

> 提醒我要拍照
> 體醒我跟大家說我們準備辦 team building -> 生存遊戲
> 提醒你要打統編

> 生存遊戲訂位 11/7
> Hack切季


<http://www.lazertreks.com/zh/>

1. 建立願景:
    1. 你為什麼想參加 PyCon TW 社群？
        * 泰瑋：因為我只會寫 Python
        * Max：想對 Python 研究更深，與認識寫 Python 的朋友 
        * Stacy：因為臉書回覆的人很兇(據說是泰祥)...會想知道SEO對於一個程式組織帶來甚麼效益
        * Hane：因為想了解更多 Python 相關技術
        * [name=tai] 大家一起寫 code 很好玩r，而且想跟更多高手一起寫 code + 累積工作上缺乏的軟技能面向
    3. 你大可以參加其他 team，為什麼是 Data Team？
        * 泰瑋：因為本業是 Data Engineer
        * Max：對 Data 有興趣，也剛好工作與 Data 相關
        * Stacy：希望可以學習運用Data，剛好之前也是處理數據的科系，私心也希望能練習python(?)
        * Hane：希望可以透過 Data 運用幫助志工及會眾們更熟悉 PyCon TW
        * [name=tai] hmmm 我參加很多 team XD data team 只是我 deliver product 必須要有的一個元素
    5. 你希望這個 team 為 PyCon TW 社群做出怎樣的貢獻？
        * 泰瑋：希望可以幫 PyCon 做到 Data Strategy Driver
        * Max：為 PyCon 找出更多的數據洞察來幫助決策
        * Stacy：找到python的同溫層(為明年賣票更順利)、為組織增加跟贊助商的籌碼
        * Hane：讓更多人熟悉&願意參加 PyCon TW 和推廣 Python
        * [name=tai] 讓中階開發者變成 senior python developer 然後跟我一起寫 code XD 讓已經是 senior python developer 的人能夠樂在其中地滋養回饋 python 社群（我沒有想要為 junior developer 服務，但為了達成我的目標還是要不斷補充 junior XD Orz)
   5. 如果 Data Team 不存在了，對 PyCon TW 社群有什麼損失？
       * 泰瑋：沒有 data team，可能會缺少某些數據，做決策決策只能拍腦袋，不科學而且未必能說服人。
       * Max：沒辦法提供更完整的數據
       * Stacy：Data Team可能相對其他Team更了解Data來源和組成，可以更快速產出組織需要的資訊
       * Hane：沒辦法運用過往的經驗來輔助&改善之後PyCon TW的活動進行以及符合會眾的期待
       * [name=tai] 變成唬爛團隊，不夠專業。2022 的 PyCon US 聽不到泰瑋 present
2. 定義關鍵要務：
    * 頭腦風暴：任何點子都可以提，這階段不允許批評 
        1. GTM Tracking (2021 Q1)
        2. 辦 Airflow Tutorial 
        3. Chatbot: 先分析會眾的問題類型，建立一FAQ chatbot 輔助會眾快速得到解答 (2020 Q4 先分析熱門問題)
        4. Pycon官網SEO體質調整：TDK、canonical、社群tag..等等
        5. 凝聚組內向心力：狼人殺、LARP、生存遊戲..等(不要恐怖的，拜託..)
        6. Pycon Blog：希望大家多看這個部落格上面的資訊(要問泰祥) (2021 Q1)

    * 把點子整理成 OKR：**2020 Q4 OKR**
        * O：不允許有數字，讓人看了有激情想去完成
            1. 讓大家都掌握 ETL 的技能
            2. Pycon官網體質調整
            3. 讓團隊成員共熟氣氛更融洽
            4. 熱門問題分析
        * KR：初始狀態有 50% 的信心能完成
            1. 辦一場 Airflow Tutorial + 組內每個人都能實作出一個 Airflow 的 Dag
            2. Q4先把整個網站架構拉出來(url的層級、Title、Description、H1)
            3. 辦一場 team building
            4. 分析 FB 上常被詢問的問題類型，預期建立20題常見問題知識庫

4. 給予反饋，接受反饋:
    * review 每個人 S3 的 OKR
    * 對於目前整個 team 的風氣、方向等等，大家有什麼想法嗎？

> 以上流程參考至這本 「哈佛商學院最受歡迎的領導課」
> https://www.books.com.tw/products/CN10973921

- [name=tai] 無法實體參與先留 comments
    - [Question] 建立願景的部份我還要講一次嗎？XD 要的話我再發在 data team channel
    - 關鍵要務
        - team: 坐等大家和 team lead 決定的方向，我 support \o/
        - 個人: 基於 airflow 在其上蓋一個報表服務提供一個不限組別的決策（非常有可能就是實做結案報告的 csv parser 改成也支援 bigquery)
    - 反饋
        - S3 review （自我 review）
            - 完成度 100%，但還沒認真評估過效果。
            - 和 Stacy 請教的過程知道很多有趣知識，合作過程中有給我很多成就感。
            - 結案報告動工有點拖到約兩週
        - team 風氣
            - 跨領域交流好玩
            - 每次的小分享好玩，請繼續維持
            - 期待組員實做與展示小成果的頻率可以更高些

- [name=Wei] 正在花蓮，用文字xD
    - 想問 team building 可能辦在 11月下旬嗎？原因是之前跟泰瑋提過的想跟 11月的 pre kickoff meeting 辦在一起，希望讓更多的志工加入。因為十月底才剛開一次，十一月初要馬上再開應該有點太快xD
    - 願景
        - 用數據降低組長決策壓力
        - 評估決策對大會帶來影響效應
    - 關鍵要務
        - 個人： 將各組的需求媒合到 data team
    - 反饋
        - S3
            - 協助找到博安老師給 airflow tutorial
            - 我沒特別訂目標xD 主要以我知道的項目（e.g., rg-cli)的協助為主


## 10/14 會議記錄

:::info
- **簡報網址:** 
- **Medium Articles:**
- **講者:** Tai
- **出席:** davidJr max wei rain tai hane
:::

1. [name=David Jr.]
    * 這兩週： 
        1. 找到 Airflow 講者 (Frank)
        2. 根據上次 data policy 的結論，生一版使用者條款
    * 未來兩週：
        1. 繼續使用者條款
        2. 跟 Frank 講者討論一下 Airflow tutorial 的投影片
    * 需要討論：
        * 10/18 是 OKR 討論會，歡迎大家來吃吃喝喝聊天喔
3. [name=Lee Wei]
    * 這兩週： 沒人問我 report-cli xD
    * 未來兩週：
    * 需要討論：
5. [name=Rain]
    * 這兩週： None
    * 未來兩週： TBD
    * 需要討論： None
7. [name=Stacy]
    * 這兩週：
    * 未來兩週：
    * 需要討論：
9. [name=Tai]
    * 這兩週：
        * 解除 self-quarantine ，繼續跑有的沒的手續 Orz
        * Follow up talk videos of PyCon TW 2020
            * 參考過往的瀏覽狀況來決定 logo 要放哪
            * 但是最後放到影片最後面惹 q
            * 對這議題有興趣的人可以來找我
    * 未來兩週：初步的報表 from https://github.com/pycontw/pycontw-postevent-report-generator
    * 需要討論：
        * 想知道 blog 現在是不是在 pending 內容？？有初步的 monitor 結果ㄇ


## 9/30 會議記錄

:::info
- **簡報網址:** https://hackmd.io/iZOKJkK_SQS_neVtlJCXbQ?view 
- **Medium Articles:**
    - [Part 1](https://medium.com/random-life-journal/link-the-attendees-and-the-decision-makers-pycon-tw-part-i-37940e730229?source=friends_link&sk=37074ce58e35d5dd0fb65954114af63e)
    - [Part 2](https://medium.com/random-life-journal/link-the-attendees-and-the-decision-makers-via-a-questionnaire-pycon-tw-part-ii-26233c1b80e5?source=friends_link&sk=8eee4a96f7a0d51baf45a3241ee49d16)
- **講者:** Rain
- **出席:** davidJr max josix yider wei rain tai (hane 中間加入)
:::

1. [name=David Jr.]
    * 這兩週： 
        1. 自架的 Airflow 上線了 http://airflow.pycon.tw/admin/
            * Pricing: server + ip = 393 + 86 = 479 NTD/month
            * 感謝 YYC 協助
            > cert 的方式最後是用 ...? ----> in progress
            > 上次七萬帳單有下文嗎？ -------> 是台幣
        2. 問卷的資料上 BigQuery 了
            * Bootcamp: https://github.com/pycontw/PyCon-Data-Strategy-Team-Bootcamp
            ![dd](https://github.com/pycontw/PyCon-Data-Strategy-Team-Bootcamp/raw/master/pictures/bigquery_demo.png)
                * 有興趣的 josix max tai ...
        3. 未來的兩次活動：
            1. Data Policy 會議：10/4  21:00~22:00 https://hackmd.io/xp8vq_LdR4WKAukQPZLtGw?edit
            2. Data Team S3 OKR Review ：舒服生活 Truffles Living 10/18 12:00~14:00
    * 未來兩週：
        1. 了解一下 https://github.com/pycontw/pycontw-postevent-report-generator
        2. 調查大家對於 BigQuery / Airflow or 其他的興趣，想安排個 tutorial（可能會找其他大大來講，找不到小弟再來獻醜）
    * 需要討論：
3. [name=Lee Wei]
    * 這兩週：
    * 未來兩週：
        * 協助夥伴了解 https://github.com/pycontw/pycontw-postevent-report-generator
        * 向 David Jr. 大大學習 BigQuery / Airflow
    * 需要討論：
        * airflow 的 admin 現在是對所有人開啟嗎？
        * 參與討論：david30907d, leewei
5. [name=Rain]
    * 這兩週：None
    * 未來兩週：TBD
    * 需要討論：None
    > 上次的報告有要繼續 present 嗎~? yes, doing this time
7. [name=Stacy]
    * 這兩週：
    * 未來兩週：
    * 需要討論：
9. [name=Tai]
    * 這兩週： 搬家 + 調時差 + 有的沒的行政手續...self-qurantine ing...
    * 未來兩週： 初步的報表 from https://github.com/pycontw/pycontw-postevent-report-generator
    * 需要討論：
        * 看有啥可以加到結案報告盡量整合看看
            * rain (會後問卷圖表)
            * wei (議程資料 ...與 code 實做)
        * blog SEO 要怎麼進行（主要是文案）、協調者？
            * 協調
                * stacy 的意見
                * 找人生 blog 內容，此內容與 stacy 意見盡量一致
                * 最後收 data

## 9/16 會議記錄

:::info
- **簡報網址:** xxx
- **講者:** Rain
:::

1. [name=David Jr.]
    1. Airflow 超貴，目前有兩個解法：
        1. f1-micro: 138 NTD / month
        2. cloud function + cloud scheduler: 3 NTD / month * job 數量
        > lesson learned: 不管如何，使用新服務前務必提早定期不定期先看看帳單，免得遇到爆表悲劇
    2. Opass 的資料在這邊，大家應該有 Query 權限了 [Bigquery](https://console.cloud.google.com/bigquery?project=pycontw-225217&authuser=0&p=pycontw-225217&d=ods&page=dataset)
        - demo: ods --> ods pass
            - [takeaways] 大家要看到一樣的畫面
            - [takeaways] 要刪掉 user_id
            - tips
                - press preview is free until pressing query
    3. 盤點一下目前的帳號跟 Data Team 的服務：
        1. GA, GTM, GCP 的各種服務:
            1. GCP：GCP 的服務大家都可以用各自的 email 登入，權限已經開給各位了，沒權限代表我弄錯了請來找小弟
            2. GA, GTM：用 data-strategy@pycon.tw 會是 admin，然後資料會串回 BigQuery，大家拿 BigQuery 權限即可
        2. Email: data-strategy@pycon.tw 這組有所有 data team 使用的服務的 admin (PS data-strategy@pycon.tw 是 mail group ...我懷疑其實不能用在 GA/GTM )
        3. Blogger 權限: 問公關組
    4. Tom 對 Query 需求的 feedback：上次說先開權限給 dev team 的 leader 去 Query 他沒啥問題，我們要準備一下 Bigquery 的 Bootcamp，告知怎樣下 Query 比較便宜即可；如果成效不錯 phase2 可以考慮把 bootcamp 開放給全部志工參加，過了就可以自由 Query 了~
    5. $$$$$$$$$$$$$  /o\ 
3. [name=Lee Wei]
    * 2021 大會籌備會希望在 Discord 上，如果不介意的話可以慢慢轉換～
        * https://discordapp.com/channels/752904426057892052
        * https://discord.gg/HmxGUE4  <- 或者也可以用這個
    * 我在這份文件加了 tag `2021-organize`
    * airflow 是不是要炸預算了 😱
5. [name=Rain]
    - dump 資料，備份並上傳 GCP
7. [name=Stacy]
    * blog 串接解決
    * data studio多種資料來源障礙
        * 再和Max討論
    * 是否需要盤點目前所有帳號的admin跟使用人員？
        * 泰祥再盤 2021前XD
    * 大會後，SEO還能為pycon做什麼？pycon想要什麼？
        * 短期回答：拉贊助
        * 把pycon做宣傳的平台
        * 想要知道會眾的樣貌
        * 很早就會開始賣票，是否能早點傳遞
        * 議程主題在google search 時可以爭取排名
        >Stacy 下次會議提出
8. [name=Tina]
9. [name=Tai]
    * 清點醞釀結案報告要用的材料中
        * 今年好像忘了在官網收 sponsor logo clicks..??
        * max 說可以幫忙 2021 landing page logo
        * 2020 應該是沒有 landing page logo click data qq
            * 開權限給 max
    * 已上傳 opaas booth data to GCS (google cloud storage)

## 9/2 會議記錄

:::info
- **簡報網址:** https://drive.google.com/file/d/1ZqkLu4fF79tQHvU0p7eFCaF-qIr4_6st/view?usp=sharing
- **講者:** Stacy
:::


1. [name=David Jr.]
    * 用 GCP cloud composer 架 Airflow
        * repo: https://github.com/pycontw/Pycon-ETL
        * Airflow UI: https://xe29c3578f60597c3p-tp.appspot.com/admin/
        * Airflow 教學：https://cloud.google.com/composer/docs/how-to/using/managing-dags
    * 詢問一下 Tom 對權限控管的想法，等他大會忙完XD
2. [name=Lee Wei]
3. [name=Rain]
    - [現階段問卷連結](https://www.surveycake.com/s/z84l2)
    ![](https://i.imgur.com/knc2had.png)
    - 再訪談議程組、主席
    - 從訪談內容擷取 metrics
    - 產出第一、二版問卷並找一些人試寫
    - 規劃問卷投放管道、聯繫各社群軌負責人協助發放問卷
    - [價值主張及指標建立的想法](https://medium.com/random-life-journal/link-the-attendees-and-the-decision-makers-pycon-tw-part-i-37940e730229?source=friends_link&sk=37074ce58e35d5dd0fb65954114af63e)
5. [name=Stacy]
    - 已完成徵才牆TDK撰寫
    - Data Studio還在努力研究中(公司練習中)
    - 部落格需要Google Tag Manager容器的權限 ( action: [name=tai])
6. [name=Tina]
    * 想問問題：你有哪部分想多了解的嗎？ 我整理完會議記錄再跟你說～
        * 好呀感謝你！如果有大家對以前問卷的一些建議或覺得這次可以新增的問題或許會不錯：）
        * 以前的問券在哪 ( [name=tai])
        * 問卷：https://www.surveycake.com/s/4wLv9

8. [name=Tai]
    * 已經完成和額外打算 https://hackmd.io/ZtlNsGThQS-zIKThptBG0A?both


## 8/19 會議記錄

:::info
- **Location:** 線上
- **Date:** 8/19
- **Agenda**
    - 讀書會分享（10m）：「大數據之路：阿里巴巴大數據實戰」 讀書心得
        - [投影片](https://www.slideshare.net/ssuserc3bde0/ss-238054233)
        - [medium 版](https://medium.com/@davidtnfsh/%E5%A4%A7%E6%95%B0%E6%8D%AE%E4%B9%8B%E8%B7%AF-%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4%E5%A4%A7%E6%95%B0%E6%8D%AE%E5%AE%9E%E8%B7%B5-%E8%AE%80%E6%9B%B8%E5%BF%83%E5%BE%97-54e795c2b8c)
    - 一起更新 OKR（15m）
    - 臨時動議 + 確定下次讀書會分享人選（5m）
- **Participants:**
:::


1. 泰瑋:
    - 確保資料權限的控管: [data studio 權限控管](https://www.youtube.com/watch?time_continue=178&v=tiT8MK95-9I&feature=emb_logo) 以下先假設我們要用 bigquery 存資料
        1. 開放部分的 bigquery table 給大家自己 query
        2. 不開放 bigquery 權限給大家，統一由 data team 寫完呈現在 data studio 上給大家看
        3. 通過獵人試煉的人可以獲得 bigquery 權限自己寫 query，其他人可以用 data studio 看

2. Rain:
    - 價值主張到 key metrix:
        - 設計一些引導表達對於品牌價值主張及未來願景的問題
        - 訪談設計組及開發組長，整理訪談內容

3. [name=tai]
    - 徵才牆尚未實做（在忙幫 PyCon TW 找錢），歡迎有興趣的人直接幫做這個靜態網頁。
    - loop-in stacy 給他 google search console 權限
        - 我補一個徵才牆進度：    我找了 James 讓他給 stacy 足夠的權限玩這些東西；@stacy 請問你今天展示的這些東西是上次給了權限你就弄得到了對不對？
        - James = jneo = 18/19 網站組組長
        - stacy: blog 也很適合研究，希望可以取得足夠權限
        - tai question:  我可以怎麼協助你取得權限？

臨時動議：

* Lee Wei: HackMD 的權限管理
    * 順便分享其他 PyCon 的會後問卷供參考
        * [PyCon US 2020](https://www.surveymonkey.com/r/LS3PVB6)
        * [PyCon CA 2019](https://docs.google.com/forms/d/e/1FAIpQLSeYLK3LvXupvCj5bjl89IhM7rbECBK4lPEhgF_QNgQFmQ1DUA/viewform)
        * [EuroPython 2020](https://docs.google.com/forms/d/e/1FAIpQLSex13c2NSp65eMc_XnVnY0X_gK5P7pbiFab3EXxrIJ9te_SBw/viewform)
* 泰祥：
    這篇摘要一下我原本想分享的資訊好了

    臉書 post vs. 實際購買一般票人數變動，心得：

    - 我第一次在 PyCon TW 這麼認真推臉書 post，目前有超過四萬觸及的實力（持續增加中但我累了想停了 XD )
    - 標的群眾約 5000 (看到之後有 0.5% 會來買票)
    - 核心群眾則是 5000 中的 2500 人（符合轉換率 1% 的經驗法則）
    - 長尾效應非常明顯；過了這 5000 人後買票的速度就慢很多   a) 還要研究如何突破同溫層、而且觸及到有效的異溫層   b) 下臉書廣告和長尾趨勢有明確甜蜜點(觸及到一個信心區間內核心群眾數量的廣告費用），以後可以根據這個甜蜜點決定廣告費用   c) 售票尚未結束   往往最後會衝一波 last minute (可以根據 last minute 的比例決定是不要要販售「晚鳥票」；可以很晚買但超級貴 XDDD )


:::info
- **Location:** 咖啡工廠站前店 (100台北市中正區信陽街6號）
- **Date:** 8/9（日）11:30 
- **Agenda**
1. 目前 Data Mining 的成果 `25min` [name=Wu Rain]
1. 往年結案報告產生器與成果 `10min` [name=tai]
1. 討論 Data Strategy Team 的願景 `45min` [name=everyone]
1. 確定本次 Action Items 以及下次開會時間 `15min` [name=everyone]
- **Participants:**
    - 泰瑋
    - rain
    - tai
    - pin-chun
    - (4cat?)
    - wei lee
    - stacy
    - tina
    - 請大家幫忙填感謝XD
- **Contact:** 泰瑋 <davidtnfsh@gmail.com>
- **Host:** 泰瑋

:::

## 8/9 會議記錄

### :books: 目前 Data Mining 的成果
---
- https://github.com/RainrainWu/pycontw-analyzer

### :books: 往年結案報告與結案報告產生器
---
- 結案報告 https://drive.google.com/drive/u/2/folders/1V-mVvwfatR-roMml3D4dBpdgs5ujYMxV
    - source code https://github.com/pycontw/pycontw-postevent-report-generator

### :dart: 討論 Data Strategy Team 的願景
---
- 討論前希望大家先想一下：
    - 你為什麼想參加 Data Team？（Pycon 還有很多 Team 可以參加，Why Data Team?）
        - [name=Lee Wei] 幫助議程組做決策
        - [name=Stacy] 因為跟工作相關，所以想貢獻一發
        - [name=tai]: short term: 過去太多觀落陰的痛苦，long term: 希望還是有 development 的成份在
        - [name=Tina]: 之前都做到 deploy 的工作，所以想來碰一點 Data（想做「根據量化資料擬定策略」的事情）
        - [name=品淳]: 在盾心做 CV 的 data scientist，想了解其他類別的 Data 怎麼處理
        - [name=Rain]: 想協助泰祥把分析功能分離出來，想嘗試看看 Data Driven Strategy 的神話是不是真的
        - [name=泰瑋] 本業就是 data engineer 做廣告投放，想要累積更多不同的經驗；同時練習帶 team。
    - 你希望 1 年之後的 Data Team 是怎樣的團隊並且達成了怎樣的成就？
        - [name=Stacy] 徵才牆
        - [name=泰祥]: 大家樂在其中即可(能活下來就好 XDDD )
        - [name=tina] 想玩玩看
        - [name=品淳]: 有新進的贊助組員跟 data team 說「這些指標很有幫助」
        - [name=Rain] 釐清 PyCon Taiwan 的品牌價值主張，並投射出對應的 metrix
        - [name=泰瑋] 希望上面 demo 過的工具或是類似材料都可以整進 airflow 每次直接拉近 warehouse
    - 假如沒有 Data Team，你覺得對 Pycon 的影響是什麼？
        - [name=Lee Wei Stacy Tai] 議程組就只能觀落陰
        - [name=Tina] (想跳過這個問題？)
        - [name=Rain] 無法回答
        - [name=泰瑋] （對決策有幫助？）
> 以上問題出自「哈佛商學院最受歡迎的領導課」

共識

- Data strategy driven

- 六頂思考帽（決定 Data Team 的願景）
> 以上問題出自「斯坦福大學最受歡迎的創意課」

### :dart: 訂這一季的 OKR
---
- 決定 Data Team 這一季的 OKR
    - Objective: 優化問卷，收到更優質的資料且自動化產出報表
    - Key result:
        - 問卷 10/5 前可以看到結果 @davidtnfsh 
            - 跟 OPass 要資料，直接 dump DB
            - 直觀數字
                - 攤位觸及率
                    - ref 2019 booth data https://drive.google.com/file/d/1xwaVlRn9fydlL0mX4nOX52SGZFNdqGed/view?usp=sharing
            - 漂亮的視覺化
        - 確定想透過問卷知道的資訊 @RainWu 
            - 由品牌價值主張衍伸 key metrix
            - 由 key metrix 設計問券互動過程
        - 問卷 8/23 之前做完問卷
            - [EuroPython 2020 quetionary](https://docs.google.com/forms/d/e/1FAIpQLSex13c2NSp65eMc_XnVnY0X_gK5P7pbiFab3EXxrIJ9te_SBw/viewform)
        - 確保資料權限的控管 @davidtnfsh 
- 決定個人的 OKR
    - stacy, 泰祥: 徵才牆
        - Key result: TBD (泰瑋會去了解)
    - 品淳
        - Key result: TBD (泰瑋會去了解)
    - 泰祥:
        - 規劃問卷投放管道
            - key results: 問卷蒐集率略大於 33%
        - deliver the product and development is quaterly long active.
    - Rain:
        - 由 PyCon Taiwan 品牌價值主張衍伸 key metrix
            - key results: 收集各組想透過問卷找到的答案
        - 由 key metrix 設計問券互動過程
            - key results: 8/23 之前做完問卷
            - key results: 問卷蒐集率略大於 33%
    - 泰瑋:
        - 跟 OPass 要資料，直接 dump DB
            - key result: 這季結束前我們的 warehouse 有 Opass 全部的資料就算完成
        - 確保資料權限的控管
            - key result: 需要訂好每個 team 需要的權限
    - Tina:
        - 整理 for 贊助商的問卷
            - key result: 簡單視覺化


把 PSF 中台灣人的資料存下來

### :closed_book: 確定本次 Action Items 以及下次開會時間
---
- placeholder
[] doodle

### Action Items:
- [ ] placeholder
- [name=tai]
    - 找有權限的人把 stacy 加進 GTM group
    - 實做徵才牆網頁後傳給 stacy
    - stacy gmail (already in private)
- [name=Wei]
    - 跟 David 協調派人紀錄現場議程 popular 程度

### 目前蒐集到的點子
<!-- Other important details discussed during the meeting can be entered here. -->
- **議程表流量 dashboard**
- 爬 PyCon Tw slack 一年下來有多少訊息，看多少訊息可以成就一個 PyconTw
- KKTIX 會詢問是否願意提供 email 給贊助商和其他問題等等，不知道有沒有 API 可以拿資料回來
- squad 的名字是我亂想的，大家可以投票決定一個新的大家都喜歡的 XD [name=tai]
- stacey：產業類別

### Misc Info
- Pycon (X)  PyCon (X)  PyCon TW (O)
    - PyCon means PyCon US
    - PyCon is registered trademark owned by PSF
    - PyCon TW is a trademark authorized by PSF
    - Trademark info https://www.python.org/psf/trademarks/pycon/
        - Search for "PyCon TW"
        - More information https://www.python.org/psf/trademarks/
    - 更多「正確名稱」的寫法，可參考大會共筆 https://hackmd.io/HM5mHCFKQCu7-W5ea8ITcw?view
- Facebook Information Case Study
    - 一般票售票
        - 8/5
            - 當網路小白亂貼還是有點用；半小時內的觸及律就從原本 22xx —> 38xx    XDDDDDDD
            - 大會報告一下，小白亂貼文（其實只有發三個 group）成效，12 小時內:
                - post reached: 22xx —> 9.5k 
                - 多賣了 6 張票 xddd
                - 轉換率約千分之一
        - 8/6
            - within 36hr
            - post reached: 22xx —-> 12.6k
            - engagement: < 700 —> 968
            - sold tickets: 116 —> 127
        - 8/7
            - within 60 hr
            - post reached: 22xx —-> 13.2k
            - engagement: < 700 —> 1k/119
            - sold tickets: 116 —> 131
            - 開始進入 decay 長尾巴時期惹！
        - 8/9 (this morning)
            - organic/paid 14128/5330
            - engagement 1.4K/211
            - Ad since 8/8 $15.12 per day
                - more info https://www.facebook.com/pycontw/insights/?referrer=page_insights_tab_button
        - gut feeling
            - 原本就在 PyCon TW 內群組（臉書粉絲頁、mailing list ...etc.）的受眾已經飽和（會不會來心裡都想好了）

### Resource or 工商時間
- SEO 論壇 [name=stacy]
- hackmd 使用心得
    - 圖片 + running note (> 500 lines) + 5~6 people 會有明顯 lag



### Brainstroming

- 票券
    - 強制填公司名稱
        - 公司名稱
        - 學生
        - 不想提供
    - 強制填產業別（相對於公司名稱是比較友善的資訊）
- 議程資訊增加 "art"
- 投稿時間 demo
- 介紹 martin 給 rain 認識 [name=tai]
- 網站徵才牆 [name=stacy]
    - SEO 也可以做
    - 直接投廣告
- CfP 決策時間（到底什麼時候才要開始擔心真的沒人投稿）
    - 什麼時間用多少力道去提醒 submitter/reviewer
- 根據有限的 review number 去協助判定錄取與否的議程工作
- 頭腦風暴（每個人都提一個 Data Team 的願景）（也可以看下面的 # brainstorming)
    - 徵才牆
    - Data strategy driven




### Valuable Concepts 金句製造機

「SEO 就是在猜 Google 在想什麼」[name=stacy]
「Data 是連結工程與非工程人的橋樑」[name=tina]

### 活動照片

![](https://i.imgur.com/v6Pqzge.jpg)



### Reference
- [2019 會後問券結果 for 會眾](https://docs.google.com/spreadsheets/d/1KyWW28xRuiRK6gQaAYap7tIBTUFNB5pMCpmsdu092ec/edit#gid=0)
- [2019 會後問券結果 for 贊助商](https://docs.google.com/spreadsheets/d/18mlsZyArYCj9fuOsM766BPzcfxg9q3w-8Ix-hDKmVpg/edit#gid=616516674)


# Memo of Brain Storming Ideas

- [name=tai]
    - bit.ly 點擊整理
        - marr 有一個公用帳號 ... 至少到 2019 的票券資料在裡面
            - 個人票點擊在兩千出頭（完售，兩百多張票的樣子）
        - 2020 應該沒做這件事情?