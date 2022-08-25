---
tags: 2021-organize, 2021-program
---

🔙 Back to [歷年 PyCon TW Organizing 共筆](/ryPr7SFyP/%2FHM5mHCFKQCu7-W5ea8ITcw%3Fview)
🔙 Back to [PyCon TW 2021 Organizing 共筆](/Wb9vQrfJQk-5tPoPR23hwA)
🔙 Back to [PyCon TW 2020 Organizing 共筆](/5u84SOprTUeQYBR57TH49w)


# PyCon TW x PyHUG Meetup 共筆


:::info
歡迎來到 PyCon TW x Taichung.py 2021 共筆 :mega:

[YT 連結]() 
[回饋單連結](https://forms.gle/qYib9XefEjJGHK3R7)
[【How to process ECG signal for Machine Learning】 slido 連結](https://app.sli.do/event/w6wpocxm/)
[【Use machine learning to generate medical report】 slido 連結](https://app.sli.do/event/vp55etgo/)
:::

## 共筆


### 1. How deep learning helps astronomers on observation data - CNN for classifying galaxy spectra

講者： Inès

<iframe src="https://app.sli.do/event/tffoga6f/live/questions" height=450 width=100%></iframe>

> 共筆從此開始

為什麼研究星系？
尺度
- 46kpc -> 151530光年
怎麼研究？
- 觀測： 亮度/大小／元素
    - 不同波段觀察到不同機制
    - 可見光： 恆星類
    - UV光： 剛誕生恆星
- 從觀測資料推測： 
    - 物理性質： 黑洞質量

目前的問題？
- 目標： 西佛星系 (Seyfert)
    - 因為有活躍的吸積過程
- 問題
    - 分類挑選困難
        - 類型過多：
            - 早期肉眼挑
            - 1990: 兩條特殊譜線的比值
            - 1997-now: 擬合光譜, （用兩條 Gaussian）
                - 花類大量時間，但也無法確定光譜是否同時擁有兩個特徵
    - 尚未確定輻射機制
        - 不清楚為何光譜會同時出現兩個特徵
            - 還在爭論中

Deep Learning
- 天文觀測
    - 處理分成影像和光譜
    - 觀察數值強度

資料處理與分析
- 製作星系列表： pandas. astropy
- 下載光譜檔案
- 預處理光譜檔案
- 建立 cnn 模型
- 擬和星系光譜

SDSS
- 全天觀測：有影像及可見光等光譜開放資料
    - 有教學如何取得資料
    - 幾百萬影像與光譜資料
    - 每一兩年會有新資料
製作星系列表
- SkyServer
    - SQL Search
預處理光譜檔案
- 使用 astropy 套件讀取 FITS 格式檔案，後使用 pandas normalize
擬和星系光譜
- lmfit: 可提供擬合誤差

總結
- 使用一維 cnn 模型來分類光譜效率較以往分類方式高
- 增加訓練樣本數來提升模型辨別能力
- 透過此 cnn model 收集更多不同星系資料

Q.A

- train test set 切分方式： 
    - random 分類
- 其他研究領域
    - 靠 nn 分析光譜得到 恆星年紀
    - 用 gan 產出宇宙論

- 使用 con layer 而非 linear layer
    - 看重 pixel 相關特徵
        - 但如果不同波段光譜的資料缺漏太多效果也不見得好

- 物理系 code 契機
    - 大四計算機物理課程
    - 暑期研習


### 2. Machine Learning Applied to Stock Index Performance Enhancement

講者： Tina Hsu

<iframe src="https://app.sli.do/event/4p89bcmv/live/questions" height=450 width=100%></iframe>

> 共筆從此開始 


Enhance the model
- Time series data dealing
    - 22 -> 667 特徵
- Feature selection
    - 60% sample
- Feature Normalization
    - 如果採用其他模型可 normalize
    - 目前使用 random forest
- Leaf pruning: 10% of samples
    - 用 vote 方式挑選表現好的股票

S&P 500 total returns
- 目前方法總報酬都超過標的
    - 大部分行情好時超過 S&P 500
    - 行情不好時跌會比大盤多

總結
- 解決不同時期不同重要因子的問題
- 1%~5% 投資組合 -> 2% 投資組合目前效果最好
- 缺陷
    - 行情表現不好時投資組合會落後大盤
        - 前期價格表現變動對模型影響大
            - 接近動能類型策略
QA
- 開源？
    - 資料可用性關係可能沒辦法開放



### 3. The 2020 CVPR Workshop of Low-Power Computer Vision Challenge 參加經驗分享

講者： 林明憲

<iframe src="https://app.sli.do/event/x20pugwu/live/questions" height=450 width=100%></iframe>

> 共筆從此開始 

Low-Power 領域電腦視覺競賽

動機
- 研究所畢業多年
    - 提升 python 能力
    - software define hardware 時代
    - 跳脫舒適圈
LPCVC 背景介紹
    - CV 三大會議： ICCV(2y) / CVPR(1y) / ECCV(2y)
    - 與 ICCV / CVPR 同步舉行之 low power cv 競賽
    - 3 track
評分標準
- 團隊限制每日提交一次
- 影像分類
    - ImageNet: 1000 類
- 指標
    - 準確度超過 68.5%
    - 有 latency 限制 (根據公式)
- 平台簡介
    - Ultra96V2: 單板電腦
    - DPU: 用來加速神經網路
    - PYNQ: 專為 FPGA 設計的 python 框架
    - Vitis-AI: Xilinx AI stack (compile tool)

先前準備及挑戰策略
- 籌組團隊
- 資源檢視
- 模型挑選
- 目標設定

![](https://i.imgur.com/iYoLrXa.png)





### 4. Implementing NMF in PyTorch Framework: An Autograd Approach


講者： Chin-Yun Yu

<iframe src="https://app.sli.do/event/ejvtyili/live/questions" height=450 width=100%></iframe>

> 共筆從此開始 

今日slide: https://docs.google.com/presentation/d/1Ji-9dc2SVUdx3Me5fEJalT4gTaTZwBr7rvs7Ko2Xoog/edit?usp=sharing
