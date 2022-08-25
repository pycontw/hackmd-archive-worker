# Python NPF 百香果 x 南投py 共筆
---
tags: Python 百香果
---

:::info
歡迎來到 Python百香果 共筆 :mega:

[YT 連結](https://youtu.be/vK6pZ_laXc8) 
[Mosky's slido 連結](https://app.sli.do/event/kuug2lga)
[Tzu-ping Chung's slido 連結](https://app.sli.do/event/29kqwr14/live/questions)
:::

## 活動議程
| 時間 | 執行項目 | 
| - | - |
| 14:00 - 14:05 | 活動開始 
| 14:05 - 14:20 | 主持人開場與社群介紹－南投.py |
| 14:20 - 15:00 | 講者分享1 : Mosky－Python 的隱藏魔法：符號計算、統計到機器學習 
| 15:00 - 15:10 | 休息時間 | 
| 15:10 - 15:50 | 講者分享2 : Tzu-ping Chung－pip install --unstable-feature=resolver |
| 15:50 - 16:00 | 活動結尾

## 共筆

### 社群介紹

* 12/4 成立南投Python Nantou.py
* 
* 市長以及校長支持，推廣 Python 程式語言
* 教育部大學社會責任實踐計畫-南投百香果資源永續之煉銀網平台： 推廣智慧農業，無毒栽培百香果相關加值產品
* Google 搜尋： 百香網誌
* 以 Open Data 建構百香果農產品交易網站
* 教材研發： 一邊學程式設計一邊認識百香果故鄉埔里，http://passionfruittaiwan.blogspot.com/2019/11/usrpython.html
* 智慧生活科技相關文章：http://cheng-min-i-taiwan.blogspot.com/
* 結論：
    * 768藝術空間，每月都會有 python 分享
    * 開發智慧農業，智慧照顧教材
    * 將智慧生活科技應用於 南投場域
        * 竹山： 竹編 QR Code
        * 鹿谷： 壓花 AR
        * 草屯： 著色 AR 魚
        * 埔里： 百香果智慧農業

### Python 的隱藏魔法：符號計算、統計到機器學習 - Mosky Liu

:star2: slide: 

<iframe src="https://app.sli.do/event/kuug2lga/live/questions" height=450 width=100%></iframe>


:star2: github: https://github.com/moskytw/


前言：
* Python 魔法： DEMO 30s 寫個網站  (flask)
* 比較推FastAPI

講者介紹：
* Pinkoi Backend Lead
    * 後端工程師招募中

緣起： 
- Pareto Distribution -> CDF, PDF 要用微分運算 ->  可用 python 來算
- 符號運算(微分):
    - [sympy](https://live.sympy.org/)

#### 統計學
- 假設檢定:婚姻評價、職業有不同的婚外情程度嗎? 
　- 利用chi-square test測試，結果為顯著(p-value=0.003)
- 迴歸分析:婚姻評價、信仰程度和婚外情的關係?
  - 婚姻評價與婚外情的關係的迴歸係數是-0.41(負關係)
  - 也就是說婚姻評價越好，越不可能發生婚外情

#### 機器學習
- 預測會不會發生婚外情
- 利用SVM

> 工具使用通常不困難，了解原理與問題本質才困難

---
#### 學習資源介紹
- [speakerdeck](https://speakerdeck.com/mosky)
    * Practice-python-3
    * Data-science-with-python
    * Hypothesis-testing-with-python
    * Statistical-regression-with-python
- Book
    - Introducing Python

##### 基礎學科系列
- 政大 Python 蔡炎龍
- 清大 統計學 鄭少為
- 交大 線性代數 巫木誠

##### 林軒田機器學習系列
- 機器學習基石
- 機器學習技法

##### Standford 機器學習、深度學習
- Stanford CS229 or Pedro Domingos's MachineLearning
- Stanford CS231n
- Stanford CS224n

##### 科普 youTube 頻道
- 3Blue1Brown
    - Essence of linear algebra
    - Essence of calculus

#### Q&A

Q: 如果希望以DS為目標轉職的話，請問是要先以工具為主還是要以理論作為主要的學習路徑呢?工具的話除了python跟R以外還有什麼工具是在成為初步的DS需要具備的呢?


A: Data Scientist 是新興職業，每家公司定義都不太一樣，先確認你想成為那一種

* Market Analyst (有點像傳統量化分析師)
    * 統計學，產業 domain knowledge (跟上面講的 AI 不太一樣)

* 研究演算法為主的
    * 在台灣比較少，台灣基礎研究還有些距離
    * 需要很強數學背景

* ML 工程師，演算法工程師
    * 使用某個現有 ML 演算法來解某個問題，了解這些東西如何 tune

* Data 工程師
    * 台灣比較缺的，也是世界趨勢
    * 如何做 User 資料收集，終端資料收集，再將這些資料轉成可以被分析的資料
    * 了解 Spark, Hadoop 生態系


講者補充： 其他工具
- [The SciPy Stack specification](https://www.scipy.org/stackspec.html) 基本認識
- [Seaborn](https://seaborn.pydata.org/)
- [Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html)
- [Dask](https://dask.org) pandas 延伸
- [Spark](https://spark.apache.org) 業界標準




Q: BACK HAND　要如何成為一個 junior 轉職 有點碰壁 有什麼方向 可以去深入  

A: 
- 可以看剛才的教材，先嘗試做個網站，了解網站每個細節
- 有些轉職者一些基本 CS 觀念如資料結構會不知道，造成溝通上的困難 (公司也有白板題)。 不用說要完全會，但至少要有基本的了解
- 網站要有自己作品
- 了解網站概念，看熟 Django 文件

---
### pip install --unstable-feature=resolver - Tzu-ping Chung 

:star2: slide: 

<iframe src="https://app.sli.do/event/29kqwr14/live/questions" height=450 width=100%></iframe>

:star2: github: https://github.com/uranusjr

- [pip 即將更新依賴解析器（dependency resolver）](https://gist.github.com/uranusjr/61f29ef16997148c3d9c2eda0bc1b2aa)

- 緣起： 去年有個 [seeking developers for Paid Contract Improving pip](http://pyfound.blogspot.com/2019/11/seeking-developers-for-paid-contract.html)，投上了

- pip team 介紹

- 一月 onboarding 印度行分享
    * 景點
        * Gateway to India
        * Taj Palace
    * 食
        * DOSA (餅)
            * 來印度不吃辣會活不下去
        * Gulab (甜點)
        * 沒有肉的印度烤肉
        * Pavings Bhaji (類似奶油餐包 + 沒有肉的義大利肉醬)
        * Ice Gola (類似覆盆子挫冰，但不吃冰)
        * Haldiram’s 來印度就要吃的餅乾 
            * ALOO BHUJIA: (有點像模範生點心餅）
        * 印度沒有百香果
            * 那些人好像也不太吃酸的，沒有在那裡吃到酸的過


二月開始 Fulfilment
* 工作都 Async，網路不太好

Uberconference 視訊軟體
* 唯一聽到其他人聲音的機會
* UX 不錯

Etherpad
* 開源文字協作軟體： 當會議筆記用，幾乎是純文字

Zulip
* Python 拿來當官方討論區，有考慮要關掉因為沒人用，但應該至少要等這 project 結束


Technical
* 想知道我們在幹嘛可以看 twitter Dustin Ingram 的文章
    * 剛好他也在參選 PSF group member
![](https://i.imgur.com/CKDmYB2.png)


* Dependence resolution problem
    * NP Hard
    * 可以被簡化為 Boolean Satisfiability Problem 
    * 市面上一堆 package 管理軟體 e.g. homebrew 都用SAT 方法解
    - 所有 package dependency 問題本質上都是 SAT 算法
    - ![](https://i.imgur.com/z2Dzkho.png)
    - ResolveLib有比較簡單的API所以才選擇使用
      - 講者就是Resolvelib的開發者 


Q & A

BERT 為何被放棄？
- 私下回答 uranusjr@gmail.com

對 Poetry 怎麼看？目前還是比較推 Pipenv 嗎？
- Poetry 有很多不錯的想法，作者很有能力成品也很優秀，不過設計上比較 opinionated
    - 作者比較沒有參與 Python 社群的標準化討論，所以比較疏於與其他工具的互動
    - 如果符合你自己的 workflow，會是非常適合你的工具；如果不符合，就會感覺需要 fight with the tool for what you want
    - 這在開源專案裡也是需要考量的點，與其他工具的互動性會影響專案獲得 contribution 的難度
- Pipenv 有人力不足的問題，缺少穩定貢獻者也讓設計比較雜亂
    - 不過相對與其他 packaging 工具的貢獻者交流管道比較通暢
    - 對進階使用者而言比較容易與其他工具互用，應用範圍比較廣

是怎麼找到這個機會參加這個開源專案的?
- 開源專案的貢獻不需要機會，討論絕大部分都是公開的
- 想貢獻就進去開始讀留言，找到能幫忙的就修，多做幾次就會融入
- 對學生而言 [Google Summer of Code](https://summerofcode.withgoogle.com/) 會是機會，相比在台灣企業實習划算很多（我覺得）
- 現在就可以打開 [issue tracker](https://github.com/pypa/pip/issues)，找到自己能做的就送 PR，剩下的做中學


### 結尾

#### 南投 py
- 推廣百香果團隊的果凍，面膜，果汁，沾醬，文創...

![](https://i.imgur.com/fyNUD6Z.jpg)


#### PyCon

財務補助到 6/21

pycon 缺人才
- SEO 高手
- 前端 Geek
- 對設計有 sense 又善於統整的小隊長


明年 keynote speaker
- Peter wang: Anaconda 作者
- Mariatta Wijaya: CPython 核心貢獻者第一位女性
- 蘇文鈺: programming the world 發起人




:::info
回饋問卷連結: https://reurl.cc/R482pz
:::

[RunCat](https://apps.apple.com/us/app/runcat/id1429033973?mt=12)
這是當天 Session Manager 螢幕上的貓咪 🐈 xD

###### tags: `Python百香果`
