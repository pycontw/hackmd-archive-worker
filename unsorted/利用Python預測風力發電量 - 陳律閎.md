# 利用Python預測風力發電量 - 陳律閎

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}

<iframe src="https://app.sli.do/event/nlrvxle3" height=450 width=100%></iframe>

> 從這開始
* Slide will be update to speaker's Github within few days.

## About speaker
* [陳律閎](https://chenlu-hung.github.io/)
    * 中興大學 應用數學系 副教授
    * 利用 Python 開統計學、巨量資料分析等

## 為什麼需要預測風力發電
* RE100聯盟: 100%使用再生能源
* 發電供給與需求平衡調度
* 調度速度隨發電方式有異
    - 調度速度: 天然氣(成本高) >> 燃煤(成本低)
* 風力發電預測的好處
    - 節省成本
        - 歐洲國家將電力視為大宗貨物，有期貨及選擇權等金融工具
    - 天然氣存量是否足夠?
        - 需要船運，船運需要好的氣候掌握
        - 預儲存量頂多一週
    - 電價預測
    - etc.

## 風力發電預測原理
* Power Curve Model
    * Steady wind speed <-> Power
    * 風力需要克服摩擦力才能達到最大發電量
    * 最大轉速有上限
    * 目前主流預測氣候方法: FEM 有限元素法 

### 問題
1. 風速預報不易
    * 氣象預報解析度
    * 地形
    * 風機彼此干擾
2. 有限元素法有計算量的問題，無法直接對全球計算-->採區域計算（以全球計算為基準，進行更細微的格點劃分）
3. 其他氣象變數
    * 風的質量與/風速/氣溫/氣壓/濕度有關

### 解決方法
* 高解析度氣象預報
    * $$$$$$$$
* 預報後處理
    * 風力發電機位置實際風速難以測量
    * 量測結果會受風機本身影響
* **Machine learning**

## 資料準備
### 德國歷史發電資料
* [Open Power SYstem Data Platform](https://open-power-system-data.org/)
    * 2010 - 2019
    * 15分鐘 解析度
    * csv檔
### 歷史天氣預報資料
* [GEFS 再預報資料](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-ensemble-forecast-system-gefs)
    * 唯一免錢!
    * 2012 版本氣象預報模型
    * 全球模式(低解析度)
    * netCDF v4 file type -> `xarray`套件可讀

### `rpy2`
* [Document](https://rpy2.readthedocs.io/en/version_2.8.x/)
* 把 R 套件當 Python 套件用
* 不需要會 R

## 機器學習演算法設計
* 均值定理
* 數學推導很重要，有效推導可以用免錢套件(誤差4.2%)做出跟官方(誤差3%~5%)差不多
* 隨便塞類神經網路誤差20%
* Future works
    * Rolling corss-validation
    * post-processing layers
    * seq-to-seq models
###### tags: `PyConTW2019`
