---
tags: 2021-organize, 2020-organize, 2020-data, data team, data strategy, data-team, meeting minutes
---

Data Strategy Team 2020 Q4
===

==願景：幫 PyCon TW 做到 data strategy driven==
* Airflow (沒權限請找 @davidtnfsh ):
    * UI: http://airflow.pycon.tw/admin/
    * Repo: [PyConTW ETL](https://github.com/pycontw/PyCon-ETL)

[TOC]


## OKR 四象限

| 目標 | OKR 當前狀況 |
| -------- | -------- |
| 讓大家都掌握 ETL 的技能 @davidtnfsh | 辦一場 Airflow Tutorial `100%`
| 讓大家都掌握 ETL 的技能 @davidtnfsh | 團隊每個成員都有在 pycon github 實做出一個 dag `20%`
| 讓結案報告和 data team 中 ETL 相關的工具互相豐富 @tai271828  | 實做 layer between rg-cli and airflow/bigquery `40%`
| 整理pycon網站架構、SEO網址邏輯  @stacy  | 1.確認可修改網頁(等網頁)`0%` <br> 2.撰寫SEO tag(等網頁) `0%` <br> (再確認需要調整的網址)<br> PS.Max記得latest要加上og tag、canonical啊啊啊啊不然社群分數都沒有我會哭 (Max 收收)
| 調整 PyCon 網站 SEO 架構 @maxlist2020   | 1. 增加歷年網址於 footer `0%` <br> 2. 調整網址導向 latest `100%`<br>|
| 熱門問題分析 @hane | 1. 分析 FB 上常被詢問的問題類型，預期建立20題常見問題知識庫 `0%` <br> 2. 建立 FB 開發應用程式(測試用)串接粉專 messenger api `20%` |

## 1/6 會議記錄

:::info
- **簡報網址:** 
- **講者:** 
:::

1. [name=Stacy]
    * 這兩週：因為今天請假+最近SEO還在等網頁那邊...沒動作實在太心虛了所以做一個網站分析(基礎版)，大家可以想想還有什麼想看的 >>[點我](https://datastudio.google.com/reporting/5239293b-142e-4372-a947-a4171d8eb002)
    * 未來兩週：none
    * 需要討論：none
2. [name=tai]
    * 這兩週：結案報告的 DAG。 rg-cli 已經整合進去，剩下掛資料的部份
    * 未來兩週：上傳資料 with bigquery + 倒進 ware house
    * 需要討論：
        * 實做上應該會遇到一些問題，再隨時煩 david Jr
        * stacy 的網站分析好棒r
1. [name=David Jr.]
    * 這兩週：
        * review tai 的 PR(感恩大大~)
        * 寫 OKR 會議的 agenda，下次週會就看這份拉~ (https://hackmd.io/LLcaglX0Szed-AsHUdC3bg#OKR-Template)
    * 未來兩週：
        * 執行 OKR 討論的 Objective~
    * 需要討論：
        * 週六 12:00 沐樂咖啡見
3. [name=Lee Wei]
    * 這兩週：
        * review tai PyCon-ETL PR
        * setup ci pipeline for rg-cli
        * 煮飯
    * 未來兩週：
    * 需要討論：
9. [name=Max]
    * 這兩週：請假
    * 未來兩週：
    * 需要討論：
9. [name=Hane]
    * 這兩週：none🤔
    * 未來兩週：none🤨
    * 需要討論：none😅


## 12/23 會議記錄

:::info
- **簡報網址:** 
- **講者:** 
:::

[Meeting Prerequisites](https://hackmd.io/IuQU8ljqRt-bieeAPVQ6Sg?view#Prerequisites)

1. [name=PinChun]
    * 這兩週： 逛街大家建好的bq 還有結報生產器
    * 未來兩週：
        * 整理之後結報需要的數據
        * 整理贊助執行所需的BQ join過後的表格
    * 需要討論： 
1. [name=David Jr.]
    * 這兩週： 
        * 實作完 search 雙週報 + deploy 到 Airflow
        * 整理轉型會議的 agenda
    * 未來兩週：
        * 看轉型會議有啥結論
        * 約 2021 的 OKR 實體聚~
        * 祝大家聖誕快樂 :christmas_tree: 
    * 需要討論：
        * 等等[轉型會議](https://hackmd.io/IuQU8ljqRt-bieeAPVQ6Sg?both#Agenda)
3. [name=Lee Wei]
    * 這兩週：
        * WIP: 跟 PSF 要 basic membership in Taiwan 做 benchmark
    * 未來兩週：
    * 需要討論：
7. [name=Stacy]
    * 這兩週：none
    * 未來兩週：none
    * 需要討論：none
9. [name=Tai]
    * 這兩週：
        * (yuhow 告訴我)結案報告都寄給贊助商了
        * released rg-cli to PyPI (2020 version)
            * https://pypi.org/project/pycontw-report-generator/
            * v1.5.0
                * [name=Wei] 我好像忘記弄 pull requests 的 action 了xD
        * (無關) 放長假前工作好忙r
    * 未來兩週：
        * 加 airflow plugin 來自動產生同一份結案報告
    * 需要討論：
        * data infra 和 growth 我都想做其實...
            * 我也想玩 discord 雙週報 XD
9. [name=Max]
    * 這兩週：點 Django 技能
    * 未來兩週：none
    * 需要討論：none
9. [name=Hane]
    * 這兩週：做了個 Dialogflow 測試 bot 
    * 未來兩週：none
    * 需要討論：none

## 12/9 會議記錄 Template

:::info
- **簡報網址:** https://docs.google.com/presentation/d/1DPiHq7qHxFbejyf_2wv0aVcRE4LZb3480a9bAPTd9uc/edit?usp=sharing
- **講者:** David Jr.
- **出席:** 
:::

1. [name=David Jr.]
    * 這兩週： 做簡報
    * 未來兩週： 把 SEO 雙週報的機器人架上去
    * 需要討論： 等等分享～
3. [name=Lee Wei]
    * 這兩週：
        * Reivew rg-cli
        * 跟 Matt 討論官網 staging db
            * Solution: 調 postgresql 的 docker 設定 & GCE firewall 讓 DB 可以被 GCP 同一 project 上的其他 services 可以 access
    * 未來兩週：
    * 需要討論：
        * 今天大家要一起來看 Ofa 分享的 [廣告&行銷 大法好](https://docs.google.com/presentation/d/1oKdTyTRJAM8z0uj9xwj0aTcQdUoVqee1gerInw2bq8g/edit#slide=id.p) 跟 [衝刺大法](https://www.dropbox.com/s/bipgijw9d9a59x4/%E8%A1%9D%E5%88%BA%E5%A4%A7%E6%B3%95.pdf?dl=0) 嗎～
7. [name=Stacy]
    * 這兩週：
    * 未來兩週：若網站可調整，和Max討論實際修改項目
    * 需要討論：
9. [name=Tai]
    * 這兩週：
        * completed 結案報告，包括
            * rg-cli
            * content
    * 未來兩週：
        * wrap up rg-cli and release
        * reworking max new letter
        * continue picking up blog SEO knowledge
    * 需要討論：
9. [name=Max]
    * 這兩週：
        * 點 Django 技能中
        * 建構 PyCon 暫時的 2021 靜態頁面
        * 重構 max newsletter
    * 未來兩週：
    * 需要討論：
        * 回報 web team 討論後的結果：
            1. 增加管理 SEO Tag 後台
            2. 歷年大會網站資料整理、呈現在目前官網上
            3. 今年活動網址修改(固定 latest)
9. [name=Hane]
    * 這兩週：
        * 整理了粉專的貼文和回覆內容
        * 看了一下BigQuery的用法（看到要綁卡就...(艸
    * 未來兩週：
        * 針對粉專貼文和回覆擷取關鍵字貼標
    * 需要討論：

## 11/25 會議記錄

:::info
- **簡報網址:** 
- **講者:** 
- **出席:** 
:::

1. [name=David Jr.]
    * 這兩週： 
        * 實作了 google search console 的 airflow 
    * 未來兩週：
        * 準備下次分享：data team 的 tech stack 101
    * 需要討論：
        * PoChun 的需求（平衡想做的事和其他夥伴們的需求）：https://hackmd.io/@pycontw/SyG5_GrED/%2FNbRo4f7hQ2G3AIiAU9jnIg
        * 上次 OKR 會議 Stacy 有提到大家分工不明確，這邊等 tech stack 101 分享完再來討論~
3. [name=Lee Wei]
    * 這兩週：
        * Minor code quality update for PyCon-ETL
    * 未來兩週：
        * Maybe some more CI/CD improvement
    * 需要討論：
        * 上次說的官網 staging DB 目前有要到了嗎～
            * 如果有的話，我會開始搬去年開在官網的 issue
        * 2020 影片其實好像都有了，是我說錯了 😢
        * 我們要 deploy 任何東西前，可能會需要先把 authentication 弄好～
7. [name=Stacy]
    * 這兩週：
    * 未來兩週：
    * 需要討論：
        * 11/25
            * 盤點了一下pycon目前網站架構，發現很多內容都是pycon歷年舉辦大會的資料，是否要建立「歷年Pycon」專區，讓Event頁浮上檯面也能擴充內容
![](https://i.imgur.com/wOXLSCY.png)

9. [name=Tai]
    * 這兩週：
        * 都在玩 Max NewsLetter 的 side project XD
            * today's free packt "Python API Development Fundamentals" https://subscription.packtpub.com/book/web_development/9781838983994
                * https://www.packtpub.com/packt/offers/free-learning
            * "12 factor app"
        * working in progress 結案報告
            * will implement a airflow plugin (myself or pass the command to David)
    * 未來兩週： 定稿結案報告 (影片應該是傳完惹！)
    * 需要討論：
        * 結案報告完成後會轉向 blog SEO，中間藉著玩 max newsletter 點一些網路行銷相關的技能樹
        * 完全鼓勵把「學 xxx」放進個人 quarter obj
9. [name=Max]
    * 這兩週：完成一隻 LINE-Bot Side project + 看 Django + 玩 max newsletter
    * 未來兩週：會參與 team web 討論，把 SEO Tag 加入進去
    * 需要討論：
9. [name=Hane]
    * 這兩週：在玩 DialogFlow 建立 chatbot
    * 未來兩週：可以研究一下 DialogFlow 串 BigQuery 存對話紀錄的做法
    * 需要討論：目前沒有

## 11/11 會議記錄

:::info
- **簡報網址:** https://github.com/hsuanchi/crawler_shopee_public
- **講者:** Max
- **出席:** 
:::

1. [name=David Jr.]
    * 這兩週： 
        * 完成用戶條款跟內部的保密協議，感謝泰祥、李唯、馬兒、Rock 跟 ~~demoji~~ deimos
        * 完成上傳 sponsor 問卷的 airflow dag
        * 研究匯入 google search console 的資料
    * 未來兩週：
        * 匯入資料
        * 確保大家都有能力操作 Airflow 
3. [name=Lee Wei]
    * 這兩週：
    * 未來兩週：
    * 需要討論：
7. [name=Stacy]
    * 這兩週：
    * 未來兩週：
    * 需要討論：
        * 11/25
            * 盤點了一下pycon目前網站架構，發現很多內容都是pycon歷年舉辦大會的資料，是否要建立「歷年Pycon」專區，讓Event頁浮上檯面也能擴充內容
9. [name=Tai]
    * 這兩週：
        * 協助演講影片上傳（結案報告要用）
        * 都在玩 Max NewsLetter 的 side project XD
        * 工作比較忙 orz
    * 未來兩週： 定稿結案報告
    * 需要討論：
9. [name=Max]
    * 這兩週：
    * 未來兩週：
        * 歡迎來玩 Max NewsLetter 的 side project XD
    * 需要討論：
9. [name=Hane]
    * 這兩週：一直很臨時地被派去出差和開會，不知道在忙什麼QAQQQ
    * 未來兩週：寫個程式整理用戶留言及回應
    * 需要討論：目前沒有

## 10/14 會議記錄

:::info
- **簡報網址:** https://github.com/hsuanchi/crawler_shopee_public
- **講者:** Max
- **出席:** 
:::

1. [name=David Jr.]
    * 這兩週： 
        * review 使用者條款
        * 感謝 stacy 上次的 feedback，想約個定期的線下讀書會，讓想學 Python 或其他技能的志工們有機會面對面交流（地點挑個咖啡廳之類的）
    * 未來兩週：寫保密協議 draft
    * 需要討論：
        * 11/11 airflow tutorial (感謝博安老師跟 @clleew ) QQ 抱歉打錯名字了
            * [name=Wei] 是偉大的博`安`老師哦xD
3. [name=Lee Wei]
    * 這兩週：
        * Rain 被 AWS 的窗口找了，所以我也要開工了
        * review 使用者條款
    * 未來兩週：
        * 下下次可以分享 table manners
    * 需要討論：
5. [name=Rain]
    * 這兩週：AWS 的窗口來找我了，直接被迫開工談合作
    * 未來兩週：
    * 需要討論：
7. [name=Stacy]
    * 這兩週：感謝Max先幫我爬了整個網站url，裡面有很多奇怪的轉址....但原諒我這禮拜被鬼抓走沒有整理完
    * 未來兩週：把整個網站架構整理好
    * 需要討論：目前沒有
9. [name=Tai]
    * 這兩週： 結案報告已動工 1) 東西跑得出來 2) 修了一些小東西 <--- 算完成 50% 惹！
    * 未來兩週： 定稿結案報告，包括
        * 填入實際文案
        * 文案要等最久的應該是演講錄影（已出爐，等放到 youtube）
        * 「送出」另外算
    * 需要討論：
        * 結案報告送出時想發一篇 blog 來總結 2020 <-- 同時是 blog 內容物
        * 有空的話還是會想多利用 airflow 來豐富結案報告，或是在製作結案報告過程中豐富 airflow
9. [name=Max]
    * 這兩週：爬取 PyCon TW 網站 TDK 結構
    * 未來兩週：與 Stacy 整理網站結構
    * 需要討論：PyCon TW 網站修改 TDK
9. [name=Hane]
    * 這兩週：下載粉專資料＆整理用戶留言及回應
    * 未來兩週：寫個程式整理用戶留言及回應
    * 需要討論：目前沒有


本此分享 [name=MAX]
    - 競品：競爭品牌
    - boston 矩陣

立體七星劍

台博館有賣好看的虎爺毛巾

建議：去 python 投稿r...XD

## 10/18 的 OKR 成果

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
            1. 辦一場 airflow tutorial
            2. 團隊每個成員都有在 pycon github 實做出一個 dag
            3. Q4先把整個網站架構拉出來(url的層級、Title、Description、H1)
            4. 辦一場 team building
            5. 分析 FB 上常被詢問的問題類型，預期建立20題常見問題知識庫

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
            - 我沒特別訂目標xD 主要以我知道的項目（e.g., rg-cli)的協助為

## 會議記錄 Template

:::info
- **簡報網址:** 
- **講者:** 
:::

1. [name=David Jr.]
    * 這兩週： 
    * 未來兩週：
    * 需要討論：
3. [name=Lee Wei]
    * 這兩週：
    * 未來兩週：
    * 需要討論：
7. [name=Stacy]
    * 這兩週：
    * 未來兩週：
    * 需要討論：
9. [name=Tai]
    * 這兩週：
    * 未來兩週：
    * 需要討論：
9. [name=Max]
    * 這兩週：
    * 未來兩週：
    * 需要討論：
9. [name=Hane]
    * 這兩週：
    * 未來兩週：
    * 需要討論：