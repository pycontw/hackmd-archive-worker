# 小鴨城(Duckietown)，一個基於 Raspberry Pi 和 ROS 的開源無人小車專案介紹 - sosorry

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}

slide: https://www.slideshare.net/raspberrypi-tw/duckietown-raspberry-piros

* 感測器校正
* 計算機視覺
* 物體辨識
* 非線性估計
* 全域定位

## ROS
* 專為機器人軟體開發所設計的系統架構
* ROS = 訊息管道 + 組態工具 + 機器人功能 + 生態系統

## 可能遭遇的實際問題
* 感測器資料收集
    * 亮度補償 (不同環境 光度不同)
    * 直線偵測 (顏色轉換)
    * 圖像道路的映射轉換(3D to 2D)
    * 車道相對估計 (車道寬度, 左右兩邊距離 => (輸出) 往前速度, 左右角度)
    * 車道控制 (移動的預測, 以及實際狀況的修正)

## 學習資源
* MIT 2.166 Duckietown
* Duckietown 交大分支 (軟體創意專題)
* Duckietown Bunny
* Duckietown Log Database

## 延伸專題
* [Puyuma](https://github.com/Puyuma/puyuma-core)

###### tags: `pycontw2018`