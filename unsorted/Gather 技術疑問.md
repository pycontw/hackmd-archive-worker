---
tags : PyCon2021-Program
---
🔙 Back to [歷年 PyCon TW Organizing 共筆](/ryPr7SFyP/%2FHM5mHCFKQCu7-W5ea8ITcw%3Fview)
🔙 Back to [PyCon TW 2021 Organizing 共筆](/Wb9vQrfJQk-5tPoPR23hwA)


# Gather 技術疑問



## 技術疑問


### 限制
- [x] 單一 Space 是否有面積限制？
    - 有，怕影響效能
- [x] Metropolis Private Space(對話空間) 是否有數目上限？
    - 沒有
- [ ] 建議的連線上限？(壓力測試)
    - e.g. 1 min 內加入 Space 人數小於 100 人

- [x] 付費時間到，空間內的人超過會生什麼事？
    - 會切成比較弱的 server，不會斷線
    - 平常沒付費時，人數超過也不會禁止對方連線或跳警告，只是空間可能會不穩


### 功能細節

- [ ] 關於 [API: GET https://gather.town/api/getMap](https://www.notion.so/EXTERNAL-Gather-http-API-3bbf6c59325f40aca7ef5ce14c677444) 回傳內容的細節
    - 此 API 是否能取得即時會場人數？
        - [name=jordan] 測了一下應該是無法，它只有回傳地圖建置的細節而已


### 特殊功能疑問

- [x] ~~是否有可能為每個用戶提供唯一的邀請連結？ 或者建議的方式？~~
    - ![](https://i.imgur.com/HUMmWGZ.png =200x)
    - 目前此功能發送的網址皆相同
    - `用 email 白名單 可達成類似目標`

- [x] ~~是否有批次調整用戶權限的功能，或者建議的方式？~~
    - ![](https://i.imgur.com/hBhOLDs.png)
    - 似乎可透過 [API: POST  https://gather.town/api/setEmailGuestlist](https://www.notion.so/EXTERNAL-Gather-http-API-3bbf6c59325f40aca7ef5ce14c677444) 達成
    - 或是上傳email white list，同時也可以設定名稱、角色（非space權限）、註解等，見 [Guest Only Access](https://support.gather.town/help/space-access-permissions)


- [x] 是否有機會調慢用戶走路速度？(有時走路會瞬移）
    - 不行
