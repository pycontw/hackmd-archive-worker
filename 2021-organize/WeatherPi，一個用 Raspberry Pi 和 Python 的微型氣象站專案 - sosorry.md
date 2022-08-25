---
title: WeatherPi，一個用 Raspberry Pi 和 Python 的微型氣象站專案 - sosorry
tags: PyConTW2021, 2021-organize, 2021-共筆
---

# WeatherPi，一個用 Raspberry Pi 和 Python 的微型氣象站專案 - sosorry

{%hackmd f0JLCtZCTiWo4ZBRNKd8cg %}

<iframe src="https://app.sli.do/event/vahxkdfe" height=450 width=100%></iframe>

<iframe src="https://wall.sli.do/event/vahxkdfe?section=180f3467-1a46-437e-b825-e264aa434a19" height=450 width=100%></iframe>

> 從這開始共筆

投影片：http://bit.ly/3l3XLg2



問題討論：
問題1.好奇會不會和政府的開源資料做比較 譬如說量到的雨量的差值
> 各地方(物理)的資料本來就會略有差異，比如台北的士林下雨但台北車站沒下雨。

問題2.請問一下 Dash + Plotly 怎麼做 real-time 的資料顯示？... 怎麼讓網頁端不斷自動更新顯示的資料點？...
> 比如說這個範例
> https://www.geeksforgeeks.org/plot-live-graphs-using-python-dash-and-plotly/
> 在抓資料部份，可以用 MQTT 去 subscribe 後顯示

問題3.Python套件部分選擇後面兩個好像有點衝突
> 一開始是用 GPIO，但有準確性等問題，所以改用 pySerial
> 但使用 pySerial 同時只能讀取一組 UART，所以最後是選擇用 pigpiod 同時讀取 APRS 和 GPS

問題4.想知道利用樹梅派測到的資料，是已經實際運用在農作上了嗎？還是仍處在 prototype 的狀態？那從資料視覺化到實際運用在農民身上的週期大概是多久？
> 目前還在 prototype 做資料蒐集和顯示，後面資料視覺化只有簡單的儀表板顯示。期待未來和其他人的合作把這專案做更完整。








###### tags: `PyConTW2021`