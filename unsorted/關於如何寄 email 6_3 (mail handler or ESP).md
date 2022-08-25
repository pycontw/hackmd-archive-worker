---
titles: 隨買即用系統 (購票流程自動化)
tags: 2022-registration,registration
---

# 關於如何寄 email 6/3 (mail handler or ESP)

1. context: 現有的 mail handler repo: https://github.com/pycontw/mail_handler
2. 市面上排名前幾的 ESP: Klaviyo, Mailchimp

# Agenda

1. Align individual, team and organizational goals
    1. individual
    2. team:
        1. 註冊：能發出行前信，並能透過 cmd 化執行，能吃 html 並不是單一寄送純文字（希望各背景的志工都能操作）
        2. 廣告：希望能測到開信率、CVR 等數據，像行銷信的場景就需要這些不然無法優化
        3. 贊助組：
    3. organizational：
        1. DJ: 純猜測，但我覺得組織會喜歡一個所有志工都能“寄信”的 solution，而不是有工程師背景才能操作的 solution
        2. GTB: 各背景都能寄信 + 支援 subscription（行銷租） 的 email 服務
2. pros and cons:
    1. mail handler:
        1. yucheng
        2. GTB: 就目前行前信來說功能算是足夠
        3. lee wei：目前行前信足夠，cons 就是廣告數據收不到
        4. DJ: 已經做了 mail handler 不用有點可惜QQ + 要花錢
        5. Li-Ying: 目前已在使用並運作OK，不用花錢
        6. [name=弘哲]: 整理沒甚麼問題, 但是缺點可能是會變成垃圾信件.
    2. ESP:
        1. yucheng
        2. GTB:
        	* props: 可以跟 ocf 談論 domain 的問題，並且可以做 DKIM 設定，減少被歸類在垃圾信的問題
        	* cons: 擔心會有額外開銷，我最初有請 [name=弘哲] 研究 mailgun(只有前5千封免費, 前3個月)
        4. lee wei：ESP 今年來不及、沒有人力；優點部分是行銷確實需要
        5. DJ:
            * pros: 最近要記得行銷信，就需要 ESP 才知道行銷的如何。ESP 已經是“成熟”的 SAAS, 他們提供其他如開信率、開信後 CTR, CVR 等等 tracking 是我們很難做的，如果沒有這些數據，是無從優化我們的 sales funnel 的。
            * cons: HTML 不夠 customized，不像手刻 html 那麼自由
        7. Li-Ying:
            * pros: 外包減少維護成本、feature多
            * cons: 同上，customized 問題
4. win-win solution:
    1. GTB: 不談錢，用 ESP 就可以解決所有的需求，我們也不用煩惱
    2. DJ: 並存，註冊信用 mail handler,行銷或其他信用 ESP 寄。缺點就是並存會讓我們的 SOP 變複雜，可能增加出錯機率。
5. 錢的預估： 寄信當月最多花 $150 (用七千封去算)，2021 的數據只記了 1000封，要 $30
7. Conclusions:
    1. 保底輸出用 mail_handler 寄註冊信
    2. 得去確定預算
    3. DJ 或 data team 去研究 ESP，如果可以的話註冊信跟行銷信就可以用 ESP 的 solution
9. AIs
    1. 確定預算能不能用四千塊以下的預算去做
    2. DJ 或 data team 去研究 ESP，如果可以的話註冊信跟行銷信就可以用 ESP 的 solution

### 結論

* [name=yucheng] 不要用 mail hander，使用 [name=derick] 做的 Template，用 mailgun 寄信，使用 mailgun 的 Metric 去收集行銷數據。

### price

