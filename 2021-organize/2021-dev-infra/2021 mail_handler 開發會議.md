---
title: '2021 mail_handler 開發會議'
tags: 2021-dev-infra, 2021-organize
disqus: hackmd
---
🔙 [PyCon TW 2021 Organizing 共筆](/Wb9vQrfJQk-5tPoPR23hwA)
🔙 [PyCon TW 2021 dev-infra 主頁](/@pycontw/Bkp2vRQEu)

# 2021 mail_handler 開發會議

[TOC]

---

## Online Meeting -- mail_handler (05/15/2021)
:::info
-  **Link: https://meet.google.com/qpd-tgax-qpz** 
-  **Date:** 21:00 May 15, 2021(TST) 
-  **Agenda:**
- **Online Participants:**
    - qazws
    - yucheng
    - josix
    - tai
::: 

### Action
- 確認今年的行前信負責進行是由哪邊負責，若使用 mailchimp 如何避諞權限問題，或是其他做法(e.g. mailchimp api)，是否需要需要寄信組別整合？ - Josix
- csv to json 開發及 review, testing - Jacky
- 測試含縮網址內容的信件 - Jacky
- 寫 Jinja File formating 的教學文件(format, coloring 功能) - Infra Team
### Discussion
- Jacky
- [name=josix] tom 對其他服務與平台的 comment https://discord.com/channels/752904426057892052/833237740979355672/838458066608455700
    - 行前信使用 Mailchimp
        - Permission Problem
- [name=yucheng] 去年經驗懷疑信件內容中有縮網址的話，似乎比較容易進垃圾信


## Online Meeting -- mail_handler (04/21/2021)
:::info
-  **Link: https://meet.google.com/joo-wqns-svr** 
-  **Date:** 21:00 Apr 21, 2021(TST) 
-  **Agenda:**
    -  Registration team demand discussion (假如有註冊組或相關的大大參加)
        -  還需要哪些 j2 TMP
        -  需要將文字檔轉成 j2 TMP的程式
    -  mail_handler會不會有進到spam的問題
        -  [name=Wei Lee] 應該會吧xDDDD
        -  [name=allen] 有補充 google 判定 spam 的網頁到  issue
        -  [name=tai] 基本上是用個人信箱發，所以會進 spam 的話跟手動用自己帳號發我覺得應該是差不多的標準
    -  接 KKTIX 的隨機驗證碼程式
        - KKTIX驗證碼格式
        - 另外寫接完output成json
    - 程式問題請教
        - tasks file功用
            - [name=Wei Lee]
                - 管理繁瑣的指令
                - 更簡單的理解就是 Python 版的 Makefile
                - 詳細一點點的理解可以參考 [https://lee-w.github.io/posts/tech/2020/02/python-table-manners-manage-trival-tasks/](https://lee-w.github.io/posts/tech/2020/02/python-table-manners-manage-trival-tasks/)
        - 如何開發成用CLI執行 render.../send...
            - [name=Wei Lee] 現在其實已經是了，如果要問怎麼做到的，可以參考 https://github.com/pycontw/mail_handler/blob/master/pyproject.toml#L72
- **Online Participants:**
    - Josix
    - Wei
    - Allen
    - tai
    - Jacky
    - Yucheng
    - GTB
- **Next Meeting**
    > https://meet.google.com/qpd-tgax-qpz
    > [time=Wed, May 14, 2021 9:00 PM]
::: 

- [name=tai]
    - 如果需要註冊組 input，可能要事先詢問他們意見，或是邀請他們參加
    - 我認知中註冊組應該不是重度使用者， kktix 的票務系統有自己的 mailing tool
        - 最大的使用族群應該是議程和行銷（特別是贊助執行）
    - 我沒跟到 KKTIX 的驗證碼一事；所以有需求想要串 KKTIX 的服務是嗎？
- [name=JackyLi]
    - 那我再請Josix學長幫我聯絡可能會有需求的組
    - 對，看能不能再發信時帶入邀請碼或驗證碼，但目前不太確定kktix那邊能不能串
    - 
        - [name=tai] 我不太確定這邊的邀請碼和驗證碼是幹麻用的？但如果是 kktix 票卷資訊本身的話，已經用 mailchimp 串好囉，這幾年都是用同一套在做的
    - [name=allen] 我記得註冊組主要是需要產生驗證碼的 tool (kktix沒有自動產生的功能?!)
    - [name=Yucheng] KKTIX 有產出驗證碼(邀請碼)的功能，但是發信功能 ~~堪憂~~ 不符合我們使用 ，我們比較需要的就是有  Template 功能，並且能群發信件。

| NickName | Mail | TicketType | InvitationCode| ExpiryDate | 
| ---  | --- | --- | --- | ---| 
| Yucheng | tyuchx@gmail.com | 特殊票 | 3a3a4b5b6c | 2021-04-01 |

### Action

 - 開發 mail_handler 可以吃 csv - 開發組 Jacky 5/14(五)
 - mail_handler 使用教學 - 開發組 5/E
 - 寫 Jinja File formating 的教學文件(format, coloring 功能) - Jacky
 - 找 Tom 確認行前信 mailchimp 使用需求  - Josix 5/7 (五)
     - https://discord.com/channels/752904426057892052/833237740979355672/838457612479234066
 - 需要壓測看有沒有信件會進 Spam 每次寄件數量可能是原因 - Jacky 5/14(五)
    - https://www.mail-tester.com/
    - 信件含縮網址測試


### Discussion
- 註冊、開發組需求
    - template 可以由註冊組或議程組等有需要發信需求的組別維護
    - 串 API、寄出功能由開發負責
    - 開發組行前信 mailchimp 服務可以整合進 mail_handler 或是將其 script 放上 github (Mailchimp 相關需求 @Josix 再找 Tom 詢問)
    - 需要研究一下 mailchimp 及其他第三方寄信商的免費方案
    - 會上郵件是否能產生一次性密碼
    - 可將 RECEIVER_DATA 更新為接受 csv 格式



- 註冊組邀請信件 template
```信件 Template
Title: PyCon Taiwan 2021 Registration

send to: {{Mail}}
cc: {{RegistrationTeamMail}}

Hi {{NickName}},

感謝您今年貢獻 PyCon Taiwan 2021

您可以透過下列網址和邀請碼，完成門票註冊：

請到網址 https://bit.ly/pycontw2021-reserved

移到頁面最下方選擇「{{TicketType}}」

邀請碼使用 {{InvitationCode}}

注意: 有效期限 {{ExpiryDate}}

若有遇到問題，請跟我們聯絡。

PyCon Taiwan 2021 註冊組
```

- how to use invoke?
    - example project: https://github.com/pycontw/pycontw-postevent-report-generator
