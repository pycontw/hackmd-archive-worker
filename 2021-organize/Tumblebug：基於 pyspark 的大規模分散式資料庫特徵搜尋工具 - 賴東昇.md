---
title: Tumblebug：基於 pyspark 的大規模分散式資料庫特徵搜尋工具 - 賴東昇 
tags: PyConTW2021, 2021-organize, 2021-共筆
---

# Tumblebug：基於 pyspark 的大規模分散式資料庫特徵搜尋工具 - 賴東昇

{%hackmd f0JLCtZCTiWo4ZBRNKd8cg %}

<iframe src="https://app.sli.do/event/mrtlhg9d" height=450 width=100%></iframe>

<iframe src="https://wall.sli.do/event/mrtlhg9d?section=43b339de-bf59-4af8-a0ef-13bece3b45c9" height=450 width=100%></iframe>

> 從這裡開始共筆

###### tags: `PyConTW2021`

- Q: 對於Tumblebug能夠找出不常使用的特徵 可能的原因為何?
    - 公司的資料算是蠻多的，有些是大家平時不會使用的，透過這些資料可以找出一些不常使用的特徵

- Q: 想請教三個模組在串接上 是不是需要符合一定的資料格式 若資料的格式與預先設置的不同即無法進行
    - 先從第一個到第二個模組，只要資料表跟資料欄位的名稱對的上，拿得到想要的統計量，那就沒問題
    - 第二個到第三個模組之間，第二個模組比較像是建模，第三個模組比較像是用這個模型對資料表進行轉換，只要最後第二階段輸出的是一個特徵的列表，就可以針對該列表生成可以使用的資料表，進行後續的建模

- Q: 在分散式系統使用Spark，還可以再使用multi-threading嗎? 不會造成問題嗎?
    - 有針對使用到 multi-threading 的地方進行測試，發現速度有明顯的改善，當然這還要看 config, 硬體之類的部分，但是在測試的專案上是沒問題的
