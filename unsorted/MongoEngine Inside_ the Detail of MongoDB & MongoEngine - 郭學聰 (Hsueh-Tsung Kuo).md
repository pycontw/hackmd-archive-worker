# MongoEngine Inside: the Detail of MongoDB & MongoEngine - 郭學聰 (Hsueh-Tsung Kuo)

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}

# 👌 佛系資料庫設計：多玩遊戲就知道怎麼設計資料庫 👌

* [slide](https://hackmd.io/p/BkqA55Epf#/)

# pyMongo vs MongoEngine

- 兩者寫法不同
- 不建議用 MongoEngine，會碰到的bug較多
- 局部資料讀寫可能會有問題
- 使用lazyReferenceField 無法直接對值修改

# Race condition
* 可以利用Transaction來處理Race condition 問題
![](https://i.imgur.com/9P9GeCc.png)


# ORM 設計
- 跟race condition環環相扣
- [Perform Two Phase Commits](https://docs.mongodb.com/manual/tutorial/perform-two-phase-commits/) - 工會交易範例

# index
- sortable
- hash (sharding) - 打散資料減輕單一(DB?)的吞吐量

## 複合index (compound)
- 多個進入點搜尋同個資料的case
- 2.x, 3.x 設定上有差異

## 如何有效率使用複合index
- 相等 > 排序 > range
- 基本上不要在做排序較佳

# migration
- 基本上沒有比較好的方法

> equal, sort, range


# QA
- 雷亞所有服務基本上是mongodb，少數聊天系統是用firebase
- 遊戲市場變動很大，擴展column很常見

###### tags: `pycontw2018`
