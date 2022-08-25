---
tags: 2022-organize
---

🔙 Back to [歷年 PyCon TW Organizing 共筆](/ryPr7SFyP/%2FHM5mHCFKQCu7-W5ea8ITcw%3Fview)
🔙 Back to [PyCon TW 2022 Organizing 共筆](/F4qRbwIsQXWH5B6cZ6Pzyw)
🔙 Back to [PyCon TW 2021 Organizing 共筆](/Wb9vQrfJQk-5tPoPR23hwA)


# RFC: Run Metabase database on CloudSQL

## Agenda

1. 先完成六頂思考帽，當天如果有人臨時加入想發言，也請麻煩六頂帽子都完成
2. 跟 amazon 一樣 pre-read
4. 開會讓大家分享自己 proposal的黑帽跟綠帽
5. 對其他人的帽子有沒有疑慮跟問題
6. 一起想解法

## Six Thinking Hats

1. 白帽子：中立、客觀（可以分享數據、開銷、metabase 的使用頻率、跟 @clleew 問的問題「這件事會多頻繁的發生、這件事發生時，修復所需要的成本有多少、如果沒有及時修復，造成的損害是什麼」

    1. [name=Matt]
        1. 開銷方面請見 [cost break down](https://discord.com/channels/752904426057892052/965930537132908555/966432796514058251)，data team GCE 目前一個月大概花 35 鎂
    2. [name=Lee]
        1. 根據 DJ 在 [Discord Thread 的資訊](https://discord.com/channels/752904426057892052/965930537132908555/966135237098733619)，一個月的花費是 NTD$ 300 - 750 ，一年則需要花費 NTD 3600 - 900
        2. 於 1 月的籌備團隊 sprint ，決議否決至少自 2016 年使用的 g suite / google workspace ，原先若要花錢解決的成本約為 NTD 15,000
    3. [name=David] 沒參與到 pass
    5. [name=Tai] 同 matt and wei lee
    6. [name=LiYing] 
        1. 我是這次metabase壞掉才參與相關專案的，沒有足夠背景，pass
    8.  [name=DJ]：
        1. 這件事發生時，修復所需要的成本: 之前有過兩次 metabase 的維修（不是 pg 損毀），沒有保留當初的番茄鐘但確定每次都修超過 `2hr（時間成本超過 NTD700)`
            2. update: 上次修是 [2/5](https://discord.com/channels/752904426057892052/927477705975410748/939356538466861114)
        3. 如果沒有及時修復，造成的損害是什麼: 至少 `兩人` 不能用，至多目前無法回答（這週有被我看到在使用的人有 AndyLee 跟 Kevin）
3. 紅帽子：直覺、情感
    1. [name=Matt]
        1. self-hosted solution 一年壞個 2-4 次我覺得算蠻常見的（目前 metabase 應該是半年不到就壞兩次，雖然剛開始但頻率還是稍嫌高一點）
        2. 開 DB 只存少少幾個 query 稍嫌浪費，有非常多手段比開一個 DB 更便宜，就算不走 GCE snapshot，最陽春的做法全部 query 用 text file 存或定期 pg_dump，以目前 query 數量要手動加回去或 pg_restore 也是一個小時內（且不用重開機器、重建 volume）
        3. [自肥] 不管開 DB 只存 metabase query 這件事效益是高是低，如果有多 serve website DBs 的話都一定是增加效益XD
    2. [name=Lee]
        1. 時間確實寶貴，但我對於「直接以志工的時薪來計算志工組織成本，是否合理」稍持反對意見。 metabase 所造成的短期、長期效益目前對我來說還不明確（p.s. 這裡並非說沒有效益，而是我不具有這樣的資訊），是否值得每個月做這樣的投資
        2. 承 1-6-1 ，如果以一年發生 2 次 metabase 維修，並且花費 `3 hr`，那時間成本就目前有的數字計算出來並不會比一年課金多
        3. 原先做結論的方式有些不夠謹慎
        4. PyCon TW 外包的東西越來越多，固定支出一直增加，但收入增加的幅度、穩定度趕不上，會增加以後的籌備風險
    3. [name=David] 如果只能不斷壞掉和修復的話，就花錢解決吧
    4. [name=Tai]
        1. 保守派；基礎建設沒事不想更動，動了就要有人，累！ XD
        2. 預算考量（同 lee wei）；我們花錢上好像有一層道德責任（有點拿社群錢的感覺？）
        3. 志工時間也很寶貴
    6. [name=LiYing] 
        1. 時間確實寶貴、但也許也可以再壞掉的時候由原志工帶新志工修復作為理解架構及技術交流的契機?
        2. metabase的效益與維護成本如何評估?
    7. [name=DJ]: 時間是全宇宙最貴的東西;而大家這個年資的時薪多半都超過或接近 `NTD 700/hr`, 覺得志工們的時間成本已經高於 cloud sql 的收費了，所以付錢託管是划算的。
5. 黑帽子：謹慎、負面
    1. [name=Matt]
        1. 養套殺+1
        2. 這筆錢我們是不是花在最值得花的事情上？
            - 如果確定大家願意花錢在 Cloud SQL for BI，那我就會開始爭取網站組組內可以花錢解決的事（像是以前就提過的 GCE managed instance group for zero-downtime deployment 或是 Cloud SQL for website DB 等）
    1. [name=Lee]
        1. 同 DJ 養套殺
        2. 省下的時間，我們是否真的拿來做更有價值的事了
    3. [name=David] 多一筆開銷，但我覺得投入也無仿
    4. [name=Tai] 養套殺 +1
    5. [name= LiYing] 養套殺+1，另外我認為PyCon畢竟是個技術社群、在可負擔的成本內應盡可能保有技術能力。但另一個角度來看，雖然說這是個練技術的機會，但不確定目前的志工組成有沒有夠多的人力來分散扛風險?
    6. [name=DJ]：花了就不容易取消，不確定我們現金水位是否健康、外包了團隊就少了這個練技術的機會，之後只能被養套殺
7. 黃帽子：積極、正面
    1. [name=Matt]
        1. 認同花錢消災，時間拿來休息都值得。
        2. 就我觀察目前開發組志工背景大多是兩年以下工作經驗且還是以 web development 為主，有 operation 經驗的志工實在是跟日本壓縮機一樣（2020-2022 我知道的加起來大概 5 人），所以 ops 負擔越少的話壓力會小很多。
        3. 很多有一點規模的公司也喜歡用託管服務，志工在這裡獲得使用經驗也許多少幫履歷/職涯加點分。
    2. [name=Lee]
        1. 花錢消災，時間可以拿來做更有價值的事
    3. [name=David] 能夠花錢解決就花錢解決吧
    5. [name=Tai] 花錢消災、有新玩具玩
    6. [name=LiYing] 花錢消災，時間可以更好的應用，託管服務的使用也是技術學習的一部分
    7. [name=DJ]：託管服務可以提升組織的抗風險能力，哪天即使今天與會的所有人都暫離社群，這個服務也不會掛或比自架好維護；時間是宇宙最貴的東西，可以花錢解決然後注重在組建團隊、帶新人讓志工們有歸屬感這種不能外包的事情，I think it's a better use of time.
8. 綠帽子：創意、巧思
    1. [name=Matt]
        1. 也許可以查 metabase 有沒有方便的 version control or IaC solution，雖然建置可能相對複雜，但維護成本也許低到可以接受
        2. 先進行省錢大作戰就可以花得安心
    2. [name=Lee]: 
        1. 如果 metabase 沒有必須 zero down time，每次的下線也許都能做為資深志工訓練新志工的一環（招募不是每次都找到很多人說要來學技術嗎 lol）
        2. [probably a bit off topic?] 解決有難搞的人 (i.e., 我) 覺得花錢決策不夠謹慎，將這次決策的方式作為以後做決策的範本
    3. [name=David] 有沒有考慮跨遇到其他便宜的國家買？
    5. [name=Tai] 搞不好真的釋出很多生產力 or 更方便更多人一起維護？
    6. [name=LiYing] 換個BI?
    7. [name=DJ]: 如果我們用這個[計算機](https://cloud.google.com/products/calculator#id=d7e4fda5-841d-4291-9714-1fa3e3b98c81)調整一下機器的配置，可能可以讓價錢落在 NTD 300~700 / month

------

## David JR.

是說這 snapshot 的用法是不是要重新 create instance 然後再 attach disk 啊？
https://stackoverflow.com/questions/42476941/how-to-restore-instance-using-snapshot-in-google-compute-engine
Stack Overflow
How to restore instance using snapshot in Google Compute Engine?
I created a snapshot of a VM instance via cloud console. I would like to know how I can restore an instance using a snapshot. The documentation for compute engine is not very helpful. The instance ...
Image
這樣的話又有點猶豫了
整台 instance 重建的話，data 的其他服務都要重開。隨著志工來來去去 + 服務變多(目前只有兩個)，重開 instance 造成的 service downtime 會被拉長 😢 
這樣的話我傾向 花錢而不是花時間


## Wei

我覺得我對於這件事的效益理解還不夠
現在有的資訊是 這筆錢跟志工的時間相比很少，但目前我還會想知道

* 這件事會多頻繁的發生
* 這件事發生時，修復所需要的成本有多少
* 如果沒有及時修復，造成的損害是什麼


## Matt

我自己是對於志工團隊願意投在開發上的額度非常不了解，budget 多寡對於開發上做出什麼選擇影響頗大，但過去連多開一台機器讓 CI/CD 好做一點這種已經確定會減輕大家負擔的開發都被擋下來，所以在我觀念裡面 PyCon TW 對於開發的投資就是偏向保守，畢竟非營利性質所以我也完全可以接受，不過若是我們在這方面的資訊能有更多交流的話也許決策會更順暢。


## David

如果短時間內這種狀況是我們沒辦法有效解決 (降低發生頻率，更好是完全解決)，我傾向砸錢解決，單純從個人覺得這筆投資該花。

## Li-Ying
老實說我對整個狀況的理解都還不夠，Wei跟Matt提到的都是我想知道的部分，但從目前上面大家的討論透露出來、我了解到的是花錢消災相對於志工群可以供的人力資源機會成本較小。

## Action Items
- [ ] metabase 是不是要更正式融入流程中？
    - [x] metabase 可以加 GA，如果能評估到一定使用程度的話，大家應該都會滿認同這個執行方案。
    - [x] 要做的話就要認真 promote in the community
- [ ] 先評估個半年，開最小的 instance，然後設個 upper bound，如果超過 or GA 發現根本沒人用的話我們就要賣股票 rollback 了，然後 @davidtnfsh committed 說如果發生上述情況要負責 rollback
- [x] 給 @yungshenglu 來約，讓 data team 跟可能需要 metabase 的人介紹，推廣 data driven 或看報表的價值？

## 風險
- [ ] upper bound 超過預期
- [ ] roll back 的人勞跑 XD
- [ ] 後面團隊不評估就直上續約（或是反過來不維護）