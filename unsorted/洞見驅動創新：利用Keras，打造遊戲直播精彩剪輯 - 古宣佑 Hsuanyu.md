# 洞見驅動創新：利用Keras，打造遊戲直播精彩剪輯 - 古宣佑 Hsuanyu

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}


> [Slides](https://drive.google.com/open?id=113sC7qQpSK-UHxgFJ0M8tmQO0tG8YTmK)
> [Github](https://github.com/matrix0415)
- Sooci: 遊戲直播 APP
- 問題: 大家儲存了很多實況, 卻很少看它們 
- 改善方式: 導入精華剪輯
- 成效: engagement 增加, 減輕 MKT 負擔


## Data labelling and model selection 
- 從傳說對決開始, 因為最多人看
- 工人智慧標記場景 400 張 -> 餵給 pre-trained model -> 廉價勞工模型
    - 減輕真人負擔: 選擇題 -> 是非題
-  Model Selection: 重點是要提供 user 什麼體驗
    1.  快, 讓 user 可以迅速上傳分享
    2.  便宜, 需要機器資源比較便宜
-  採用CNN而非CNN-LSTM架構，因為訓練比較快，該作法是將影片切成一張張圖片辨識。
- SqueezeNet 速度快, 在 Imagenet 較不準
- 相對於ImageNet要預測一千個類別，商業問題上可能不需要這麼多類，就可以考慮比較輕量的架構。

## Training strategies
- early stop: 10次迭代內結束
- 15分鐘就可以訓練好 再進行調整
## Highlighting prediction
- 剪擊殺畫面: 訊息前 4 秒 & 後 1 秒
- 問題: 
    - 雖然出現擊殺訊息，但不是當事人
    - 跳出 APP 畫面，到其他 APP，卻誤判是擊殺
- 解法: 
    - 加入 features (英雄別、英雄密度...)
    - 擊殺訊息出現三秒才算

## Real world application
- MKT 進一步剪輯發布
## What’s next
- 移植到其他遊戲
    - 降低 learning rate 修改原 model
- 利用模型預測的 output 給 user 即時戰略回饋與建議

# Q&A
- 英雄密度 label 方式?
    - weakly supervised learning: 直接 label 畫面有幾個人
- 為何壓縮 224*224
    -  一般論文使用大小
- 為何不擷取部分畫面分析?
    - 訊息會出現在畫面中不同區塊, 也希望同一個 model 可以直接用在不同場景
- 為何不每個 event 建各別的模型?
    - prediction 成本變高, 一張圖要餵六個模型
- kill 跟 playing, dead 相似，所以改用 sigmoid
- 用 keras 是希望能快速 prototyping, 縮短開發時間
- 大家可能只想看自己的英雄片段, 怎麼解決?
    - 加入人口密度某種程度有解決這個問題
    - 只看自己成本太高，需要 object detection，也難複製到其他遊戲
- 秒數是 based on domain knowledge 嗎?
    - 是的, 也考量到精華要很短
- 是否想過把 MKT 剪的丟進 GAN 去 train?
    - 是不錯的改善方向
- 幹話的精華?
    - 接下來的方向之一, 預計從語音下手

###### tags: `pycontw2018`
