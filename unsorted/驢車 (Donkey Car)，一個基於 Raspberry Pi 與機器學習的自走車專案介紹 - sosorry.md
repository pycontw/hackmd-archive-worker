# 驢車 (Donkey Car)，一個基於 Raspberry Pi 與機器學習的自走車專案介紹 - sosorry

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}

> 從這開始
* [Donkey Car](https://github.com/autorope/donkeycar) 是什麼
    * 由 DIY Robocars 開始
    * ML 的效果比 Computer vision 好
    * 組成
        * 以遙控車(1/16 HSP RC Car)為載體
        * Raspberry Pi 3B+
        * 魚眼相機
    * 目標
        * Steering(方向)
        * Throttle(速度): 控制電壓決定馬達轉速
    * Raspberry Pi 3B+
        * Wi-Fi
        * 相機模組
    * 控制理論
        * Perception 感知
            * Take picture
            * Get user input
        * Planning 規劃
            * Get model prediction
        * Control 控制
            * Update servov
            * Update motor
        * Data collection 儲存資料
            * Save data
    * 軟體架構
        * Take picture
        * Get user input
        * Get model prediction
            * NN
        * Update servo
            * PWM value -> PWN signal -> Servo/ESC
        * Update motor
        * Save data
            * JPG / JSON
            * 把影像和操作資料一起丟進去訓練

* 機器學習 自駕車
    * 
* Hack
    * 
* 學習資源
    * 
* Donkey car vs. Duckiettown


http://docs.donkeycar.com/guide/train_autopilot/

https://www.youtube.com/watch?time_continue=119&v=4fXbDf_QWM4

###### tags: `PyConTW2019`
