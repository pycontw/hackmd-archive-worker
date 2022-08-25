---
tags: 2021-organize, 2021-data, data team, data strategy
---

# Data Team: 堅持還是轉型？

**共識：前三 months (data infra) 後九 (growth)**

## Prerequisites

想拜託大家這 4 篇在與會前都看過，不然不易取得共識XD
想拜託大家這 4 篇在與會前都看過，不然不易取得共識XD
想拜託大家這 4 篇在與會前都看過，不然不易取得共識XD

> [name=Wei Lee] 可是這裡有三篇 🤔 (david: 感謝，我又更新了一篇XD)

1. 每間公司的 data team 架構都略有不同：https://blog.getdbt.com/data-team-structure-examples/
    - [name=Wei] 我最近有稍微在玩 dbt 耶xD
2. 每個 Data 相關的 function，其職責是是什麼？ https://www.sisense.com/blog/the-6-functions-of-a-data-team/
3. Growth Team 的職責：https://andrewchen.co/how-to-build-a-growth-team/
4. MarTech: https://www.awoo.com.tw/blog/2020-martech-edm-tigerfly/

## Agenda

1. 六頂思考帽：https://hackmd.io/xp8vq_LdR4WKAukQPZLtGw?view#%E7%95%B6%E5%A4%A9%E9%96%8B%E6%9C%83%E6%B5%81%E7%A8%8B
2. 用 six thinking hat 的流程走過下列三個問題的每個提案

## 問題清單：能麻煩大家把想到的問題都列下來嗎？我們再來整理成下次會議的 Agenda~
1. 目前的團隊願景和 Q4 的 OKR 是否衝突？
    - [name=stacy] Growth Team 跟 Data Team 的目標不衝突，沒有 SEO 帶來的資料就沒辦法產出 dashboard 給其他人做 data-driven (Tai, Wei +1)
        - [name=tai] 認同 Stacy 觀點 (refer to sisense 那篇文章，把 growth 視為 data team 的一部分)
        - [name=Wei] 回朔到 data warehouse 的話題，data warehouse 可能只是達到 data driven 的手段，所以不一定衝突
    - [name=David Jr] 覺得在 priority 上是衝突，因為目前已經有資料了，需要優先驗證的是目前的資料是否足夠讓其他 function 做決策。組成 Data-Driven 的兩個要素：
        - 有資料
        - 有 dashboard 輔助決策
3. 個人目標 v.s 組織利益的 priority 誰優先？
    - [name=Wei] 在符合組織利益的情況下，尋求個人目標的最大值（聽起來也許是偏組織？）(David Jr 應該是 +1，我猜唯一不同的點是這件事情需不需要有價值)
        - [name=David Jr] 在不危害組織的利益下，做自己想做的事情
        - [name=tai] 我好像稍微偏向 David Jr 的觀點一點
        - [name=Max] 同意 David Jr 的觀點多一點
4. 每個人 OKR 適合存在於 data team 嗎？是否有其他 function 適合所有人的 OKR？抑或各自適合的 function 難以整合？
    - [name=David Jr] 不適合，Growth Team 比較適合。SEO 不是 data team 的業務，有聽過 growth team 在負責（請參考上面的 ref）；Chatbot 像是 ML engineer 的業務；Airflow 則屬於 data engineering 的事。 
5. 小結個人立場
    - [name=tai] 刷完四篇文章後，我初步對方向的看法是
        - 團隊名字叫做原本的 "data & strategy" 或是換名稱成為 "growth" 都很好，根據這幾篇文章，這兩個名字也都有人用。
            - 團隊重新命名（與決定側重 data infra 還是 growth）
                - 如果用原本的名字 "data & strategy" squad 下面每個人的角色可能就要 by function 大致講好，例如誰做 growth 誰做 data infra 誰是 DA
                - 如果用 "growth"，我會想知道 data infrat 會誰來做？還是併入 infra team??
            - 在交出第一個 milestone 的成果前，除非組織運作明顯有重大瑕疵，原則上我稍微傾向不 re-org。有一些成果的前提下 review 才有機會更具體 --> 定義成果（每季 OKR?）
            - 也可以更 long-running 一點，像是早期（也許就要個一年）維持使用 "data & strategy" 的架構， data infra 運作到某個程度之後，再把 growth 獨立出來，然後 data infra 併入 infra
            - 另一個觀點是因為還在籌備相對前期（大概跑了一季，用掉一年的 1/4），re-org 也許成本低，如果主席覺得付出的成本遠小於收益的話，也能採取現在立刻馬上 re-org。只是如果要採取這個方案，re-org 可能要兩週內發生比較好？這樣還有一季可以 dry-run；已經用掉一年的 1/4 是個說多不多、說少不少的量。
                - 至少要有兩季來維護與執行 annual conf 本身。


# by 6 hats 六頂思考帽原則下大家的意見發言記錄
1. 代表「思考管理」的藍帽：安排思考順序
    - 「白帽先行、黃在黑前、黑後有綠」
1. 代表「資訊」的白帽：充分蒐集各種數據、資訊
    - [name=tai]
        - 很多公司行號與團隊都正在 data & strategy 與 growth 哪個為重心間搖擺
        - 我們這種架構（data 下有人想做 growth）也有公司使用
        - 我們的 data 下有人想做 growth
            - 也有想做 growth 的人想做 data infra，反之亦然
    - [name=stacy]
        - PyCon TW 籌備團隊內每個 team 或多或少都會（或是都可以）用到 data
    - [name=davidJr]
        - SEO 歸類在 growth 下
        - 有人 growth 獨立出去
            - e.g. linkedin
        - 啊我漏掉了 [name=tai]
    - [name=wei]
        - ETL 有人正在實做、也會用到
        - SEO 有人正在實做、也會用到
        - chat bot is depening on its usage，if 有，也算是蒐集資料（但是不是最好的手段則可以再討論）
    - [name=max]
        - discord 機器人正在運作中
        - 如果數據量更多一點可以對大家在洞察上有幫助(目前 PyCon TW Search Console 的數據跟其他手上的專案比起來約是萬分之一)
