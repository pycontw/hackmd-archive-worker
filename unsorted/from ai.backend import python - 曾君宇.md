# from ai.backend import python - 曾君宇

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}

[toc]

* [Umbo](https://umbocv.ai/) CV AI Engineer
* [slide](https://www.slideshare.net/excusemejoe/from-aibackend-import-python-pycontw2018)

英國研究: 一個人沒辦法看超過12個畫面。


## infra

* 主力在 aws
* GCP
* Azure 主要做 CICD


## Backend lang
* go
* **python**
* nodejs


## Flow
* docker
* git
* Jenkins

## monitoring
* grafana
* papertrail -- log
* [sentry](https://docs.sentry.io/clients/python/)
* new relic
* kibana (EFK)
* Metabase -- 做更高層級的決策

## AI Eng. Jobs
1. Develop and maintain CV service 
2. Machine learning pipelines



> How much can the backend do?
> 87%
* infra
    * LB/ASG/VPC
* monitor
* develop
* maintenance


> Adopting python asyncio in large scale project

* Refactor Stream Manager
    * asyncio: breakdown a big business logic into smaller ones, which async/await
    * Use pipeline pattern (藉由Queue來實現)
    * Still use run_in_executor/ThreadPoolExecutor for blocking codes

* Result
    * cleaner architecture
    * high performance
        * GPU resources are the bottleneck
    * python package ecosystem

## PyTorch
* Refactor CV Worker
* Lua => Python
  * Torch => Pytorch
* Use [aiohttp](https://aiohttp.readthedocs.io/en/stable/) server

* Result
    * easier to maintain/upgrade

## Debug
* use [pyflame](https://github.com/uber/pyflame) to profile the program
* use [tracemaclloc](https://docs.python.org/3/library/tracemalloc.html) to find memory usage
* Use Valgrind to check your C++ Code


## 13%
* 事實上不止 13%
* Computer Vision and Machine Learning 
* ML learning curve is too step which is not easy to apply to production environment

## build our own ML pipeline
Structurized each step in ML into component and made them as a pipeline


## How to imporve your service
* Measure first
* New models / heuristics approaches
* Need to do training or redesigning
* need more (or specific) labeled data
* Training
* Need to compare with the existing ones
* get the best on production
* Measure again


cloud collection --> aumatic data selection --> data labeling platform --> dataset db --> train / test --> model design pepeline 
![Marchine Learning Pipeline](https://i.imgur.com/efFzsvH.jpg)

* Good references:
    * [Meet Michelangelo: Uber’s Machine Learning Platform](https://eng.uber.com/michelangelo/)
    * [Machine Learning Pipeline for Real-Time Forecasting @Uber Marketplace](https://www.infoq.com/presentations/uber-ml-architecture-models)


## Labeling platform
* can dispatch tasks to
    * our own labelers
    * third party partners
    * MTurkers
* Backend:
    * Flask + Plugins [flask-swagger](https://github.com/gangverk/flask-swagger)
    * NumPy
    * Celery/Redis/Pymongo
    * uWSGI


## Train Pipeline
* Can train you a lot of new models with different parameters

* backend
    * airflow
    * celery


## visualization platform
* Can visualize
    * the ground truth data
    * The evaluation results

* backend
    * flask + plugins
    * Numpy
    * SQLAlchemy

a faster pipeline means a shorter turnaround time.
speed matters for a startup


## what i have learned

* recap
    * services
    * pipelines: 需要和其他人 cowork，87% 也是 backend 的事情
* collaboration
    * researcher vs engineer
    * 去幫助 researcher 不要重工
* Domain Knowledge
    * Basic understanding of ML with practical experience
    * public dataset與實際dataset還是有差，在前者有好的performance不代表在後者就一樣能有好的performance
    * 即使訓練出有高performance的model，可能會因實際情況(GPU資源、網路頻寬等因素)，而有所取捨

* Pipeline未來可能服務化


Not totally agreed with today's keynote (AI will become mandatory things)


## Question
* dataset 的 database
    * 使用 mysql
    * 一開始只是介於 sql / nosql 做選擇，但因爲怕塞入髒東西到 nosql 所以最後就用 sql

* 為什麼不用 tf serving 而使用 aiohttp?
    * 因為沒有裝過 tf serving

* model 的版本控制？怎麼上線？
    * 正在設計中
    * 存一些  machine metadata
    * 上線：2 stages
    * 題外話，可以設計一些 event based 的 evaluation metric，因爲最後產品是針對有沒有發出 alert 來做判定，所以有這樣的 metric 是很有幫助的



###### tags: `pycontw2018`
