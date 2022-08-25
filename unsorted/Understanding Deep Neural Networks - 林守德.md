# Understanding Deep Neural Networks - 林守德

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}
      
###### tags: `PyConTW2019`

> 從這開始
>
## Toward better Understanding of a Deep Sequence-to-Sequence Model

* What is machine learning
    * Learn f(x) = y
* Traditional ML vs Deep Learning
    * Tradition: needs to pick features
* RNN (recurrent neural network)
    * Output is the input of next level
    * 類似遞迴的運作方式
    * Back propagation training
* RNN approaches
    * Vanilla RNN
    * LSTM (Long Short-term Memory)
    * GRU (Gated Recurrent Unit)
        * Variant of LSTM
        * 用 z 決定 h, h(t-1) 的權重
        * 各個weight都是train出來的
    ![GRU](https://img-blog.csdnimg.cn/20190224220747594.png)
    * *pic from: https://blog.csdn.net/u012328159/article/details/87907739*

* Use of RNN
    * Language modeling
        * y 對應到每個 character/word 的機率
    * Classification/Regression
        * 例如：檢查文法有沒有錯、預測文章讚數
    * Neural machine translation
    * Article summarization
    * [小冰寫詩]( https://poem.msxiaobing.com)

* Components of Seq2Seq
    * Encoder
        * Input representation: word embedding, CNN feature maps
        * e.g., Uni/Bidirectional RNN
        * Word Embedding: 把字轉成向量
    * Decoder
        * Bridge(Initial state of RNN)
        * RNN(Usually unidirectional RNN)

* Design of Decoder


* Train a Seq2Seq model
    * Loss
        * loss 反比於應該產生的字/詞機率

* Evaluation
    * Perplexity
    * ROUGE
* 我們無法了解機器是否有了解或推論，只能從他表現去間接推斷
* 很屌的換韻腳跟藏頭詩的研究：
    * How to varify this thing:
        * 他先 train 一個 classifier，輸入是他模型訓練好的 vector，然後就知道哪些 vector 是對應到這種韻腳（他的任務是輸出符合的韻腳），之後用 pca 之類的方法分析 feature，就知道是 vector 中的哪些 dimension 在控制 model 輸出這些韻腳，就可以開始話題，進而推論出 eos 是超過 threshold 就會 fire
    * Contribution：
        * 知道 eos 的機制其實是 neuron 會給你一個低於零的初始值，然後他會隨著 lenght 越來越長，值會越來越高值到超過 threshold 就會 EOS token
        * 知道 hidden state 比 output 有用，neuron 基本上都是看 hidden state