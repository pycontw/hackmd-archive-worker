---
title: 使用 Pytest 進行單元測試 - Max Lai
tags: PyConTW2021, 2021-organize, 2021-共筆
---

# 使用 Pytest 進行單元測試 - Max Lai

{%hackmd f0JLCtZCTiWo4ZBRNKd8cg %}

<iframe src="https://app.sli.do/event/wylgzomz" height=450 width=100%></iframe>

<iframe src="https://wall.sli.do/event/wylgzomz?section=3e9b672e-2b65-4248-b295-2c8e0a43e87f" height=450 width=100%></iframe>

- slides: https://www.slideshare.net/maxcclai/pytest-pycon-tw-2021 
- github demo code: https://github.com/cclai999/pycontw21-pytest
- demo video(13:00開放): https://www.youtube.com/playlist?list=PL6QCmNaWVjU4GOvJ_Gj2RQZimkUZdbHbz
###### tags: `PyConTW2021`

## Q&A
#### 第一階段
- Q: 請問做機器學習也會建議做unit test嗎？謝謝~
    - 機器學習比較難測，但是可以針對一些特殊的小單元進行測試
    - 如何測試 deep learning code, by Max [How to Trust Your Deep Learning Code](https://krokotsch.eu/cleancode/2020/08/11/Unit-Tests-for-Deep-Learning.html)
- Q: 能不能舉幾個需要單元測試的場景和應用，不確定何時會需要用
    - 建議有function就可以用，特別是有加減乘除或是邏輯判斷時，因為人的邏輯跟機器的邏輯可能不太一樣
- Q: 想問會建議一個測試上測試多個情境嗎？
    - 一次一個情景比較好
- Q: 想要一個函數只有一個測試函數的話，請問exception的測試跟pytest parametrize可以合用嘛？
    - 建議exception要分開測試
- Q: 請問如果是用SQL CODE去呼叫DB的程式碼，應該要怎麼MOCK?
    - 先把 DB 內容的 function 先抽出來
- Q: 請問是否建議在 CI 流程當中直接呼叫第三方 API 進行測試 (不做 mock)?
    - 要看情境
- Q: unittest 與 pytest 該如何做選用，優缺點是如何，有何經驗可以分享，感謝~
    - 講者比較喜歡 pytest，因為比較 pythonic
- Q: 如果測試量大的話(例如 2000 項以上測項)，有什麼辦法加速測試嗎？ parallel tests?
    - xdist: pytest distributed testing plugin
    - https://pypi.org/project/pytest-xdist/
- Q: 一個測試函數有多個assert的話 上方一點的assert error的話下面的是不是就不會跑了
	- 是
- Q: 請問一個測試 function，只有一個 assert 比較好，還是可以寫多個 assert？
	- 同一個邏輯底下的話就寫在一起
- Q: 請問關於 coverage, 如果程式碼內有單行 if, 例如 a = 1 if is_success else 2, 這樣 report 內雖然顯示有覆蓋到, 但可能只測到一個狀況, 沒有測到 else, 實務上會怎麼樣解決

- Q: pytest 是否可以針對多個微服務進行整合測試? (例如多個 docker container 組成的環境)
    - 利用一些特殊的API
- Q: 想詢問單元測試單元的次數頻率，若測試過部分還需要測試嗎 ?  (edited)
    - 每一次commit就重run一次，才了解會不會改A壞B
- Q: 如果想要mock mysql db有什麼建議嗎


### 講師分享
有Pytest可以讓程式愈來愈好，若是沒有Pytest，可能會傾向code會run就好(有測試的話比較能放心重構，就算改錯也能被抓出來，不用擔心影響到其他部份)

