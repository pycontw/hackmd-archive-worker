---
tags: 2020-organize, program
---

🔙 Back to [PyCon TW 2020 Organizing 共筆](/5u84SOprTUeQYBR57TH49w)

# 2020 議程組 Retro

:::info
- **Location:** https://meet.google.com/frv-arjr-udf
- **Date:** Sep 12, 2020 10:00 PM (TST)
- **Agenda**
    1. 閒聊 `15 mins`
    2. 大家稍微寫一下自己在各項事項的想法/意見 `15 mins`
    3. 一起走過大家的想法 `60 mins`
    4. 閒聊 `30 mins`
- **Participants:**
    - Wei
    - pochun
    - Jordan
    - petertc
    - Winnie
- Action Item
    - 一起更新 [PyCon TW 2020 Organizing 共筆](/@pycontw/HkXbemQeP) 議程組部分
    - 明年應該會使用 Discord 籌備，歡迎一起加入 https://discord.gg/cAsVJM 🙂
:::


## Keynote Speaker
### 做得不錯可以繼續
* 今年很早就完成 Keynote Speaker 的邀請！遠端參與應該有提升 Keynote Speaker 的意願
* Keynote Session 看得到現場會眾，Keynote Speaker 對此很滿意
    * https://twitter.com/mariatta/status/1302081926547660800

### 做得不夠好，也許可以改善
* 對 Keynote Speaker 的想法可能不夠明確，像是 SITCON 好像會有跨年度主題
    * 對 PyCon TW 好像還好（？
* Mariatta 的 session 開始前，還沒有登入 google 帳號
    * 在每一場議程開始前要 set up 好設備
    * 在 opening 開始前就要有人在各演講廳待命

