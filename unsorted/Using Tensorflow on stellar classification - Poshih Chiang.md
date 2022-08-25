# Using Tensorflow on stellar classification - Poshih Chiang

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}

## 怎麼開始的
- 天文：不事生產，沒有經費，佛心作功德研究

## 恆星
- 黑體輻射：恆星可以近似成黑體☢️
  - 有熱亮型、冷暗型
- 三稜鏡分光可以分出不同顏色（稱為光譜），得到不同溫度，溫度高的偏藍色，低溫偏紅色
- HR Diagram (https://zh.wikipedia.org/wiki/%E8%B5%AB%E7%BE%85%E5%9C%96)  - main senquence 主序帶: 大部分恆星都分布在此
  - OBAFGKM(LT)

- 光譜在不同波段濾鏡的強度積分可得到不同波段的亮度（星等）與斜率 （顏色）
    - color = $\Delta$ mag

- 雙色圖 color-color diagram (https://zh.wikipedia.org/wiki/%E5%8F%8C%E8%89%B2%E5%9B%BE)
    - Blending source problem: 不同天體的範圍重疊導致混淆
    - 過時

- 星色星等圖 color–magnitude diagram (https://zh.wikipedia.org/wiki/%E6%98%9F%E7%B3%BB%E9%A1%8F%E8%89%B2-%E6%98%9F%E7%AD%89%E5%9C%96)
    - 常常沒有距離
    - 不同距離的星在圖中會混到一起

## Goals 目標
- Multi-label classifer: photometry data -> spectral types
  - 星等容易取得: 希望從星等就可以分類

- 拍照片 (取得星等)比拍光譜快上千百倍
  - 很快就可以有大量的統計樣本

## Data 資料
- Photometry: 
  - SDSS + UKIDS + ALLWISE
  - 10 bands 
- Spectroscopy:
  - SDSS (https://zh.wikipedia.org/wiki/%E5%8F%B2%E9%9A%86%E6%95%B8%E4%BD%8D%E5%B7%A1%E5%A4%A9)
- ~ 50,000 stars 的 labeled data (csv格式, 先做一個小樣本)
- subclass -> 已知 label

- 不均勻的分佈 unbalance data (目前還沒解決) 

## Pre processing
- 修正 interstellar absorption
- 缺失的資料
  - 1 或 2 區段: 線性修正
  - 超過：drop

## Exp Design
- Easy classes (M, K): 簡單的先做，難的先跳過. 先 classify M, K.

## Tree

1. 收集500萬顆星的資料
2. M分類器，分出是否為M類
3. K分類器，分出是否為K類
4. 不是 M 也不是 K -> 分F跟G (現在有問題)
5. 時間代表訓練時間

## Models

四層類神經網路
PCA + NN (ReLU) + Sigmod Y/N

## Performance

|       | M   | K   | F/G |
| ----- | --- | --- | --- |
| 正確率 | 98% | 94% | 95% |


- M subclass ± 1 的分類可達到近 100% 

## 其他方法

- K-mean
- MLP
- Decision tree
- SVM (linear/RBN)
- Random Forest

## What's wrong with AFG

- Diffent sky surveys have different sperctrum
- 懷疑原本的光譜分類就有問題

## Problems

- 每種label量不平均 (Unbalanced data)
  - 解法: 產生更多資料 
- 原本label就有問題
    - 人工確認
    - 修正label

## 目前進度

- 光譜資料
    - supervised/reforcement way LSTM/RNN
    - unsupervised way
- 光譜資料+影像資料
- 光譜與星等模型互相學習

## 參考資料

- SDSS
- ALLWISE
- UKIDSS

## 經驗分享

- 要檢查資料x3
- 該領域專業很重要
- 團隊成員背景多樣性
- 透過幽默感、批判性思考來保持創造力




## 提問時間

- 分類困難是因為資料(50000筆)太少？
    - 雖然有考慮過，但是因為這些資料的label就有問題所以先修正label
    - 目前是小樣本試做，成功率提升後應用到下一代的資料中 (1.e8 量級)
- F/G分類上會因為Unbalanced造成某些分類資料太少？
- model是先PCA再用類神經，但是類神經就有PCA的功能？
    - 我們是新手所以先試
    - 怕over fitting
    - 我們覺得參數越少越好調整
    - 實際比較有PCA的結果比較好

###### tags: `pycontw2018`
