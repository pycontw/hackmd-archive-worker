# 該怎麼樣（認真的）部署你的 Python Web 應用程式? - Andy Dai

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}

* 簡報 https://www.slideshare.net/daikeren/python-web-100066618


## 關於我

- Andy Dai
- Taipei.py 創始者之一
- Django, Python, DevOps

## (隨便的)部屬你的 Python Web 應用程式
- 找一台 ubuntu server
- 放 code
- gunicorn/uwsgi + nginx
- 用上面的關鍵字找到處都是教學
- 會遇到很多問題，下述

如果你只是要demo 這樣是可以的

## (認真的)部屬你的 Python Web 應用程式
- 如果他是一個長期的project
- 常常需要修改，維護

## 認真！
- 手動容易出錯，所以要做自動化deployment
- 開發的不同階段需要不同環境來測試 (staging, QA, Production)
    - 容錯程度不一樣
    - 危險的測試可以在 staging QA 等階段測試
- 因為一定有bug，所以 rollback 要很容易
- 因為要~~抓戰犯~~釐清狀況，讓開發者/管理者可以輕鬆得知每個環境系統設定與狀態
    - 有哪些服務？版本為何？修改時間？

## 從開發到部署的pipeline
- Repository
- CI (Continuous Integration 自動整合) & Build Artifacts
- Staging
- Release -> QA
- Deploy (one-button, auto push, push by janitor, ...)

## 如何實作pipeline？
- 管理你的code
- 管理你的佈署環境
- 保持 master branch (或其他release branch) 為可以部屬的狀態
- Tag 

## 管理你的code
- 版本控制
- 明確宣告dependency [(請參考「這樣的開發環境沒問題嗎？ - Tzu-ping Chung」)](https://hackmd.io/c/pycontw2018/%2Fzh2DOHnoSXiVwYo4x6LGQg)
    * pipenv, requirements.txt
    * requirements中**鎖定版本**很重要
        - 沒鎖版號可能在其他電腦會跑不起來
- 把 config 放到環境變數中
    * Database, cache, File Storages 的選擇 ...
    * 不同環境下會有不同 Config （開發，測試，正式環境）
- [The Twelve-Factor APP](https://12factor.net/)

## Continuous Integration
- Why CI
    * 我要如何知道 Repository 上面的 Code 是好的？
- Jenkins, CircleCI, Travis-CI, CodeShip, Drone, 太多選擇了
    * 講者偏好看設定檔案的語言
    * 看設定跟語法適合性
- 沒空寫測試？至少做完基本款
    * 安裝套件
    * linter
    * 把 Application 跑起來
    * 對所有的 URL 發 request
- Build Artifacts
    * Artifacts -> 可發佈的單元
        - tarball, Python Package, ubuntu package, docker image, AMI image 等等都是

## 管理你的佈署環境
- Cloud? Data center? 公司的server?
- Infrastructure as Code
    - 使程式碼來描述建立你的infratructure
        - Ansible, Chef, Puppet 等等
        - **Terraform(推荐)**, CloudFormation（不好debug） 等等
        - Kubernates (k8s)，~~Docker swarm GG~~
    - 優點
        - 自動化（確保每次建環境都是一樣的）
        - 可以重現（避免只有某個人會手動建環境）（快速 migration to others infra, e.g. AWS to GCP)
        - 可以被 Review（享受Code Review的優點）
    - YAML 格式
        - 把所有環境參數都寫入
- Infrasturcture Repository 當做為整個系統的 Single source of truth
    - 不存在 Repository 中的東西就不存在系統中 (如果不在 repository, 理論上就不該在系統中)
    - 所有東西都有版本控制，歷史都可以檢查
    - DevOps (DEVelopers can do OPS.)
        - 等等會 Demo
    - 所有使用與version control相關的整合工具/流程都可以使用
        - Code Review, Pull Request
        - Issue Tracking
        - ChatBots, ChatOps 或是任何你想的到的應用
    - 一切透明
    - 知識分享，**code == 更好的文件**

## 範例
用pull request更新建立環境用command，寫在yaml config內

## Repository Structure
- Application Repository
- 不同環境的 Infra 放在不同 Repository 中
- 程式碼的更新會連同 stage/qa 環境的更新
- 更新 Production 環境只能夠靠 pull request
    - 怖屬新版
    - Rollback回舊版

## Demo
- Github Flow
- CI 是 Google Container Builder + GKE
- Staging 永遠跑著最新的 commit tree
- tag 做 release，自動部屬到QA環境
- Production 環境跑正式的 code

[daikeren/pipeline-application 程式碼](https://github.com/daikeren/pipeline-application)

- 可以使用 service 提供的 build-in 環境
- Google Container Builder 會自動來 Github 更新 version 與 tag
- merge 修改的 commit 到 master
- 使用 Github 的 release 功能，同時 Google Cloud Platform 會開始建立新的 Docker image

## 認真佈署還要做啥？
* Logging
    * Centralize Logging - 把所有你需要的 log 都集中在同個地方
    * Why?
        * 分散式系統時代，無法一台一台看
        * VM/container 直接死掉，無法進去查
    * ELK (Elasticsearch + LogStash + Kibana), Graylog
* Error tracking
    * 把 error tracking service 獨立出來
        * 最 critical, 最需要被注意
        * 有些 error 未必有 log
        * 主動通知 v.s. 事後查 log
    * Sentry, Elastic APM, ...
* Monitering
    * 拉完圖表只是開始
    * 不斷優化，找出對系統重要的metric
    * 發出警告，及早發現，及早治療，如：CPU用量>90%
    * Promethseus, Grafana

## Q&A
- 有用過 docker swarm 嗎
    - 有，但是還是輸了，docker官方選了k8s
- 怎麼保證 production 的錯誤在 staging 階段就被發現？
    - 如果是流量大才會發生的錯誤，staging無法重現，那可以用紀錄工具紀錄production流量，然後在staging環境模擬重現


###### tags: `pycontw2018`
