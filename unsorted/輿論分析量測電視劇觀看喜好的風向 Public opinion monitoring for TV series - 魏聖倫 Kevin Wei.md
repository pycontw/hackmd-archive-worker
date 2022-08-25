# 輿論分析量測電視劇觀看喜好的風向 Public opinion monitoring for TV series - 魏聖倫 Kevin Wei

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}


# About me
- 2014 ACM: 命名實體辨識與分歧異挑戰 (SIGIR Entity Recognition and Disambiguation Challenge)
    - 搜尋*王建民*時不知道是map到哪個人
    - 搜尋*王建民 洋基*時就可以確定
- 2016 COLING: NL2KB Resource
    - 偵測實體之間的關係
- KKStream Applied Data Science Team
- ccClub Python 讀書會 in NTU since 2016 Fall 

# KKTV
- 現場聽過的人7成
- 現場使用過OTT(over-the-top) 約4成

- 版權問題
    - OTT業者需要取捨

- 內部data分析喜好綠？
    - 內部data可能有問題，可能與觀影民眾的分布不同
    - 改用外部data

- 分析論壇熱度？
    - 期待度低可是上映後很受歡迎 (黑馬)
    - 期待度高可是上映後不受歡迎 (地雷)
    - 期待度高，上映後也很熱門

# 流程
1. 收集與論資料(Data Collection)
    - collect forum posts (如PTT)
2. 整理資料，分析出metadata，如該篇文章代表的劇名(Data Process)
    - [Named-entity Recognition algorithm](https://en.wikipedia.org/wiki/Named-entity_recognition) 簡稱NER
    - 預先定義好的category，稱為entity
        - 如洋基隊是organization
        - 如洛杉磯是Location
    - 電視劇標題的 NER
        - 目標：從標題找到 Entity Name 來確認文章主體
    - Google Natural Language API 測試？
        - **逃避可**恥但有用ep9 劇組請加油
        - 標出了*逃避可*為Other category
        - 對電視劇名稱效果不好(因相較"體育"，非熱門領域)
    - 字串比對？
        - 王牌大律師 vs 勝者即是正義 vs Legal High
        - 月薪嬌妻 vs 逃避雖可恥但有用 (不同翻譯)
        - 逃恥 vs 月薪 (不同縮寫)
        - 逃避可恥但有用 vs 逃避雖然可恥但有用 (typos)
    - Typos:從使用者搜尋紀錄來看
        * 經常請吃飯的漂亮姊姊
        * 漂亮姐姐經常請吃飯
        * 經常請你吃飯的漂亮姐姐
        * 經常請我吃飯的漂亮姐姐
        * 經常吃飯的漂亮姐姐
        * 請我吃飯的漂亮姐姐
        * 每天請吃飯的漂亮姊姊
        * 請漂亮姐姐吃飯
    - Our NER Algorithm
        * 理想：解決上述所有問題
        * 觀察：找出規律性
            * 有書名號的標題可以拆出劇名
            * 使用語言上先天的特性來找出重點(Language Feature)
            * 尋找與標題相關的內容，而且內容有書名號
        * 把文章標題拿去查google，可以發現內容有書名號
        * 將從google中取得的數個term(含count數) map 到 wikipedia，看會指向哪個劇名，最終再基於count數進行多數決
    - 問題
    - 
        - [新聞] 新垣結衣堺雅人續集戰開打《月薪》恐讓
            - <<月薪>> -> 工資 (knowledge domain的重要性)
            - 當文字不夠特別時，在wiki有可能錯誤比對，就需要換Resource做比對
    - 思考
        - wikipedia不是好的查詢term的工具
            - 改用偶像資料庫網站, 影評網站
        - 盡量把垃圾移除
            - 如單集的感想
    - NER Evaluation
        -  Human label ground truth from PTT KoreaDrama
        -  2018四月共296篇
        -  準確率 76%
    - Code

3. 不同觀點切入做資料分析(Data Analysis)
    - 應用數據
        - 每周產生報表
        - 可看每個電視劇的文章數，爆文數、推噓文數
        - 時間關係圖表
        - 正在上映時討論熱絡，剛放映結束就冷了
            - 放映結束後還繼續維持討論熱度的可能是好選擇

## 結論
- 監視輿論來獲得社交資訊，如使用者偏好
    - Developed a public opinion monitoring system to collect social information
- 結合平台上的使用者行為來幫助 OTT 決策要買什麼電視劇
    - Combined them with end-user behavior in KKTV to facilitate decision making for content team and marketing team
- 不需要電視劇名稱清單
    - Designed an entity recognition algorithm to detect title names for TV series, reaching 76% accuracy without using existing drama list. 

## 工商服務

ps. 

## 提問

- 有沒有要使用machine learning？
    - 這是多分類問題
    - 目前的方式已經足夠
    - 不認為machine learning提高的辨識率值得將要投入的資源
    - 想要集中資源在backend service
- 有沒有辨識該留言的情緒？如正面留言，負面流言
    - 正在做，目前詳細內容是機密
    - 大部分內容提到演員會用角色名
        - 除了少部分例外，如：結衣我老婆
    - 正在做角色與演員對應資訊

## 相關文章

* [看劇「完食率」：KKTV 提高營運效率的新數據武器！ \- INSIDE 硬塞的網路趨勢觀察](https://www.inside.com.tw/2018/05/17/kktv-view-achievement-rate)
* [輿論分析量測電視劇觀看喜好的風向 – KKStream – Medium](https://medium.com/kkstream/%E8%BC%BF%E8%AB%96%E5%88%86%E6%9E%90%E9%87%8F%E6%B8%AC%E9%9B%BB%E8%A6%96%E5%8A%87%E8%A7%80%E7%9C%8B%E5%96%9C%E5%A5%BD%E7%9A%84%E9%A2%A8%E5%90%91-c9c4993f959d)

###### tags: `pycontw2018`
