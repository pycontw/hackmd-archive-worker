---
titles: 隨買即用系統 (購票流程自動化) Pitch
tags: 2022-registration,registration
---

# 隨買即用系統 (購票流程自動化) - (RFC) Phase1

本 spec 是用 [ShapeUp principle](https://www.prodify.group/blog/book-report-5-key-takeaways-from-shape-up-by-basecamps-ryan-singer) from BaseCamp 寫的

# Problem

1. 花人工：進入 Gather town 聽演講需要拿到 invitation link, 而目前的流程是需要 `人工` 匯入 kktix 的售票紀錄後，才能送 invitation link 的 email 給 user
2. Cannot maximize our revenue: 因為需要人工寄信給他，所以我們過去會提前截止，讓人類有時間能寄信給會眾

本次專案的目標，是希望能讓收到 gather town 等 invitation link 的流程自動化，做到隨買即用。

# Appetite

(解釋一下，ShapeUp 的原則是根據時間 time frame 決定我們能實作多少功能，而不是想做多少功能去預估要做多久；Spec 服務時間，而不是時間服務Spec )

`21 days` 希望七月底 ship to prod

# Solution

~~~mermaid
flowchart LR
	Extractor --> Transformer
    Transformer --> Loader
    Loader --> Aggregator(Data Warehouse)
    Aggregator(Data Warehouse) --> Authorizer(Authorizer e.g. Gather Town or YouTube)
    Authorizer --> Email
~~~

In short, 這是個 data pipeline. 可以用任何語言任何框架去實作，框架部分如 Airflow or crontab 都行，只要能每五分鐘或 semi-realtime 的把最新的 kktix event 吃進來都蠻理想的。

* Extractor:
    * https://docs.google.com/document/d/1OOtG_2SagCR7ZJRquVJZCNpGXPgHTH9Hc0D2Uj6b4gw/edit
    * 可以挑任意的服務實作，如 Airflow or crontab 都行，只要能每五分鐘或 semi-realtime 的把最新的 kktix event 吃進來都蠻理想的
    * 這邊要敲 GTB 特製的 KKTIX API 去拿資料
* Transformer: need to de-identify, 用 sha256 to hash user's email should be enough
* Loader: there's many BigQuery python SDK allowing us to load data to BigQuery [ref](https://cloud.google.com/bigquery/docs/reference/libraries)
* Data Warehouse: Destination for these kktix raw data should be (根據資料類型決定送到哪個 table):
    1. `pycontw-225217.ods.ods_kktix_ticket_corporate_attendees`
    2. `pycontw-225217.ods.ods_kktix_ticket_individual_attendees`
    3. `pycontw-225217.ods.ods_kktix_ticket_reserved_attendees`
* Authorizer:
    1. Gather Town: TBD（完全不知道這邊怎麼加白名單然後產生 invitation link）
        * Angus: REF: https://www.notion.so/Gather-HTTP-API-3bbf6c59325f40aca7ef5ce14c677444
        * 加白名單 Test Code: `curl  -d '{"spaceId":"VUJexktI2UhoGaun\\FunFunPython", "apiKey":"B5eJhwMx3eapRpeP","guestlist":{"googolangus@gmail.com":{"name":"angus","role":"guest","affiliation":"pyguest"}}}' -H "Content-Type: application/json" -X POST "https://gather.town/api/setEmailGuestlist"`
        * Invitation Link: 應該直接提供Gather Town 空間網址即可, GatherTown whitelist 的認證方式是登入時產生一組確認碼e-mail到註冊的address, 用該確認碼登入. REF: https://support.gather.town/help/restrict-access#guest-list-only-access
    2. Youtube: 直接給 private link
* Email:
    * main logic is as follow: :point_down: 
        1. create template
        2. create a list （list 是一群已購票用戶的 email 列表）
        3. create campaign
        4. send or schedule this campaign
    * 用 Klaviyo API 去寄信，請不要使用自幹的 SMTP 發 Email 給 user，缺點是自幹的話無法追蹤開信率、點擊率等等，但付錢給 ESP 的話這些數據都追得到，能讓我們更好的了解銷售漏斗（詳請請查 Sales Funnel, Marketing Funnel）

# Rabbit Holes

1. Airflow infra 可能不穩定，如果掛了資料就會 delay 而且目前沒有 uptime monitoring service 會通知我們他掛了
2. Authorizer: Gather Town 的 API 不知道誰熟
3. ESP: 不知道我們決定買哪一家，那一家的 API 可能沒人研究過不知道怎麼 post（不過理論上他們的 document 不會寫太爛才對）
我用過mailgun, API簡單好用, 前5000封信免費 (by [name=derick])
KKTIX 也是用 mailgun，之前也有請弘哲研究 (by [name=GTB])

# No Gos

correct me if I'm wrong, 但看起來最緊急的是自動寄 email 給 user, discord command 是 nice to have

# Scopes

- [x] Extractor @davidtnfsh 
    - [x] KKTIX API @yfRGNNkIRbuSG29WjF3SdQ 
- [x] Transformer @davidtnfsh
    - [x] Making sure we use SHA256 to de-identify their email and name
- [x] Loader @davidtnfsh 
    - [x] load de-identified data into `ods` bq dataset
    - [x] installed bq SDK
- [x] Data Warehouse @davidtnfsh 
    - [x] making sure data is available in BQ dataset
- [ ] Authorizer
    - [ ] do some research about how to whitelist emails in Gather Town
    - [ ] 應該會拿到 unique 的 GatherTown invite link(?)
- [ ] Email
    - [ ] 研究 ESP
    - [ ] 或是用 SMTP 自幹

# Gather Town API document
https://www.notion.so/Gather-HTTP-API-3bbf6c59325f40aca7ef5ce14c677444#3c526203a2d543879841dae77dbe3ed5

set guest email example
https://forum.gather.town/t/is-https-gather-town-api-setemailguestlist-supposed-to-set-a-users-role/101

# Reference

https://hackmd.io/TqAet6zNTTifRa4wzE__RA?view