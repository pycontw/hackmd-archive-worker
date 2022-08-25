# CBFHSS 專為高中生設計的管家型聊天機器人 - 廖煥杰

{%hackmd JgQsr94hSFK427iUDWF9NQ %}
:::warning
Slido 連結: https://app.sli.do/event/33v4ivaj/
:::
> 從這開始
> 
## 功能
- 推播訊息給使用者，提醒使用者明天要帶的作業、考試、段考資訊等
- 限制：google sheet API rate limit(100req/100s)
- 體溫登記
- 放學推播
- 資安防護處理：18歲以下個資（採用 TWCC 內網連接 DB）

## tools
- py3
- django
- vscode
- heroku
- mysql

## Q&A
1. message API 限制：每班一個 channel，看看學校是否有補助
2. 學生亂傳訊息：後台權限管理，只接受特定指令

###### tags: `PyConTW2020`
