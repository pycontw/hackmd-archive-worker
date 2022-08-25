# Build and Host Real-world Machine Learning Services from Scratch - 曾君宇

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}

> 從這開始
      

## Chapter 2 (Enable)
  * Send camera streams to cloud
        * AWS
        * ~~Kurento~~ Websocket[(ZeroMQ)](https://zeromq.org/)
## Chapter 3 (From Chaos to Stability)
## Chapter 4 (Data Data Data)
* Is data or algorithm more important?
* Unexpected images in night mode
* Collect more data, and tweak ML
## Chapter 5 (Refactor)
* Python 2 to 3
    * byte string / decode
    * isinstance
    * format
    * API changes
* Adopt asyncio
* Torch to PyTorch
    * Lua => Python
* Debug
    * pyflame to profile program
    * tracemalloc to trace memory
## Chapter 6 (ML pipeline)
* Workflow iteration between research, ai_eng, customer
* Not only pipeline or automation, but also SOP.
* Have clear goals, practical user stories, and enough resources before building the pipeline
* Current progress
    * Data collection
        * 需有一層 data access layer，提供存取的人有此次存取的資訊檔（e.q. 存取了什麼樣的資料），才可以跟其它使用的人比較用來訓練 model 的資料有什麼不同
    * Model training
        * [Kubeflow](https://www.kubeflow.org)
    * Model evaluation
        * 建議有共用 library，讓每個人的 evaluation 一致，降低差異的可能
    * Model deployment
## Chapter 7 (Production readiness)
* Cost
    * Cloud
        * Computing/Network => architecture
        * GPU => throughput + algorithm
    * ML pipeline
        * Computing
        * GPU => provider (ex: TWCC臺灣AI雲 gpu - 國網中心) + integration
        * Labeling => automation
* SLO and maintainability
    * SLO
        * Monitor first
        * Setup alerts
        * Oncall process
    * Maintainability
        * DevOps
        * Adopt engineering best practices
## Chapter 8 (Edge)
* Why edge device?
    * Lower cost
    * Less latency
    * Less network consumption
* AiCamera
    * Edge + Cloud
        * 例如：當 edge 無法處理時（例如環境問題），傳到 cloud 處理





###### tags: `PyConTW2019`
