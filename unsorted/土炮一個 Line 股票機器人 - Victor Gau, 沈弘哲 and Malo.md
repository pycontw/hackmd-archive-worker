# 土炮一個 Line 股票機器人 - Victor Gau, 沈弘哲 and Malo

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}

[toc]

[Github Repo](https://github.com/victorgau/PyConTW2018Talk)

## Linebot tutorials(上) - 沈弘哲

### Line bot - Python + Flask
 * Flask: 組裝電腦
 * Django: 套裝電腦

### 開始動手建立Linebot
 1. 註冊Line
 2. Line bot會自動加入自己好友
 3. 打開webhook
 4. Deploy到Heroku（自帶HTTPS）
 5. 進入line bot api設定介面設定hook url

### ngrok
 * 讓localhost可以讓其他人看到
 
## 土炮Line股票機器人(下) - Victor
 * Crawler (twstock)
 * Using pandas to analysis data
 * Adopt matplotlib to plot out charts.

### 如何顯示圖形在Line上
 * Line <- Messaging API -> heroku 
 * Heroku -> imgur 取得圖形link
 * heroku send out the message with link

### Demo



###### tags: `pycontw2018`
