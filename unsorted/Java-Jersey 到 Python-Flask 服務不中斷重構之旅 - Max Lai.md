# Java-Jersey 到 Python-Flask 服務不中斷重構之旅 - Max Lai

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}

## Java-Jersey
類似django + restful

## 簡報
[https://www.slideshare.net/maxcclai/javajersey-pythonflask](https://www.slideshare.net/maxcclai/javajersey-pythonflask)

## Self-introduction
- 台中py, agile
- Jarvish (Jarvis + Helmet)[勸敗?](https://secure.newegg.com.tw/item?itemid=654349&categoryid=473&StoreID=7&utm_campaign=TDG_ShoppingAdsLow&utm_source=TDG_Google&utm_medium=TDG_ShoppingAdsLow)
- 智慧型安全帽
- 打美國市場根alexa做結合


## 專案背景
- 新創公司做 backend 的前人跑掉

```
Redis/MySQL -> Java/Jersey -> Python/Flask
Redis/MySQL ->Scala/Akka
```

- 為什麼從 Java 轉 python ?
  - 就總~~監~~兼只會寫 python，看Java很痛苦
  - 參考 Youtube 用 python 打敗 google video 的故事
      - ref: [Python Interviews: Discussions with Python Experts](https://www.amazon.com/Python-Interviews-Discussions-prolific-programmers/dp/1788399080)

---

## Flask vs Django
- 當時覺得 django 很肥，flask 輕量化
- 初期對 web framework 不夠瞭解，flask 相對親民
  - flask 可以快速做 prototype（當時的能力來看）
  - 老闆曰: 明日可不可以好?

## 什麼是 Restful API (自己wiki lol)

- 一個 GET + jsonify 的範例

| HTTP Method | Action | URL |
| -------- | -------- | -------- |
| GET     | Text     | Text     |

## API in Django

* Django REST Framework is great!
* 其實 flask 也有 flask-restful

## 其他考量

- 需要if-then
- 不需要 template

----

## Flask 匯入 MySqL Schema
- 背景：資料庫不會因為框架換掉而重建 (SQLAlchemy)

## 線上 try 遇到的問題（offline開發沒問題）
```python
(OperationalError)
(2006, 'MySQL server has gone away')
```
- MySQL 會自動關閉連線如果閒置太久（預設8小時）

### 解法1
```python
engine = create_engine(mysql_db_url, pool_recycle=3600)
```
### 解法2
每次查詢之前都測試連線
### 解法3
```python
# SQLAlchemy 1.2版以後
engine = create_engine(mysql_db_url, pool_pre_ping=True)
```

## 文件
- [Swagger](https://swagger.io/) 產生網頁版 API 文件
- API Documentation by Flasgger (Swagger)
- [Demo] (http://flasgger.pythonanywhere.com/)

## 重構
- 在不改變外部行為的前提下，改變內部結構使其更容易修改
- 人力精簡之重構步驟：
    1. 確定要重構的單元
    2. 找出測試點
    3. 編寫測試建立防護網
        - API測試
        - 整合測試
    4. 新的程式碼補上單元測試 
    
## [Tavern](https://taverntesting.github.io/)
- Tavern
    - Python based
    - focus on automated testing
    - Write in yaml.

## 金絲雀部署 (Canary Release)
- 背景：金絲雀很敏感一點瓦斯就會掛掉，所以礦工要帶金絲雀才可以提早知道瓦斯濃度是否太高要爆了。
- 逐步提升轉至新API的流量人口
    - 80% 傳到 Java 版本 API
    - 20% 傳到 Python 版本 API
- 利用Nginx的upstream作分配 (weight dispatch)來達成金絲雀部署

## 總結

- Flask
    - 自助餐
    - 特殊需求
    - RESTful
- Django
    - 套餐 （懷石料理）
    - 無特殊需求
    - Admin, Template

## 公司徵人
- 歡迎到台中玩!

## 提問時間

- 移轉到一半時突然要新增功能，怎麼辦？
    - 全新功能的話用Flask寫新模組
    - 舊功能更改：跟老闆商量
- 重構時遇到的阻力，如何說服其他人？
    - 我是負責人所以沒有遇到阻力
- 怎麼確定新的功能正常
    - 直接上線到市場上測試
- 那有測試階段嗎？
    - 因為量比較少，所以用人工檢查

###### tags: `pycontw2018`
