---
tags: organize, gather town, tutorial
---

# gather town 錄音教學

目的：本次大會使用 gather town 舉辦。本教學可用於紀錄 gather town 上雙向/多向的互動 event, e.g., pynight, open space, sprint, et al., 供後續使用。

需求：收錄 gather town 一個 private space 的聲音。

Approach：
 - brute force: 錄音師角色直接進入要錄音的 private space，以電腦 speaker 方出，再以手機 voice memo 收音（coscup 有在 sitcon 場地測試過此方法）
 - piping: 將 audio out 到一 virtual audio device，再對此 device 收音。以下將介紹以 VB-cable implement 此方法。

## 以 VB-cable 收音

* 至官網 （https://vb-audio.com/Cable/） 下載 VB-cable 並安裝
* 安裝完以後應可看到音源裝置多了 VB-cable
![](https://i.imgur.com/3B1l8sW.png)
* 開啟音效設定及任意錄音程式
![](https://i.imgur.com/vi9NFSs.png)

![](https://i.imgur.com/494TLUb.png)

* 進入 gather town 及確認進入要收音的 private space，確認聽得到聲音，待命。
* 將要開始錄音時，在音效設定將Output/Input 都設為 VB-cable
![](https://i.imgur.com/MhNsXna.png)
![](https://i.imgur.com/SK0r1uw.png)

* 開始錄音
* 結束錄音，恢復相關設定


注意事項
1. 在錄音的過程，聲音都被轉導到虛擬裝置，所以錄音師將聽不到任何聲音。
2. 建議進入錄音狀態後，現場主持人或工作人員可以協助透過 text channel 與錄音師溝通錄音結束或是其他狀況。
3. 若為重要紀錄，為避免失誤，建議每個 event 可以配置兩位錄音師備援