1. 代表「感覺」的紅帽：用情緒感受 
    - [name=tai] 不衝突：團隊還算喜歡、至少是不排斥目前的合作節奏，即使方向還在摸索中
    - [name=wei] 跟 tai 一樣 XD 😆
    - [name=max] 大家前進，大家有做自己想做的，也都對 PyCon 有幫助
    - [name=stacy] 大家都有在做，但方向不一
    - [name=Hane] 想做的事情對組織有益，但還沒完整性的規劃，無法看到這些事的實際用處
    - [name=david jr.] (stacy + hane) / 2 ? 沒照 OKR ，有分歧了，目前統合意見還沒做好 
1. 代表「價值」的黃帽：專注於價值、好處和利益
    - 可用於精準投放廣告、徵才牆的職缺等等
    - [name=tai] data-infra (贊助例行工作)、growth（贊助開發新贊助商）。不衝突：維持原本氣氛合作感覺成本低，衝突：集中能量
    - [name=wei] 照著認為不衝突的方向的好處（維持目前節奏、成本低），認為衝突的好處（提早修正方向成本低）
        - 怎麼有點我在玩文字遊戲的感覺（笑   （驚）
    - [name=stacy] 不衝突：、衝突：
    - [name=hane] 不衝突好處：很多 team 應該還是可以用到 infra   衝突好處：提早
    - [name=max] 跟 tai 一樣 XD
    - [name=davidJr] 跟 max 一樣

1. 代表「負面」的黑帽：專注在找出問題所在、負面情緒
    - [name=tai] 不衝突：可能兩者都做不好(data infra vs. growth)，衝突：想做 growth 的人會覺得無聊
    - [name=wei] 不衝突：同 tai(?)   衝突： re-org 花心力成本、也不知道是不是正確方向
    - [name=stacy] 不衝突：任務破碎、發散，大家會不停懷疑自己對組織帶來什麼益處（懷疑自己在組織中的價值）    衝突：有人可能會覺得無聊；啊我就想做 data infra R(?)  ~~growth 我很會惹~~ ~~我才沒有ㄅ要亂講~~  😆
    - [name=hane] 不衝突：同 stacy   做出來的東西可能不符合 pycontw 整體需要的東西，事後修正更花成本       衝突：每個人的專長不同，如果側重 growth，可能有人需要 pick up 時間長、已經熟悉的人又會覺得很無聊
    - [name=max] 不衝突：實做時間拉很長   衝突：有人會覺得無聊/離開
    - [name=davidJr] 不衝突：太分散、不像一個 team；如果事後發現不是其他 team 需要的東西，可能會沒有成就感   衝突：可能有人覺得無聊
        - 大家開始意見「跟其他人一樣」，似乎有共識！


1. 代表「創造」的綠帽：專注在想出解決辦法、新點子
    - [name=tai]
        - team 重點前期（前 3 個月） data infra、後期（後 9 個月） growth
        - 搭配落實 mentor/mentee 制
        - 範例
            - 前期 team goal data infra 為主
                - growth 專長的人可以 bi-weekly 分享自己的專業給其他人分享
                - data infra 專長的人認真實做 + 認真帶其他專長的人做 data infra
    - [name=wei]
        - 擴編啦擴編，招募組上ㄅ
    - [name=stacy]
        - 堅持先弄好 infra >>也沒有堅持，就是看到最後可以做的部分
            - 認為 infra 是不管做什麼都要的，所以一定要實做完
        - 要釐清 davidJr 關於「順手建 ware house」這件事情的 warehouse 該長什麼樣。
    - [name=hane]
        - team 重點前期要是 data infra
        - 我同意前三後九
        - 也許可以普查其他 team 的資料需求
    - [name=max]
        - 擴編擴編
        - 我同意前三後九
    - [name=davidJr]
        - 前面先照著 tai 的作法，招募擴編成功後獨立 growth team
        - if 招募不順利，限縮題目在 chat bot and SEO，品淳（贊助）的需求變成「順手把 ware house」建立起來。本質上是獨立成 growth team。

markdown 會自己解讀 1. 1. 1. 變成有意義的數字列
可是看起來就很啊雜 xD
    - 好處是不用改一個中間的數字、後面就要全部改
    - 阿砸+1 強迫症會發作

**共識：前三後九**
other action items: next meeting
- [ ] 討論 data warehouse spec (ref: 各 team 資料需求)
- [ ] 請 pingchun、伯俊、Rex 以及所有的 function 提需求，你們需要看哪些資料通通丟出來~

# 下次 meeting (實體) 會再開投票


# Summary of 4 Articles
上面列的四篇文章裡，摘要自己覺得有趣、可能會用在討論裡的資料。


## getdbt
https://blog.getdbt.com/data-team-structure-examples/
    - 沒有標準答案，剛好和下面 sisense (growth 是 data team 一個分支) 和 andrew chen (growth team 獨立出來、提高層級) 的文章呈現對照
    - 列出各公司組織圖與考量，很有意思的整理


## sisense
https://www.sisense.com/blog/the-6-functions-of-a-data-team/
    - 把 growth 視為 data team 的一支業務（和下面 andrew chen 的觀點有點稍微不太一樣，層級可能不同）
![](https://i.imgur.com/9OT4X1C.png)


## Andrew Chen
https://andrewchen.co/how-to-build-a-growth-team/
    - growth team 是整合與推動這四種業務
![](https://i.imgur.com/eC2aPqo.png)
