---
title: 成功地測試失敗 (Fail tests successfully) - Keith Yang
tags: PyConTW2021, 2021-organize, 2021-共筆
---

# 成功地測試失敗 (Fail tests successfully) - Keith Yang

{%hackmd f0JLCtZCTiWo4ZBRNKd8cg %}

<iframe src="https://app.sli.do/event/9rgrmtht" height=450 width=100%></iframe>

<iframe src="https://wall.sli.do/event/9rgrmtht?section=b9378313-c568-4125-a089-deb25608cd6d" height=450 width=100%></iframe>

> 從這開始共筆

## 逛逛測試場景

- 場景一：團隊 coverage 不正常發揮提升
- 場景二：升級套件導致測試問題
- 場景三：Jenkins 有在好好工作～

## 講者背景

- iCHEF lead backend engineer
- Tiapei.py co-organizer

## 測試帶來的好處

- Hypothesis
    - 測試對大家都好
- 團隊的期待
    - 關鍵價值的速度和品質
        - 品質：程式碼測試覆蓋率 (code coverage)
        - pull-request 的 review 人數
        - 開發時的整合問題、上線前 QE 驗出的問題數
        - hotfix 上線後的重大問題數
        - 測試數量與角度
        - …
- 測試常見場景
    - CI 提報 coverage 掉太多
    - QA 問有沒有 unit test
    - 第三方 API 只能在正式測試卻不能在測試環境測試
- 經驗
    - 說服力有限，有可能有用但也可能沒用

## 工具簡介

- unittest.mock
    - 用來仿製程式的一些行為
- pytest
    - 簡單地寫測試，出錯時得到更詳細資訊
- coverage
    - 計算並輸出程式覆蓋率
- vcrpy
    - 錄下打出去的 requests
- Jenkins 2 pipeline
    - 同時跑多個測試
    - 功能還在持續增加

## 沒有測試的壞處，如何測好、測到

- 優先等級問題
- 注意事項
    - 寫測試的時候應避免重複寫原來的程式邏輯
    - 不要因為著急而跳過測試
- 沒有測試的話
    - 會花更多時間在上線前的來回
    - 可能有些問題還沒修好就上線，引發更多新問題
- 經驗
    - 使用pytest測試第三方api，在非prod的branch中執行，避免突發性的api錯誤
    - 用三元表達式，可能覆蓋率不準確
    - 什麼都要測試嗎?
        - 關鍵的測試有測到更重要!
    - 測試是為了速度與品質
        - 不好的"快"不是"真的快"
    - 簡明的程式與測試很棒
        - 追求"測到關鍵邏輯"

## 總結
> 預防勝於治療

- 測試是為了==速度==和==品質==
- ==簡明==的程式與測試，持續追求==測到關鍵邏輯==
    
## iCHEF 招募中～快來

## Q & A
    - 來不及問問題啦～大家直接到 R0 講者交流區去問 Keith 吧 :smiling_face_with_smiling_eyes_and_hand_covering_mouth: 

### Slido 上的問題

Q: 想問一下 pytest.mark.parametrize 與 Django 碰到的問題是什麼
A: pytest 的 fixture 與 parametrize 不支援 unittest.TestCase
https://docs.pytest.org/en/latest/how-to/unittest.html#pytest-features-in-unittest-testcase-subclasses

Q: 寫測試的策略會影響到 code review 嗎？兩者的交互作用 (如果有的話) 是如何？
A: 舉例來說，code review 要求有邏輯就要寫測試 -> pull request 就會有測試。pull request 裡的 code 沒有測試，review 的人需要自己用腦編譯確認程式沒有 syntax error 等低級錯誤，或著有時難猜是想完成什麼樣的 spec。

###### tags: `PyConTW2021`
