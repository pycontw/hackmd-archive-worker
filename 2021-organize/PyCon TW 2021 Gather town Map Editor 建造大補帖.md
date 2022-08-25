---
tags: 2021-organize, gather.town, gather, gather town
---

🔙 Back to [歷年 PyCon TW Organizing 共筆](/ryPr7SFyP/%2FHM5mHCFKQCu7-W5ea8ITcw%3Fview)
🔙 Back to [PyCon TW 2021 Organizing 共筆](/Wb9vQrfJQk-5tPoPR23hwA)
🔙 Back to [PyCon TW 2020 Organizing 共筆](/5u84SOprTUeQYBR57TH49w)

# PyCon TW 2021 Gather town Map Editor 建造大補帖
**創建自訂地圖**
* 地圖空間的命名無法修改
* 編輯完記得存擋才會更新在空間裡面 (應該無法多人同步編輯，可能會覆蓋變動)
* 雖然放滿裝飾小物很療癒，但也會大大拖慢載入速度，請適量就好，不要每個人桌上都放一杯咖啡一本書。
* 直接把無互動功能的物件畫在背景裡，能加快空間載入速度。

**Ｗall 牆面 （背景、前景）**
* 房間左上角至少從地圖的（1,5) 開始建構，藉此避免房間最上方的設計被玩家通話視窗遮擋。
* 每個 Gather Room 只有一個背景
* Tiled是一個第三方軟體，可構建自定義地圖。
* 官方的公共地圖集 https://github.com/gathertown/mapmaking 單擊綠色的“代碼”按鈕並選擇“下載 zip”
* PNG 支持透明度，這對於前景很重要，但如果背景中有透明空間，則會在地圖上留下黑色空間。

**Tile Effects  地磚效果**
* 人物踏上就會觸發效果。共分為以下五種：
* Impassable，就是不能過，讓角色撞到該撞的東西，Impassable 磚塊至少要沿著牆放一圈，才不會有人跑到地圖外面，也可以放在桌子、盆栽之類的應該要會擋住去向的東西上。如果沒放你就會看到有人穿牆或穿越盆栽和櫃檯。

* Spawn，第一次進入空間或是萬一卡住，使用者可以按自己畫面下方的角色頭像，可以看到 Respawn 的選項，按了以後角色就會重新出現在 Spawn 的磚塊上面。一個空間至少要有一個spawn點，建議直接設置一片區域。

* Portal，傳送門，如果你多蓋了好幾張地圖，可以用 Portal 連接起來，造成往外走到另一個空間或上下樓的效果。

* Private Area，私人區域，也就是這塊區域裡面聲音、視訊都共享，但是只要一走出去就完全聽不到。可以建造會議室，這樣就不怕有人沒聽到，也不怕有非與會者聽到了。同一個區域編號地磚會一樣，所以要注意一下，不要把兩間會議室都設成一樣的編號，否則就會一直聽到隔壁會議室的聲音。

* Spotlight，聚光燈就是廣播，只要踩到這種地磚，就會擴音給空間內所有的成員聽到，適合需要公告的時候使用。要特別注意！！地磚在使用介面上不會顯示出來！！所以最好用一些標示物件（比如標出 Spotlight 免得誤觸廣播）、地毯或隔間可以標出私密區域的範圍。


**物件**
* 物件圖片可自行設計上傳，尺寸限制為32*32 pix
* 物件可具備互動功能：1.嵌入網頁 2.嵌入圖片 3.嵌入線上影片 4. 嵌入通訊軟體連結 5.嵌入留言訊息（文字內容）


**外部參考資料**
[Gather.Town Custom Map Creation](https://docs.google.com/document/d/e/2PACX-1vQrz8JSQv83CfoOXWm4Ja03BITBlV9GDdTbcPQ1uZUXrkd-34FWxnD4vHdFgxAAoNZrmCQEtBV7XP8Q/pub)

[inside ＧＴ攻略](https://www.inside.com.tw/feature/covid-19-digital-transformation/23708-how-to-gather-town)

## 許願參考

- quiet/noise room
- 無法開麥、不想開麥區  https://discord.com/channels/752904426057892052/845976899846275083/859147835513241611
- [name=JoJo] 大地遊戲 --> 類伊底帕斯地圖 ref https://discord.com/channels/752904426057892052/759696531237896212/870339108910809118