Mailgun 
![](https://i.imgur.com/UPFLAgp.png)


----

## 過去相關的討論

https://hackmd.io/ycDd_ZTYT5uCTQa7H9OmnA?view

> Matt Wang — 08/31/2021
> 往年行前信中是用 mailchimp 批量發送，但根據去年開發組長描述 [1]，要做 email 的 styling & 排版是非常困難的事情（可參考過去兩年的 code [2][3]），不過為了能看開信率之類的好處可能不會變換工具。
> 
> 因為蒐集行前信內容需要不斷與各組聯繫，去年會期檢討會上才決定將這個任務交給 Joe & PR team，但我不確定目前負責行前信的大家還有沒有心力處理實作成 email template & 批量發送。如果這部分是希望讓 web & infra team 幫忙的話，也需要留一點時間給我們研究（過去兩年幫忙行前信的志工今年剛好都不在開發組內）。
> 
> [1]: https://discord.com/channels/752904426057892052/833237740979355672/838457612479234066
> [2]: https://github.com/pycontw/PyConTW2020-mail
> [3]: https://github.com/pycontw/PyConTW2019-email


> Josix — 04/30/2021
> Hello @yychen, 想要來請教這兩年行前信相關的流程看看能不能夠做些自動化改善它：
> 
> 1. 首先想先確認我們目前有沒有寄出行前信相關流程的文件可以參考?
> 2. 另外想問目前有使用到 mailchimp 的功能有哪些，不確定有哪些需求是有必要可以合併到 mail handler 進行的？我想可以的話應該是可以減少額外使用其他服務的維護成本
> 
> mail handler 目前可以透過寫 jinja2 template 達到自定義的信件範本（目前還未包含樣式），給定 JSON 定義寄件者、收件者郵件位置、信件主旨等變數，可以渲染郵件自動寄出信件。 cc @tai271828 @Matt Wang @jneo8 


> yychen — 05/03/2021
> 應該是這一篇 https://hackmd.io/oYkOPj57TDWLIffOtPLi2w
> 使用 mailchimp 的重點應該是在於，我們會把 KKTIX 的名單匯出之後，匯入 mailchimp，然後由 mailchimp 的名單發信
> mailchimp 最大的好處應該是在於他的排版... email 排版是一件非常夭壽的事情
> mailchimp 已經有 editor 幫你把事情都弄好了... 所以把最麻煩的事情交給他... 一切就簡單
> 
> 當然，有另外一種做法，就是用 mailchimp 把排版都弄好之後，把 html 挖出來然後用 mailgun 或其他東西發送
> 這樣也是可以的
> 喔 mailchimp 還有另一個好處是他有埋東西.... 所以你可以看開信率、bounce rate ... 等等
> 這些人家已經造好的輪子就可以不用再造... 但如果輪子規格不符合，硬要用轉接環也是頗麻煩的... 就可以看你們怎麼考量了
> 我覺得 email 寄信最複雜的應該就是信件本身的 html/style 了... email 跟網頁完全不一樣，完全是另外一個世界
> 有些 mail client 像瀏覽器行為類似 (你可以考量到 thunderbird / outlook)... 有些則是包在網頁裡頭 (所有的 webmail like gmail, yahoo, outlook.com)
> 以及那些你不太確定 behavior 到底是如何的 (ios/mac mail.app, android gmail)
> 所以 css style 都不太能夠使用，然後通常 email 都是使用 table 切版
> media query 不好說，不一定每個都可以吃進去
> 所以你需要有特殊工具去把 css style 全部弄成 inline 的 (或者是現在相容性已經比較高了我也不太清楚)
> 
> anyway, 這些恐怖的事情也有可能你們早就知道了...
> so........ 我的作法就是 -> 讓 mailchimp 去搞定這一切 XDD
> 然後 email 可能要有兩個版本, text/html 跟 text/plain，讓那些無法讀取 rich text 的 client 也看得到你的信 (那些 linux 上的 mail client (?))
> 
> tai271828 — 05/03/2021
> 這樣聽起來，在某些情境下，其實可能反璞歸真使用 plain text 反而可以繞掉最難的地方 (css/html）；開信率等資料的確很有趣，如果 pycontw 志工執行能量可以高到真的有能力去追蹤與利用這類資訊的話才能真的派上用場。  uhmmm..... 
> 

### mailchimp 被買走了

https://twitter.com/axios/status/1437515671223537669?s=20
