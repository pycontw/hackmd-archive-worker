---
title: 從 Flask 邁向 FastAPI 的心路歷程 - 用房屋估價模型服務體驗急速開發、高效能的快感! - 陳家丞
tags: PyConTW2021, 2021-organize, 2021-共筆
---

# 從 Flask 邁向 FastAPI 的心路歷程 - 用房屋估價模型服務體驗急速開發、高效能的快感! - 陳家丞

{%hackmd f0JLCtZCTiWo4ZBRNKd8cg %}

<iframe src="https://app.sli.do/event/lypoclvj" height=450 width=100%></iframe>

<iframe src="https://wall.sli.do/event/lypoclvj?section=26e2efeb-fcfe-44ee-ae8d-56dff14d3d43" height=450 width=100%></iframe>

> 從這裡開始共筆

###### tags: `PyConTW2021`

### 選擇FastAPI的理由
* 支援Type Hint
* 支援同步與非同步API: WSGI, ASGI
* OPEN API 規範
* 自動生成 api doc

### 業務通點 - 房屋估價流程
* 估價流程繁複，產生斷點
* 玉山e指房貸服務→提供房價試算
* 使用ML方式去優化智能估價模型
* 

### 改造模型的緣由
* 透過cprofile與pyinstrument在運算過程中 multithread_all的時間佔比非常重

### 改造方式
* route 定義方式調整
* api input/output檢查
    * Flask檢查方式繁瑣參數多
    * Flask-Restful檢查方便但功能有限
    * FastAPI整合了pydantic作為檢查方式，更為彈性
* 同步/非同步使用
    * Flask 
        * 同步：run函數等結果
        * 非同步：須加上 async/await字眼
        * multithread_all
            * 省下很多queue消耗
* API Sepc文件
    * Flask必須額外撰寫swagger.json才能產生WebUI網站，容易造成資訊不一致情形
    * FastAPI將api服務啟用後就會即時更新到spec的部分，統一的溝通規格

### 三個套件的比較
* FastAPI
* Flask
* Flask-Restful
![](https://i.imgur.com/AKyHaeF.png)

### 兩個框架的比較
* 單次呼叫上 FastAPI 比 Flask 快一點點
* user/worker數接近時，兩者回應時間差不多
* 資源消耗來看FastAPI在cpu/mem上的消耗的比較少

### 轉換心路歷程
* 同部非同步的注意事項
    * scenario
        * 同步
            * 較少IO bound
            * 執行速度夠快
        * 非同步
            * IO bound較多時
            * CPI bound執行時間佔比過重
        * 地雷：race condition

### [SQL model (ORM)](https://github.com/tiangolo/sqlmodel)