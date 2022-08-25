# Useful tools to explain ML models - Jack Pan

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}

> 從這開始

* 主講者背景：金融業
    * structure data 為主
* Apply for a Credit Card
    * 估計信用分數
    * 銀行需要知道「為什麼」某些客戶沒有 pass
    * 要能去解釋模型
* Linear Regression 因為夠簡單，所以容易解釋
    * 看係數就知道某些 feature 的重要程度
* P-Value: 判斷統計上是否顯著的指標
    * scikit-learn 沒有
    * `statsmodels.api as sm`
    * `model = sm.OLS(Y,X).fit()`
    * `model.summary()`
* Tree Based Models
    * decision tree
        * 如果只有一棵樹，可以直接攤給客戶看
        * 但是怎麼知道哪些因素比較重要？
    * random forest / gradient boosting
        * 多棵樹，更複雜
        * 更難知道哪些因素比較重要
    * feature importance
        * 一種算法：看它在第幾層？
        * 一種算法：entropy 減少了多少
        * 多顆樹就直接平均
        * 但是這不是客戶要的 => **全局**性解釋
            * 客戶要知道因為什麼原因
            * 而不是哪個 feature 重要
            * => 需要**局部**性的解釋 （相比較於「**全局**解釋」）
* [SHAP](https://github.com/slundberg/shap) - (SHapley Additive exPlanations)
    * Additive Feature Attribution
        * 可以指考慮部份因素便計算結果
    * Shapley Value: 合作博弈論中的解決方案
        * 賽局理論
        * 各種排列組合，並根據可能性去給 weights
    * TreeExplainer
        * 設立基準值，並根據特徵加減分
        * 可以透過產生報表，知道因為哪個特徵扣分 => 可解釋（**局部**性解釋）
        * 透過比較各個特徵對結果的影響可算出**全局**性解釋（未考慮特徵的先後順序）
    * Neural Network
        * can not handle null features
        * 需要 reference point
        * gradient is not always correct
    * Explainers: 解釋器
        * TreeExplainer
        * DeepExplainer
        * GrandientExplainer
        * LinearExplainer
        * KernelExplainer: All model can use.
    * How can we use it
        * 看單一 feature
        * 看多個 features 交互性
        * 可以藉由解釋模型來基本健檢我們的 model
    * Limitations
        * require computation resources especially when we are note using TreeExplainer or samples are large
        * DeepExplainer for deep learning models works. However, how you choose reference samples will affect the result
            * Q: 不能用平均嗎？ 但講者認為實際上不是這樣，因為有些特徵彼此之間是有交互性

* Others
    * [Eli5](https://eli5.readthedocs.io/en/latest/)
    * [Skater](https://github.com/oracle/Skater)
    * [LIME](https://github.com/marcotcr/lime)
    * [DeepLIFT](https://github.com/kundajelab/deeplift)
      
###### tags: `PyConTW2019`



