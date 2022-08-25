# 寫個能幹的中文斷詞系統…然後讓它養我 - PeterWolf

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}

> 歡迎大家到 https://api.droidtown.co/ 試玩 Articut 中文斷詞。
> 如果有覺得「斷詞結果切得不好的句子」，可以直接到 https://www.facebook.com/Articut 貼出來讓大家笑一笑呀！XD
> Talk 中的簡報、錄影以及測試程式原始碼：https://github.com/Droidtown/PyConTW2019
      * 中文的古文遇到特定的字，會有類似標準符號的停頓

## 中文三歧義

* 組合型歧義
    * 小紅帽
        * 小/紅帽
        * 小紅/帽
        * 小紅帽
* 真歧義
    * 美國會派特使來訪
        * 美國派出？
        * 美國國會派出？
    * 「語言層」和「知識層」維度(而不是依據頻率)
* 交集型歧義
    * 我幫爸媽買了一份超值保險套餐
    * 你再做一次試試看！
    * 「語言層」和「語境層」維度

## 語言學概論

* 現代理論語言學提出的句法樹結構**X-bar**(70年, 61087顆樹)
    * 語言學家的心中只有一棵樹
* 語言學假設
    * 所有人大腦結構一致
    * 所有人有一樣的語言處理機制
    * 人類的母語語言習得機制允許參數改變
    * 所有語言的差異是來自參數的差異
    * 參數的變化是有限的
* 中文/日文可以用同一顆句法樹 + 參數調整
    * 因為大部分語言學家不會程式，所以發展受限

## Articut 斷詞引擎

* 詞性與斷詞同時發生
* 以結構來處理，而非使用大數據訓練的模型
* 錯誤是有可解釋性的
* 犯錯是知識(常識)的缺乏，但因為有可解釋性，所以修正起來很快，相對於頻率統計學派，只能表示是因為訓練資料的受限，但不知道確切的原因。
    * 範例
        * 餃子 / 包 / 高麗菜
        * 麵 / 包 / 牛奶
        * 借600萬養老金
            * 借 600 萬 / 養老金
            * 借 600 萬 / 養 / 老金
        * 魅力無窮
            * 魅力 / 無窮
            * 魅力無 / 窮

* 測試資料：
    * 四十年 前 的 這 一天 台灣 關係法 通過 了 促進 臺美 關係 (可分辨"關係法"與"關係")
    * 齁 盡量 不要 買 武器 了
    * 今天 台北 忠孝東路
    * 這時 川董 拿出 鋼筆 開始 簽名 在 杯墊 上

* 效能比對: Articut 92.55  vs. CKIP 97 
    * 請語言學碩士逐條比對 93~94就是頂天了，97就overfit了

## RE

* re 抓地址
```python
# Test on Python 3.5, 3.6, 3.7
import re
pat = re.compile('\d樓|\d號(\d樓)?')
re.findall(pat, '4號') # [''] re bug!
re.finditer(pat, '4號') # Correct!
```


> Note Due to the limitation of the current implementation the character following an empty match is not included in a next match, so findall(r'^|\w+', 'two words') returns ['', 'wo', 'words'] (note missed “t”). This is changed in Python 3.7.
> 

* finditer() 沒問題, findall() 有問題

## 中文斷詞

* 工具：
    * Jieba
    * CKIP
    * Monpa
    * CKIPtagger
* 罕見句表現：有能力得出兩種結果，才是和人類一致的斷詞處理。
    * 我 想過 過 過兒 過過 的 日子 (我思考過這件事)
    * 我 想 過 過 過兒 過 過 的 日子 (我想要去試試看這件事)
* 詞性記轉品表現
    * 努力 / 才能 / 成功 vs. 他 / 的 / 領導 / 才能 / 很 / 突出: Articut 可分辨「才能」在兩種句子裡的詞性轉品。
* CKIPtagger 命名實體辨識 (NER)
    * 復活島 北方 兩百 公里 處 發現 失事 殘骸
        * NER => 兩百公里
    * 北方 兩百 公里 處 發現 失事 殘骸
        * NER => Nothing...
* 使用機器學習或統計方式完成斷詞、POS、NER 的模型訓練：
    * 95% 中文斷詞 CWS 正確率
    * 93% POS 正確率
    * 80% NER 正確率
    * 最終產品正確率基礎： 95% x 93% x 80% = 70.68%
* 使用時直接比對答案完成 NER 的標記，再使用句法樹「一次完成斷詞、POS」：
    * 92.55% CWS/POS 正確率
    * 最終產品正確率基礎：92.55% x 100% x 100% = 92.55%
    * CWS 的正確率就是 POS 的正確率，因為兩者是同時發生的。故以 92.55% X 1 即為 CWS x POS 的正確率。
* 中文分词十年又回顾: 2007-2017 https://arxiv.org/ftp/arxiv/papers/1901/1901.06079.pdf
* 賈文杰

## 有誰採用語言學規則做為解決方案呢？(Rule-Base)

* Droidtown: Articut (文截)
* bitext: NLP core
* UCI 加州大學爾灣分校：Language Science


###### tags: `PyConTW2019`
