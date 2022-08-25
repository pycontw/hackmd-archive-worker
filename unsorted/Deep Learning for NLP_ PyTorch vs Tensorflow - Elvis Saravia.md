# Deep Learning for NLP: PyTorch vs Tensorflow - Elvis Saravia

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}

 
* 簡報: [Deep Learning for NLP \(PyCon\) \- Google 簡報](https://docs.google.com/presentation/d/1cf2H1qMvP1rdKUF5000ifOIRv1_b0bvj0ZTVL7-RaVE/edit#slide=id.p)
* [Deep Learning for NLP: PyTorch vs Tensorflow](https://paper.dropbox.com/doc/Deep-Learning-for-NLP-PyTorch-vs-Tensorflow-uLd5vxnoJ78Dl3WNqO6MG)


1. About Emotions
    -挑戰:沒有統一定義的情緒


# 選擇 framework

- pytorch
    - 2016
    - 動態有向圖 (DAG)
    - 執行時偵錯
    - 需要看蠻多手冊說明
    - 需要手動來跨平台
    - 不支援分散式學習
    - 資料平行化簡單
    - 幫你包到好
    - 容易上手
- tensorflow
    - 2015
    - 靜態有向圖 (DAG)
    - 開始運算前就要決定(先決定架構，才做運算)
    - 使用特定的工具偵錯
    - 跨平台很簡單
    - 支援分散式學習
    - 資料平行化較難
    - 很多事情要手動處理
    - 適合產品化

- 講者是研究者，想快速做實驗，所以選pytorch

# 資料

- 如果句子中的hash tag有情緒就能用來當tag

- 講者推薦這個dataset: 英文和印尼文https://github.com/huseinzol05/NLP-Dataset/

## 資料轉換

需要先處理資料
- Bag of words(詞袋)
- n-grams
- Character embeddings
- Word embeddings
## Bag of Words

將句子中每個字代表的情緒取出，只記錄該句子包含哪些情緒

- 句子有出現的詞 -> 1, 沒出現 -> 0
- 但無法保留詞序、無法處理否定句： Good, not bad跟Bad, not good組成字相同所以vector相同，但意思完全相反

## one-hot encoding
使用 one-hot encoding 來保留句子中單字的順序
- 無法辨識相同意思的句子

## Word Embeddings
- 用機器學習將詞轉為向量
- Continuous Bag of Words(CBOW)[https://zh.wikipedia.org/wiki/Word2vec#Skip-grams%E5%92%8CCBOW]
- 使用預先訓練過的model(pre-trained model)或自行訓練model

## 如何自行訓練 word embedding model
1. 給每個詞一個 id
2. X 是 Y 前後的詞
    *  e.g. feel(X) awful(Y) about(X)
3. Train!
- 使用 tensorflow
    - 較關注於架構 
    - 存模型的方式較彈性
- 使用 pytorch
    - 只需要知道input 與 output，不太需要知道內部參數的細節(implicit) 

# 訓練

- 為什麼使用 LSTM
    - 句子中的字與該字之前的用字有關
    - 需要保留順序
    - 句子長度不同

## 步驟

- 分割資料，驗證，測試
- 將句子切成字
- 用 word2vec 轉換
- RNN 處理 (padding很重要)
- Bucketing比padding更有效率。可參考 https://goo.gl/h6Z9kU


# 結果
- 準確率 89.9%
- TensorFlow 和 PyTorch 的訓練時間和結果差不多
- love與joy的情緒不容易分辨

## 延伸
- 試試 CNN models
- 使用不同資料來源，如演講等等
- 使用包含錄音、影像的文字資料

## 結論
- PyTorch 建立 models 比較簡單
- 使用 Tensorflow 可以學到更多底層
- Data 是效能瓶頸

# Q&A

- 你是手動還是自動產生每個字的情緒token?
    - 是自動的，用字與字在同一份文件中出現的頻率
    - 利用同義詞
- 你如何處理中文字等等不同語言？
    - 只要有字庫就可以處理，但是我沒試過中文跟日文
- 就我所知，tensorflow可以保存model到檔案，請問pytorch也可以嗎？
    - 可以 [ONNX](https://onnx.ai/supported-tools)


###### tags: `pycontw2018`
