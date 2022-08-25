---
title: 使用 Python 實現可即時互動用的遠端影音傳輸 - Milo Chen
tags: PyConTW2021, 2021-organize, 2021-共筆
---

# 使用 Python 實現可即時互動用的遠端影音傳輸 - Milo Chen

{%hackmd f0JLCtZCTiWo4ZBRNKd8cg %}

<iframe src="https://app.sli.do/event/hpzyw9em" height=450 width=100%></iframe>

<iframe src="https://wall.sli.do/event/hpzyw9em?section=055b9fda-c0ed-4c6e-9704-7ade7ddcb0e2" height=450 width=100%></iframe>

> 從這裡開始共筆

###### tags: `PyConTW2021`

[投影片連結](https://www.canva.com/design/DAEkk9XLz7s/i0___crEfNFA3J0WXT3p1Q/view#1)

## QA
- Q: How's the performance look like?

- Q: WebRTC傳輸本身支援adaptive bitrate streaming嗎？還是這是上層要自行要實作？
	- 只要套用web RTC，bitrate就會幫忙處理這個部分
- Q: aioRTC有串接上opencv使用, 請問那能夠串接上自己實作的影像處理模組嗎?
	-  可以，這是沒問題的