### 也許明年可以嘗試
* Call for Keynote Suggestion
    * [Suggest a Keynote Speaker for EuroPython 2020](https://docs.google.com/forms/d/e/1FAIpQLSdXISyYyEDy9gExkr4Znjw2anujEA4jQyKLDGB7UnnofFJs1w/viewform)


## Talks
### 做得不錯可以繼續
* 有注意講者時區，但 rehersal 沒做到
* 今年有會眾反應步調比較慢、比較舒服、比較台南
    * 雖然我們也沒有增加休息時間 xDDD
    * Winnie -> 覺得 2019 太緊湊，休息時間要更多（今年有多一點點啦 by Wei）
        * 每個休息時間拉長一點
        * 大地遊戲也是活動的一環 -> 交流 up 贊助商 up

### 做得不夠好，也許可以改善
* 會後問卷認為今年的演講深度不夠
    * 我們好像也沒辦法...
* 15 分鐘的議程不夠深入
    * 明年加回 45 分鐘的議程，但不一定要砍掉 15 分鐘
        * Winnie -> 20 / 30 / 45 分鐘 （好，那明年就這樣定了 by Wei）
        * TP 覺得三種可能對講者太複雜
            * maybe 20/45 ? 20/35 ? 20/40?
    * 也可以看投短講的深度來決定錄取量
* 以遠端場來說，人太少決定不轉播，有被抱怨
    * 如果現場人少還是可以轉播 

### 也許明年可以嘗試
* Young Adult (高中以下)
    * Winnie 覺得不錯 -> 那明年就這麼做了 👍


## Call for Proposal and Review
### 做得不錯可以繼續
* 在售票前就完成審稿且公布
> [name=tai] 如果公佈之後買票邀請碼就能出去更好

### 做得不夠好，也許可以改善
* 議程表公布時間有點拖到（google sheet 用得有點久），最後一週才上到網站（開發組人力不足 QQ）
* 今年審稿的各個階段沒有留空，造成作業時間過短，CFP 結束 / 第一階段審稿 / 修改階段 中間都需要留作業時間
* **修改階段開始前要 backup db**，不然審稿委員會看不到兩次修改階段的 diff
* 可以提醒投稿者怎麼看審稿評論
    * ![](https://i.imgur.com/bkev1z0.png)
* 排序功能
    * 排序 by 主題

### 也許明年可以嘗試
* 審查系統的審稿者是否要清空？ (p.s. 新增一名黑名單) 
    * 需要嗎？
        * Winnie 說不要，每年要加有點麻煩
* 可以加入 First Time Speaker 的選項
    * 審稿委員要看得到嗎？
        * Winnie 說可以看，沒差啦
        * Pochun 說第二階段再給審稿委員看 （好像不錯）
        * 可能是給審稿委員一個hint要再給他多點建議
            * 那審稿委員第一階段就要看得到
* 投稿 mentor 計畫？ from [PyCon US 2020](https://us.pycon.org/2020/speaking/talks/)
    * 就看明年的人力
    * Mentor 完還是沒上怎麼辦
        * 沒辦法啊 XDDDD
    * 這件事好像可以拿來宣傳哦！ by Winnie
        * 說不定會增加投稿量 by Wei
    * TP: 沒有人ＱＱ
* 是否要讓審稿委員針對其專長領域進行審查（suggestion from Tai）
    * 委員是我們找來的  我們大概知道對方背景、是什麼專家
        1. 可以放進
            * group_reviewer_generic
            * group_reviewer_packaging
            * group_reviewer_science 
            * 之類的  （一個人可以屬於多個 group）
    * 屬於某些 group 的人會預設只能看到某些類別的稿件要審
    * 有兩個配套
        1. 作法跟往年一樣，但在資料庫另外 associate 投票人的專業背景
        2. 不只是只能看到某些類別的稿件，也會根據「被審稿數」亂數(?)丟一下審比較少的出來給審稿委員
* category based 的投稿可能不太好分辨，可以改成 tag based
    * 不用理投稿者亂 tag ，審稿者會審核
    * 這好像也會上一項審稿委員的分類審稿更複雜
    * 使用者可以自己加 tag 嗎？
    * Winnie 說沒問題 👍
    * Tom -> 參考wordpress 的做法
        * TP聽起來會大爆炸


## Sprint
### 做得不錯可以繼續
* 今年人數、氣氛都不錯
    * 可能是因為是假日？

### 做得不夠好，也許可以改善
* 給講者建議的介紹時間 e.g., 5~10分鐘

### 也許明年可以嘗試
* Sprint 可能拉贊助商嗎？
    * 贊助商自己來帶開源專案？ e.g., InfuseAI
    * ＴＰ：但好像要保證有人要去 sprint 

## Tutorial
### 做得不錯可以繼續
* 大爆滿，順利！
* 以 plotly 那場來說，一個小時半的長度還算順利

### 做得不夠好，也許可以改善
* 便當不夠，可能有人沒登記但有拿
* 沒看 kktix 票，導致座位不夠
* 錄影有部分沒錄到，meet 沒開到聲音
    * 今年是第一次錄影，大突破了
* 有人沒報到過來，滿臉不爽，叫我們寫檢討，所以我就多列這項 (by Windfred)
* 很多人沒注意到要報名
    * 官網設計或許可以多強調 Tutorial 報名連結與文字
        * 今年沒放kktix連結
    * 行前信該段或可粗體字標醒目一點
* 講者簡報有點晚給，所以有點跟不上
    * 明年提醒講者提早放簡報
* 原本的 tutorial 只有組長審核
    * 明年可以早一點決定哪群人來討論審核 tutorial

### 也許明年可以嘗試
* 也許可以嘗試不要辦 tutorial （笑），我們可以重新反思一下為什麼要辦 tutorial
    * 今年有爆滿，那應該就是有需求
    * 有人就是希望有循序漸進的手把手教學 -> for junior


## Lightning Talk
### 做得不錯可以繼續

### 做得不夠好，也許可以改善
 * Day 1 沒有 check 到閃電罐設備，以及交接社群軌閃電講方式給註冊櫃檯志工
     * 活動流程有點沒設計足（特別是閃電講）
 * 宣傳不夠
     * 今年只有 Opening / Closing ， 2019 好像有一直收到消息

### 也許明年可以嘗試
* 租扭蛋機來抽！

## Open Space
### 做得不錯可以繼續

### 做得不夠好，也許可以改善
* Open Space 參與率低
    * 明年或許可以改全天 加 固定時段 兩種形式一起進行 (Wei seconds this idea)
        * Joe: 這個時段後面要安排重要事件（e.g., keynote）
        * 這個同時也能幫助到贊助商攤位
    * Winnie 表示去年有 Open Space 獨立時段還不錯
* 每一桌的主題有點不容易發現
    * Open Space 的牌子要能立起來，大家才看得到
* Open Space 的列表不明確，大家會找不到，可以再宣傳
    * 今年好像只有在行前信
    * 可以用一個大白板來記錄（e.g., 中研院大白板）

### 也許明年可以嘗試


## Host
### 做得不錯可以繼續
* 遠端講者有 rehearsal 到
* 主持人指南很完整

### 做得不夠好，也許可以改善
* 遠端主持人/助理主持人應該要在跟遠端 rehearsal 過之前，先在內部 rehearsal
* 一般主持人/助理主持人也應該 rehearsal 順過流程（可以在場佈當天）
* 一個主持人至少要連續兩場會比較好 (或是休息時間長一點?)
* 遠端議程中，如果下一場議程的講者提前加入 meet 會有提示訊息，干擾到上一場的講者
   * 另外開一台主持人的機子，負責控管加入的人
       * 打直播的機器是另一個被主持人邀請的帳號
       * 或者一台機子開兩個不同帳號的tab
   * or 遠端講者的每一個 meet 應該要是不同的
* 主持人班表表單要再更直覺
    * 相關資訊要能夠容易被找到
* 主持人可以先跟講者稍微聯絡（e.g., send a mail or 講者晚宴）
* 應該建立一個主持人的專用群組，可以讓主持人協助公告事項給各個議程
    * 今年有做，但做的成效不太好，可能原因是當天或前一天才創好這個群組

### 也許明年可以嘗試


## Chair
### 做得不錯可以繼續
* 有比較清楚地列出議程組各個任務要做什麼

### 做得不夠好，也許可以改善
* 不夠明確將任務授權給組員 / squad leader，導致最後大家都要找組長再確認
* 分散成幾個 squad leader
    * Keynote Speaker
    * 宣傳（e.g., post, 網站更新）
    * 一般演講 and CFP
        * Host
    * Other Event (including tutorial?)
* 即使是朋友 or 朋友推薦來的志工，也應該多花點時間聊過，確認彼此在合作上的認知是相同的
* 過度依賴大會月會，沒有例行組會，讓大家更認識彼此
    * [name=Wei] 我懶，我道歉ＱＱ 明年不會惹
    * Winnie -> 任務性聚會
        * 也可以各個小組的 leader 約，約共同時間討論吃飯，增加歸屬感

### 也許明年可以嘗試
* COSCUP 的志工指南跟志工招募文件超完整，可以參考他們
    * [COSCUP 議程組的 guide ](/@coscup/SJGfnJVmU#%E5%9F%BA%E8%AA%BF%EF%BC%9A%E7%A4%BE%E7%BE%A4%E5%8D%B3-COSCUP)超完整
    * 更明確的志工徵求指南 👉 [COSCUP 2020 徵求議程組志工](/@bobchao/HkrexKSWL)


## On Conference Day
### 做得不錯可以繼續

### 做得不夠好，也許可以改善
* 會議當天需要開場前主持人
    * e.g., before opening
* 每一場演講應該安排一位知道狀況的組員場控
* 會議前一天場佈要留議程組組員協助
* opass 公告觸及率低
    * 中研院大會廣播的可能？
    * 場務組拿大聲公指引 <- Winnie 表示非常同意 xDDD
        * 不行！太吵了！ by 多位前主席們xD
* Discord 使用率低
    * 也許可以以一整年的 scale 來規劃讓大家加入？
    * 內部溝通也是有沒注意到的
        * 因為今年原本是用 telegram，非戰之罪
 
### 也許明年可以嘗試


## Financial Aid
### 做得不錯可以繼續
* 有做志工用的問卷
    * 不過好像還是有志工填到對外的（也可能志工問卷晚出）

### 做得不夠好，也許可以改善
* 門票補助的申請方式不明確，表單中只有問旅行費用
* 申請表單應該跟審核表單格式一致，最好能自動化
* 志工申請住宿跟補助原則要切分開來
    * i.e. 何謂因特殊任務可以直接取得住宿，以外的才算是要額外申請審核的
* 沒啥人填 社群補助表單
    * 明年申請表單上面可以順便放 電話, 職業，以及願意提供資料給廠商與否

### 也許明年可以嘗試
* 把 Financial Aid Committee 從議程組拆出去...







十週年慶貼紙簿

----

- 