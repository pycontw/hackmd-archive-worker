# Keynote - 陳昇瑋

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}

簡報檔：https://www.slideshare.net/swchen11/ss-97741195

{%slideshare swchen11/ss-97741195 %}

## 斜槓中年
- 在中研院工作，知道每年pycon都在這，但這次第一次來
- 寫ACM，念博士
- 200x年寫書
- 第一個資料分析工作：20 個小時的遊戲封包（phD 畢業後）

## Change is the only constant.
- 先有飛機才有雷達，有雷達後聽飛機來的人就失業了

## Deepmind
- 第一版 AlphaGo 只針對 GO
- 第二版 AlphaZero 針對所有封閉規則的遊戲
- 沒有規則的情況？
- 軍備競賽（硬體還是太貴，可以用租的但費用負擔不起）

## pattern recognition
- Polanyi's Paradox: 我們懂的事情，比我們能表達出來的更多
- 舉例：[狗臉 vs 餅乾臉](https://i.imgur.com/TTpIGvo.jpg)
- 機器選擇的pattern 或許會比人類選擇的還要來得有用

## 深度學習
- multi-layer patterns
- 優點：可以做的比人精準（同性戀偵測機器準確率80 ~ 90%，人類50 ~ 60%）
- 缺點：人類無法去解釋（問作者為什麼：作者無法解釋）

## Google如何用深度學習
- 兩年半前有超過兩千個計畫
- 舉例：只要有「常數」的部分，都可以用深度學習預測（例如 memory allocation）

## 關係圖
- 機器學習不容易處理高維度問題（非結構資料），例如音訊。
- AI > Machine learning > Representation learning（高維度問題） > Deep learning (大多數研究在這塊)

## 哪些東西適合機器學習
- 有足夠樣本
  - 不適合：第三次世界大戰，七級以上地震
  - 適合：德州撲克，金融
- 容錯率夠高

## 大預言
👻 十年內，machine learning 是軟體工程師必備技能 👻
- 學python是不會錯的，因為大家都用他學。

## 初學熱門項目
- Classification: 自動上色（黑白照片->彩色照片)
- GAN: 自動產生圖片
  - BEGAN :(https://github.com/carpedm20/BEGAN-tensorflow)
  - WGAN
  - conditional GAN
- Deepfakes
*編按：每個範例都一定要放一個ACG範例* 🤔🤔🤔🤔🤔

## Types
- reinforce learning（門檻較高）
  - Geoffrey Hinton (Google): 未來的重點是這個
  - 從錯誤中學習，一定要有一個模擬器
    - 18個關節的人跑步，最後發現重心可以往前；8個關節蜘蛛；18個關節的人站起來
    - 跨越障礙
  - 應用：無人機、自駕車...
- supervise learning
- unsupervise learning
*編按：他前面都在講後兩者（從alpha go開始，但這頁講分類的投影片出現在這）*


## 台灣之於世界
- 都沒有位子：Cloud, Mobile, Social, IoT, Big Data/AI
- 跑台灣各公司看狀況：沒人才，找到人才也不知道怎麼做
  - 發現一些適合的項目：焊接目檢，預測ＸＸ何時壞
  - 弄完後發現沒有辦法規模化，因為人才不足，所以開始搞教育

## 教育內容 ~~工商時間~~
- 台灣人工智慧學校 （http://aiacademy.tw）
-第二期，考五科：入取率210/500
  - 第一週機率統計，第二週就開始搞機器學習

## Take home Messages
- 今天的AI如同1994年的WWW
- 今天學ML如同1994年學CGI/HTML
- 所有人都相信AI現在才剛起步
  - 建議往semi-superviser transfer reinforce 方向發展- Transfer 
  - 建議若CNN, RNN… 等基本模型已經了解的可以往GAN、Transfer Learning 和 RL 學習，因為這是趨勢也比較多殺手級應用
  - AI技術可能有機會像10~20年前大家學HTML一樣，不過學習門檻確實比較高，但機會相對也更多




###### tags: `pycontw2018`


-> 演講完後會在玉山的攤位到第一天中午。