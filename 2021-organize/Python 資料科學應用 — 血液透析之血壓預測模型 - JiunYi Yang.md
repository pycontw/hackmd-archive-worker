---
title: Python 資料科學應用 — 血液透析之血壓預測模型 - JiunYi Yang
tags: PyConTW2021, 2021-organize, 2021-共筆
---

# Python 資料科學應用 — 血液透析之血壓預測模型 - JiunYi Yang

{%hackmd f0JLCtZCTiWo4ZBRNKd8cg %}

<iframe src="https://app.sli.do/event/afdghll1" height=450 width=100%></iframe>

<iframe src="https://wall.sli.do/event/afdghll1?section=e7c59a09-26c2-4ffc-84db-df318ab64331" height=450 width=100%></iframe>


--- 

# 公告
嗨各位，由於我的講題預錄剛好講滿 45 分鐘，所以針對 Q&A 我會將 Slido 上的問題在這邊進行文字回覆；若相關疑問想交流，也可以到 Gather - R1 (with speaker's Q&A) 那邊找我！

# Slido Q&A 
- Ｑ：剛剛聽到每兩分鐘就會有一筆紀錄，想問每天更新 model 這樣的頻率有什麼考量嗎？如果更新的 model 沒有預期的好，也是會更新嗎?
    - Ａ：
        1. 目前每天 re-train 的考量點還會根據醫院端需求和成效調整；假設醫護有回報比較多 case 是預警判斷錯誤的，那我們可能會增加 re-train 的頻率。也還要考慮到院內環境能夠負荷多高頻的 re-training，因為當 training 和 prediction 的流程並行時會需要共享院內機器資源。
        2. 以目前 pipeline 的設計，會透過 MLflow & DVC 進行模型版控，根據加入新資料後的 Sensitiviy, Specificity （分類）及 MAE（迴歸）等數值來決定隔天是否更新成新模型進行預測；目前已我們也會與腎臟科的醫師定期來檢視成效來決定模型迭代的頻率。
        3.  MLflow：模型成效的追蹤，它的 Model Tracking 和 UI 工具可以非常快速的比較不同模型間的成效
    

- Ｑ：有說到是非本科來接觸資料分析，想知道是什麼契機XD 以及是如何開始的，有推薦的資源嗎～
    - Ａ：
        - 我在當數位廣告操作師之前有自學過網站開發和網頁事件追蹤，所以對程式比較熟悉一些，後來因為要協助廣告客戶做成效優化，我們會整合 FB Ads, Google Ads, GA 等數據，當時有很多手工 work，才會自己去探索怎麼使用 GDS (Google Data Studio)，比較快速的監控成效、從 BigQuery 撈比較細的行為維度，Python 分析廣告效果；
以及我本身對事件資料搜集端（ex：埋追蹤碼於客戶網站，進行用戶事件搜集）有興趣，因為客製廣告受眾來自於廣告商可以追到怎樣的行為、做什麼處理（條件式、建模訓練等）讓每一包變得更精準；所以選擇往數據分析端走，在前公司剛成立數據部門時有自薦加入
後來發現數據領域的開源工具迭代很快，掌握一項資料探勘技術越深、在新東西出來的時候能更快應用是更好的，因此透過發展「與想要的技能樹相匹配的」 side-project 來快速提升能力。

        - 資料分析推薦資源：
            - 初學者：從資料集設定分析問題，或是從真實世界發現問題、找資料集；接著利用解決問題的過程熟悉不同的方法。推薦以下方法庫：
                -  [Machine Learning Mastery](https://machinelearningmastery.com)
                -  [Analytics Vidhya](https://www.analyticsvidhya.com)
                -  上 Kaggle 學前幾名的作法，資料探索視覺化/特徵工程/建模 等，看別人的作法找脈絡
            

- Ｑ：在Feature Engineering中，請問講者是如何知道/想出新的特徵?
    - A：因為題目是醫療類型的數據預測，對於該領域的 Know How 其實非常重要；目前是與團隊中的醫學工程博士、腎臟科主任醫師來補充相關知識。另外，A我們也採用 XAI 工具來來與臨床人員確認特徵的重要性：比如 SHAP、Scikit-learn 的 Feature importance 來比對模型使用的特徵是否吻合。

- Ｑ：請問關於讀取資料的部份講者提到用了multi-processing來加速讀取，就我理解這部份瓶頸是在I/O，想請問為何不是考慮threading的方式處理?
    - A：其實是在實作的時候直接以過去經驗用了 multi-processing，但我沒有想太多理論面，這是我應該加強部分，感謝你。另外看其他測試分享的文章 [ex1](https://www.rocksaying.tw/archives/15356403.html) [ex2](https://qing-yao.blogspot.com/2016/08/writeByMind-2.html)，也是提到 multi-processing 速度較快，I/O 密集型則是[相差不大](https://www.cnblogs.com/massquantity/p/10357898.html)；說到這個，最近有看到另一篇是[微線程](https://www.maxlist.xyz/2020/04/09/concurrency-programming/) (Coroutine)，如果之後有加速需求也會考慮測試看看

- Ｑ：想請問對於長期透析的病患，只用自己的過去數據做模型來預測會不會反而效果比較好？
    - A：以單個病患去建模，達到足夠的數據量會需要該病患進行過多次血液透析累積，實務上無法對醫護提供即時的預警，所以考量到即用性和廣泛適用，我們從多位病患多次血液透析紀錄進行建模。
若是單位病患，以我們目前測試的結果而言是有相關性的；原因是以醫療類型的事件預測中，大部份都是呈現資料不平衡的問題，我們曾經使用 T-SNE、PCA、XAI 等方式來將資料視覺化並加以判斷；但考量到深度學習的需要保持資料的多樣性和數量、還有做到病人個人化模型所需的資源，目前還是傾所使用一個通用型模型來滿足臨床使用的需求。


- Ｑ：1. 請問預測是否只用當天30分鐘之前的血壓資料做預測，是否有使用過去(前幾天)洗腎資料？理論上過洗腎發生低血壓，末來發生機率會高非常多。2.請問此系統目前是否佈署在洗腎室做即時預測試用？3.請問血壓(raw data)是否是都由護理人員手動測量，平均測量間距大約是多少，預測模式是用多少的間距當input(2分鐘？)
    - A：
        - 1.目前我們是使用病人所有有效的回溯資料做模型訓練，再進行預測；所以我們有考慮到病人的情況來進行訓練。
        - 2.目前已經完成人體試驗的審查，即將導入南部某地區醫院進行臨床試驗。
        - 3.血壓值是透析機器的自動模組進行測量的：幫病人穿上測量模組 -> 設定測量間隔 -> 資料透過 TCP/IP 傳到資料庫
        - 4. 預測是以當次血壓量測及前60分鐘資料，對下次量測(30分鐘後)進行預測 
    
- Ｑ：請教3個問題：(1)每隔30分鐘量一次血壓，如此量測點數很少，例如只有1個數據點，如何進行差值特徵？(2)血壓量測點數少是不是會影響False alarm次數高？(3)模型整合進入醫院的系統是否有困難？例如自動取得即時的血壓計資料。謝謝～
    - A：
        - 1.目前我們會放棄第一個沒有差值的時間點，改以第一個小時 -> 預測第一個半小時來進行；另外我們比對該醫院病人回溯性資料及相關的回顧文獻，發現低血壓的集中發生在血透析的第 3、4 個小時，所以去除第一個預測點在整體上並不影響成效。
        - 2.目前沒有看到這方面的問題；我們在做模型解釋性時，發現是有一些的特徵會對預測結果造成影響。
        - 3.血壓值是透析機器的自動模組進行測量的、但對於仍使用人手測的的診所、醫院來說，資料的不準確性會是個問題；其他麻煩的地方在於醫院的資安的設計、針對醫護人員的業務邏輯理解、黑盒模型的預測解釋性、上市的法規認證都是本案會遇到的問題。

- Ｑ：直播畫面不清楚
    - Ａ：*行前信有提供三種管道，都測試看看；我這邊在 Gather 畫面和聲音是清楚的哦～*


# 演講大綱
- 血液透析預測低血壓發生的重要性 [5 mins]
- 建模目標、流程說明 [5 mins]
- 血液透析數據介紹 [8 mins]
- 數據前處理與特徵生成 [10 mins]
    - 前處理流程
    - 時間差值特徵
    - 數據樣本標籤不平衡處理
    - 多執行緒加速資料處理效率
- 建模、優化與成效視覺化 [10 mins]
    - 交叉驗證進行參數搜尋
    - 遞迴特徵排除
    - 分類樹及神經網絡參數組合成效表
    - 迴歸樹及神經網絡參數組合成效表
    - 特徵重要度
    - 集成學習
    - 二元分類混肴矩陣
    - 數值預測殘差分佈
- 結語


### ＊前情提要

#### 講者簡介
- 講者：楊鈞宜
    - 社群
        - [LinkedIn](https://www.linkedin.com/in/jiunyiyang)
        - [Facebook](https://www.facebook.com/Abao.JiunYiYang)
    - 工作經歷：1 年網路廣告/直效行銷背景，自學程式轉職為數據科學家滿 1 年，曾任職於行銷科技業、金融業
    - 教育經歷：
        - 國立政治大學 資訊管理研究所 碩士

- IEEE ECBIOS 2021 - Best Paper Award
    - 獲獎論文
        - [Differencing Time Series as an Important Feature Extraction for Intradialytic Hypotension Prediction using Machine Learning](https://ieeexplore.ieee.org/document/9510749)
        - [The New Method of Feature Selection for Intradialytic Hypotension Prediction using Machine learning](https://ieeexplore.ieee.org/document/9510559)


### I) 血液透析預測低血壓發生的重要性

#### 真實世界問題
- **什麼是血液透析？**
血液透析是末期腎臟病（ESRD）的保守性療法，目前全球約有 2,000,000 位透析病患，以台灣為例，約有 95,000 位透析病患，近 18 年透析盛行率增加 8.9%、發生率增加 3.7%；每年新增 12,346 人、淨增加約 2,300 人
但透析患者五年累積存活率卻只有 56.2%，這方面的治療更是全民健保支出的第 1 名。
其原理是透過人工腎臟將血液抽出體外，過濾掉當中的廢物與多餘水分，再將過濾後的血液輸回患者體內。每位病患每週要接受 3 次療程，每次 4 小時。

- **透析中低血壓發生的影響**
儘管在這十多年透析機器與技術進步，透析低血壓之發生率仍然居高不下；大約 20%–50% 透析療程會出現透析低血壓。
透析低血壓的發生直接或間接的導致或加重許多併發症與共病，如冠狀動脈心臟病與腦血管疾病等，也直接導致病患出現如痙攣、意識障礙、虛弱與腸胃症狀等降低病人生活品質。
然而對於低血壓的處理，包含降低脫水量、降低流速等，更會讓透析品質下降。
綜合以上，護理人員更會因低血壓而產生的加班照護成本 10~15 mins 的護理成本 (US$ 5 - $7.5)，嚴重時更可能產生訴訟成本，總額外醫療成本估計超過 10 億台幣。


#### 提出解決方案：血液透析低血壓預警系統
由於護理人員最快只能間隔 30 分鐘量一次血壓，我們希望透過預警系統提前對下次量測(30分鐘後)發生低血壓機率高於門檻的病患發出預警，讓醫護能夠對病房狀況排序處理。


### II) 建模目標、流程說明
#### 雙指標輔助醫護判斷

#### Data Pipeline Overview



### III) 血液透析數據介紹
#### 資料表介紹

#### 資料探索
1. 血液透析**收針前 1 小時發生低血壓機率最高**
2. 盤點與低血壓發生較高相關的特徵



### IV) 數據前處理與特徵生成
#### 前處理流程

#### 格式轉換：以滑動視窗產生訓練資料
#### 使用 Multiprocessing 節省處理時間

#### 使用前幾次血壓記錄生成「差值特徵」
#### 使用 SMOTE 算法對少數標籤合成新樣本，平衡兩類別的樣本數




### V) 建模、優化與成效視覺化

#### 以交叉驗證結果進行參數搜尋最佳化
#### 遞迴特徵排除  Recursive Feature Elimination

#### 分類

##### 二元分類混肴矩陣（指標解釋）
##### 機器學習分類器中，以 LightGBM Classifier 較佳
##### 不同參數設置下的 RNN 模型中，LSTM 擁有較佳成效
##### 使用 SHAP 值增加模型可解釋性
##### Ensemble Learning with Blending

#### 迴歸
##### CatBoost Regressor 較佳；遞迴特徵排除使 R2 再提升 0.7%
##### GRU 效果較佳；遞迴特徵排除使 R2 再提升 1.7% 
##### 同樣使用 SHAP 值視覺化每個樣本特徵的重要度
##### 81.3% 的預測誤差在 10 mmHg 以內 


### 結語
1. 本講題共有 2 篇相關期刊論文發布於 3rd IEEE ECBIOS：
- Differencing Time Series as an Important Feature Extraction for Intradialytic Hypotension Prediction using Machine Learning
- The New Method of Feature Selection for Intradialytic Hypotension Prediction using Machine learning


2. 後續我們已將資料及建模流程自動化：
    - 模型代碼打包完成
    - 初版資料流程自動化：使用 Prefect Local Server

3. 未來將持續優化模型成效，並建置模型版控流程等


若您對於本講題的模型再優化有興趣，歡迎相互交流

### 聯繫方式
Jiun-Yi Yang
- email: jiunyi.yang.abao@gmail.com
- linkedin: linkedin.com/in/jiunyiyang

Nero Un
- email: nero.chun@acusense.com.tw 
- linkedin: linkedin.com/in/nerouch


###### tags: `PyConTW2021`







