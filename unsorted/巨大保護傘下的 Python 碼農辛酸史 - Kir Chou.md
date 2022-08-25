# 巨大保護傘下的 Python 碼農辛酸史 - Kir Chou

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}

Slide: https://bit.ly/2Jwn8oE

## 保護傘
- 大公司: 可能讓員工無法發揮所長

## 關於我
- [LinkedIn](https://jp.linkedin.com/in/kirchou)
- [stack overflow](https://stackoverflow.com/users/2740386/kir-chou)
- [Github](https://github.com/note35)

## 如何進大公司？
- How to get into them?
- what are them doing?

## 演講主要議題
讓想進大公司的人參考PYTHON的應用，與給予面試官一些面試PYTHON一些想法。

## 大綱
- 3 種台灣產業
- 3 種 Python 能力水準
- Python 在大公司的使用情形
- 個人經驗想法

## 三種產業

- 半導體產業
    - IC Design House (IC設計公司)
    - OEM(Original Equipment Manufacturer / ODM(Original Design Manufacturer)，就是代工廠
- 普通軟體公司
    - RD < 1000人
    - Software Developer 為主
- 巨型軟體公司(巨大保護傘)
    - RD > 1000人
    - 各種人都有

## 為什麼他們用 Python?
### 半導體產業
- 討厭 Perl(X)  轉換成 Python(O)
- 作為腳本語言使用
    - 驗證、EDA工具 (RD)
    - 整合測試 (QA)
    - 自動化 (DevOps)
    - 資料分析 (Data Scientist)
- 比較像處理後端事務，不是用來做產品
- 普遍的職缺內容都包山包海

### 普通軟體公司 (RD 1000 人內)
- 沒有 Perl 包袱
- 作為一般語言使用
    - App / API / 資料串接 (SE)
    - 自動化 (DevOps)
    - 整合測試 (QE/Quality Engineer)
- 資料工程師(非講者專長)
    - 資料分析 (Data Scientist)
- 職缺比較特定範圍
    - 希望有即戰力
    - 明確列出大量工具名稱（公司使用的核心工具）
    - 甚至指定Django版本
    - 是台灣最普遍的職缺形式

### 巨型軟體公司
- 討厭 Perl(X)  同樣需要轉換成 Python(O)
- 跟半導體產業類似，描述也極為空泛
- 職缺要求很有該程式語言長期經驗

## 三種 Python 能力水準

### 等級一: ~~可愛的皮丘~~
- [So you want to be a Python expert?](https://www.youtube.com/watch?v=cKPlPJyQrt4)
- Leetcode medium
- 會使用內建function與module
- 會使用Decorator/Context manager/Generator
    - 到底會不會使用專屬於 Python 的功能還是只是會 loop 跟 function
- 熟悉OOP/MRO
- 接觸過Test/Monkey patch
- 熟悉生態環境/趨勢/寫作格式/歷史
- **How** to use Python

### 等級二: ~~皮卡丘~~
- 接觸Python核心/GIL問題
- 設計模式(Design pattern + 系統設計(System design)
- **為什麼**要使用 Python?
- **在哪裡**使用某 library/framework?

### 等級三: ~~憤怒的皮丘~~
- Python + 與 Python 整合
- 看 Python source 了解原理
- 看 Library source 了解原理
- **Where** to use Python

## Python 在大公司的使用情形

- 雇用標準不是看你會不會某個 framework，而是為什麼要用這個？你做過哪些專案？解決過哪些問題？
- Library與Framework可能幾天就可以上手，但是背後的Domain knowledge才是無法短時間學習的東西，如：如何調整NN中model的參數

### 大公司的生態
- 內部架構
    - 可能要從0開始建立所有project
- 內部開發環境
    - 無法直接使用外部的東西
- Stack Overflow 不夠用

## 個人經驗分享

### 個人反省
- 太專注於職缺內容
    - 太在意使用過的 library/framework
    - 其實重點在能創造價值，解決問題
- 讀太多 python 技巧
    - 知道了也只是休閒，對工作沒有幫助
- 讀太多面試心得
    - 面試者的背景跟你不一樣，無法直接套用在自己身上
    - 被問的問題與面試者的背景很有關係
    - 應該去思考該公司重視的項目
- 為何我在這裡
    - 為何外國公司來台灣找人？
        - 外國公司找到的人似乎無法在台灣發揮
        - 這些人可以從無到有建立搜尋引擎，可是寫到履歷上不好看
    - 台灣的人才流失
        - 競爭力
        - 市場小
        - 只看結果
        - 硬體公司主導，對軟體公司不友善

# Q&A
- 沒時間了，來 open space 找我

###### tags: `pycontw2018`
