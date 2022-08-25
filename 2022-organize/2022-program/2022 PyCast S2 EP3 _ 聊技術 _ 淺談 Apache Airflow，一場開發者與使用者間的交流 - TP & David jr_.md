---
tags: 2022-organize, 2022-program, pycast
---

🔙 Back to [歷年 PyCon TW Organizing 共筆](/ryPr7SFyP/%2FHM5mHCFKQCu7-W5ea8ITcw%3Fview)
🔙 Back to [PyCon TW 2022 Organizing 共筆](/rkk3KQ_VY)

# 2022 PyCast S2 EP3 | 聊技術 | 淺談 Apache Airflow，一場開發者與使用者間的交流 - TP & David jr.

[TOC]

---

## 本集核心目標
1. 讓聽眾對 Data engineering 有進一步概念
2. 讓聽眾對 貢獻開源 project 的形式＆參與方式有概念

## 來賓邀請
* Apache Airflow 開發者 - TP
* Apache Airflow 使用者 - David (Jr.)

## 資料收集

## Rundown Discussion
:::spoiler discussion
- **Opening & Intro**
    - 開場白 “Rolling on with ..."
    - 今天邀請到 ⋯⋯ 兩位來賓，David 是⋯⋯，TP 是⋯⋯。
    - 今天的主題會圍繞著⋯⋯，希望對於想要了解相關領域的聽眾會有⋯⋯
- **Engineer & Apache Airflow** `20 mins、主key是小d`
	- flow
	    - 聽小d分享業界經歷
	        - Data engineering daily routine
	        - 核心工作目標：data pipeline
	        - 慢慢帶出和 Apache Airflow 的關聯
	    - 幫聽眾瞭解這套工具
	    - 補充商業統計數據
	- 簡單介紹此工具
	    - 現在最主流的工具？
	    - 為何是最主流？ 
	        - pure python/ useful UI/ Open source
	- 此專案的有趣故事(如何成為 Apache 專案…?)
	- 通常被用來解決什麼問題？
	    - PyCon TW Data team 有使用，分享使用的場景
	- 跟目前其他工具相比
		- 聽說現在主流雲端服務也可以達成類似的功能？
		    - 多補充主流服務的作法
    	- ==(請求多幫補一些這部分的問題)==
    - ==(找 Airflow 的 usecase、應用場景案例、統計數據)==
- **開發者 vs 使用者的觀點 PK** `主key是TP`
    - flow
        - 如何參與專案貢獻到變成維護者
        - product roadmap 如何決定
        - [name=TP] 這個工具被送進 foundation 的過程分享
        - 使用工具遇到的困境或是無法解決的問題，請開發者回覆這個問題
            - [name=DJ] 但是大部分問題太 specific，開發者很難複現問題因此難以解決
    - 開發者的觀點 (maintainer's perspective)
    	- 開發的經驗談
    	- 如何經營開源專案的使用者社群？
    	- ==(請求多幫補一些這部分的問題)==
    - 使用者的觀點 (user's perspective)
    	- 使用經驗分享
    		- 什麼時候開始接觸資料工程這個領域？
    		- 之前是否有使用過其他相似的工具？
    	- 什麼業務/技術情境使你選擇採用這套工具？
    	- 有無使用上覺得此工具有所限制的地方？
    	- ==(請求多幫補一些這部分的問題)==
    - Product Roadmap
- **如何成為大型開源專案貢獻者？**
	- 從發 PR 開始
	    - 因為有棘手的問題想要自己解決。
	    - 單純發 PR 跟成為正式的 maintainer 的差別是什麼？
	- 沒有 data engineering 的 domain knowledge 也能開發出優秀的 data engineering tool？
	- 加入團隊的經歷
	- 有趣的工作經驗
	    - 參與 pycon US
	- 開源技術演講？
    	- ==(請求多幫補一些這部分的問題)==
:::
## Question Collection
### TP
###### Airflow 工作經驗
1. 當初是透過什麼方式加入 Airflow 團隊？可以幫我們介紹一下公司嗎
2. 開源專案的 product roadmap 該如何決定？你們有什麼 workflow?你在裡面的角色是什麼？
3. 你們如何經營開源專案的使用者社群？
4. Airflow 團隊的有趣的工作經驗分享？參與 PyCon US？
###### 開源貢獻者經驗
1. 之前你說過自己沒有 data engineering 的領域知識跟技能，這對於你在開發一個專門解決資料工程領域問題的工具上有沒有什麼阻礙？
2. 如果我也想成為開源專案開發者，我應該從什麼方向去努力？聽說有些人是不斷發 PR 發到變成維護者？
    - (討論)成為一個正式的 maintainer 跟單純發 PR 之間的差別?
    - Has contributing to an Open Source project made the speaker a better developer? How?
### d
###### 資料工程師經驗
1. 你擔任 Data Engineer 蠻長的一段時間，能否請你分享 Data Engineer 的一天，以及 DE 的工作重點
    * 大部分的時間不是等待你的 pipeline 跑完，就是在等待的路上。
因為 data engineer 的守備範圍就是這些 data pipeline，你每改一段 code 就要重跑這個環節，等測得差不多了就會整個 pipeline 跑一遍，我們稱為 end-2-end testing。
這個環節跟 backend 的專案相比，通常都比較花時間。因為 data pipeline 常常有 ML 的計算，會比 backend 的 CI 要久上很多
2. Data Pipeline 是 DE 領域的一大重點，如果想要對一個完全沒有資料工程經驗的人解釋 Data Pipeline 的概念，你會怎麼解釋？
    * DE field 相對於 Data Scientist, 就類似農夫跟廚師
### both
###### Airflow 使用經驗
1. Airflow 被送進 Apache Foundation 的背景？
2. 請幫大家介紹一下 Airflow 這套工具，generally 有哪些特點跟應用場景？
	- What is an orchestrator (Airflow is an orchestrator)
3. Airflow 的使用經驗，搭配業界實例、data team 的使用經驗分享
4. 有跟在不同公司擔任 DE 的朋友們聊過，幾乎每個公司在做資料工程的 ETL 時都一定會使用到 Airflow 這套工具。業界還有使用什麼其他的工具來解決類似的工作，以你的觀點來看你覺得為什麼 Airflow 成為主流？
5. ~~如果現在主流雲端服務也做到達成類似的功能，那麼~~自架 Airflow 的優勢是什麼？
6. [name=d] 舉出曾經使用 Airflow 遇到的困境或是無法解決的問題， [name=TP] 一起討論問題
###### 聽眾投稿
- What are Airflow's strengths compared to other orchestrators such as Luigi (Spotify) or Kubeflow.
- How active the Project is ? (Number of active developers and PRs per month)
- How well does Airflow scale? (Can I get it to run millions of jobs at the same time? If yes, how?)
- If the speaker is using Airflow in his current position?
- ~~Does Airflow also give more power and responsibility to PMs, POs and other non-technical positions? (It does in my company but I'm interested to know the speaker's answer)~~
