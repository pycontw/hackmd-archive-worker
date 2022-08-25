---
tags: 2021-organize, program
---

# PyCon TW 2021 衝刺開發 Development Sprints
* 日期 Date: 9/26  10:00 ~ 16:30 (台北標準時間 TST)
* 線下地點 Location: 八米共同工作空間 （台北市大安區和平東路二段107巷23弄6號，近科技大樓），僅工作人員及專案主持人
    * map: https://g.page/8meters?share
* Rundown: https://docs.google.com/spreadsheets/d/1fKimCtiVNuIvebypaZTVk2iT25SfuAI8Vetv4OpqvHM/edit?usp=sharing

[TOC]

## 如何組織一個衝刺開發 Organizing your Sprints

* 介紹你的專案 Introduce your project

    你可以在 HackMD 中詳述你的專案內容與特色，以及想要參與者協助的地方。你也可以錄製一個小影片給無法參與實體聚會的參與者，讓他們能夠迅速瞭解你的專案內容。例如一個簡短的教學影片，包括專案介紹與操作、如何佈建、測試，觀看 Issue、Pull Request 等等。讓參與者可以很快上手，並瞭解可以從哪開始著手貢獻。
    
    You can detail your project description and features in HackMD, as well as where you need participants to help. You can also provide a pre-recorded video for participants who cannot participate in the physical Sprints meetup so that they can quickly pick up the knowledge of your project. For example, a short tutorial video, including project introduction and functionality, how to deploy, test, view Issue, Pull Request, etc. Make participants get started quickly and understand where to start contributing.

* 與參與者互動 Interact with participants

    專案主持人可以透過實體聚會分享、信件、聊天群組 (Slack, discord) 等等與參與者互動，交流意見，並協助參與者貢獻你的專案。如此一來，貢獻開源便不受限於時間與地點，而是一個長期的社群經營。
    
    The project host can interact with participants, share ideas with each other, and help participants contribute to your project through physical meetup sharing, email, chat groups (slack, discord), etc. In this way, contributing to open source is not limited to time and place, but a long-term community promotion.

* 提供參與者貢獻的方向 Provide direction for participants to contribute

    你可以從專案中現有需要幫忙的 Issue 或是需要幫助的 Pull Request 中提供參與者貢獻的方向，也可以透過與參與者相互討論，尋找可以更好的方向。
    
    You can provide the direction for participants from the existing issues or pull requests that need help in your project, and you can also discuss with participants to find a better direction.

* 你可以選擇是否參與 **9/26** 的 Sprints 聚會，帶領會眾一同貢獻你的專案，若 covid-19 疫情嚴重時，我們將透過線上的方式，組織你的 Sprints。
    
    You can choose whether to participate in the physical Sprints meetup on **9/26** and lead the participants to contribute your project together. If you cannot participate in the Sprints meetup, you can organize your Sprints online.

## 如何報名你的專案 How to register your project?

報名時間：8 月 27 日止
報名網址：https://docs.google.com/forms/d/e/1FAIpQLSd4e9F7CLF9nJQ1c5IeW9XtfUgjE3v3sbVF6D4FOsPJcEawgw/closedform （已截止）

## 如何報名成為參加者 How to register as a attendee?

在 [KKTIX 註冊頁面](https://pycontw.kktix.cc/events/20210926-sprints)

Register on [KKTIX Registration Page](https://pycontw.kktix.cc/events/20210926-sprints)

---

## 2021 專案列表 Projects List


### ScammerDisguise — A Loki NLU model that extracts the fake identities scammers in Taiwan court's verdict.
詐欺者的偽裝 - 一個用於分析台灣法院判決書中詐欺犯選擇的偽裝身份的 Loki NLU 模型
- **專案描述 Project description**:
The project's goal is to use Loki NLU system to extract scammers' disguised identites and draw plots to see if there is any difference among different cities/counties. This project is part of Audio_Hackiato - the most practical NLP/NLU applicatin Discord channel held at 10pm every two Thursday night. (https://discord.gg/PF8uG53KHw)
本專案的目標在於利用 Loki NLU 系統擷取出台灣各地方的詐欺犯偽裝身份並以圖形化的方式呈現其異同。本專案是 Audio Hackiato - Discord 上最實際的 NLP/NLU 應用討論頻道，隔週四的晚上 10 點開台。

- **專案連結 Project link**: https://github.com/Droidtown/Audio_Hackiato
- **專案聯絡人 Project Contact**: 
  - PeterWolf 
  - mail peter.w@droidtown.co
- **先需知識**:
  Participants will use Python3 and be given 1 Loki operating quota. As for the plotting module...well, it's TBD.
    參與者將使用 Python3 程式語言，並獲得 1 個月的 Loki 操作額度。至於用什麼模組來繪製結果嘛…我們再討論看看吧。
    
* 專案房間: Room 1
* 備用Google Meet連結： https://meet.google.com/sii-ykck-aok

---

### commitizen-tools

- **專案描述 Project description**:
  Create committing rules for projects 🚀 auto bump versions ⬆️ and auto changelog generation 📂
  
  [commitizen-tools](https://github.com/commitizen-tools/commitizen) 是一套可以協助團隊管理 git commit message 規範的工具，讓團隊能更容易寫出可讀的 commit message。除了提供符合 [conventional commit](https://www.conventionalcommits.org/en/v1.0.0-beta.2/) 的規範外，還有提供數種規範模板。另外一項很重要的功能自動跳版本號跟產生 Changelog，commitizen-tools 會根據最新 merge 回 main / master branch 的 commits 的內容來判斷該怎麼跳版（follow [semantic version](https://semver.org/) ）我另外有寫一篇教學文[Python Table Manners - Commitizen: 規格化 commit message]說明這個工具該如何使用。
  
  順帶一提，我還有兩個跟 commitizen-tools 無關的小專案可能也適合初心者一起參與 [
bahamut_ani_stat ](https://github.com/Lee-W/bahamut_ani_stat) (巴哈姆特動畫瘋資料收集、視覺化)、[pelican_stat](https://github.com/Lee-W/pelican-stat)（pelican site 過往文章資料收集、視覺化），但我主要會把時間放在 commitizen-tools 的討論上
  
- **專案連結 Project link**: https://github.com/commitizen-tools

- **專案聯絡人 Project Contact**: 
  - Wei Lee
  - mail weilee.rx@gmail.com
- **先需知識**：
    - Git
    - 請先按造 [Contributing](https://commitizen-tools.github.io/commitizen/contributing/) 上的教學設定環境

* 專案房間: Room 2
* 備用Google Meet連結：
https://meet.google.com/qif-uzgz-jcd
---

### Apache Airflow

- **專案描述 Project description**:
  從 Airflow committer 學習如何設定開發環境、選擇適合你的 issue、並提交貢獻。
  本專案會邀請 Airflow PMC member 帶領參加者進行。
  專案進行過程主要會使用英文；聯絡人會在現場協助溝通。
 
- **專案連結 Project link**: 
https://github.com/apache/airflow/

- **專案聯絡人 Project Contact**:
  TP
  uranusjr@gmail.com
  加入 [Airflow Slack](https://s.apache.org/airflow-slack) DM @uranusjr
- **先需知識**：
  需要基本的英語聽說能力。
  請先準備好 Docker 與 Git。
  如果是 Windows 則必須有 WSL2 (不支援原生環境或 WSL1 開發)。
  Python (3.6 或以上) 沒有也沒關係。
  請嘗試設定 [Airflow 的開發環境 Breeze](https://github.com/apache/airflow/blob/main/BREEZE.rst#prerequisites)；若有問題，我們會在早上時段協助排除。
  

* 專案房間: Room 3
* 備用Google Meet連結：
https://meet.google.com/yrt-qfju-qkx
---

### 1D shock tube calculator

- **專案描述 Project description**:
  - 改進既有的一維 Shock Tube 計算器，例如更友善與直觀的使用介面。
  - [Sprint 當日專案介紹細節](https://hackmd.io/7WfzJZ-HTuKxG_PyqGcFdA?view) 與 [介紹錄影](https://youtu.be/m9B_M8riFV8)
 
- **專案連結 Project link**: 
  - https://github.com/solvcon/shocktube1dcalc

- **專案聯絡人 Project Contact**:
  - Tai
  - email tai271828@python.tw
- **先需知識**： git
* 專案房間: Room 4
* 備用Google Meet連結：
https://meet.google.com/iii-xdwj-dmr
* 今日成果
    * Issue closed https://github.com/solvcon/shocktube1dcalc/issues/1
    * Issue closed https://github.com/solvcon/shocktube1dcalc/issues/4
    * PR merged https://github.com/solvcon/shocktube1dcalc/pull/9
    * New issue https://github.com/solvcon/shocktube1dcalc/issues/6

---

### 第一次做 PyConTW 粉專智能客服就上手

- **專案描述 Project description**:
用 Google Dialogue flow 訓練模型，然後串接臉書的粉專做出智能客服。後續會不斷累積資料來優化模型

- **專案連結 Project link**: 
TBD

- **專案聯絡人 Project Contact**:
  - David Jr.
  - mail davidtnfsh@gmail.com
- **先需知識**： git, python, etc.

* 專案房間: Room 5
* 備用Google Meet連結：
https://meet.google.com/ycf-scae-xvb
---

### 台灣生物多樣資訊入口網站

- **專案描述 Project description**:
  - 推廣國際間通用的生物多樣性資料開放格式
  - 協助各單位發布生物多樣性資料
  - 生物多樣性資料的倉儲與管理
  - 讓所有人都可以方便搜尋與下載資料
  
- **專案連結 Project link**: 
https://github.com/TaiBIF/portal20

- **專案聯絡人 Project Contact**:
  - 李思賢
  - mail moogoo78@gmail.com
  
- **先需知識**： git, Django, pandas, Jupyter Notebook, React, Apache Solr

* 專案房間: Room 6
* 備用Google Meet連結：
https://meet.google.com/ndi-dzxx-kqj

---
https://meet.google.com/vfs-qmqs-uf
### Integrative interface for analyzing open EEG/MEG datasets using MNE-Python

- **專案描述 Project description**:
近年來神經科學的研究開始提倡公開分享資料。其中腦波數據 (EEG & MEG) 的分析可以透過 mne-python 套件進行各式各樣的訊號處理、統計考驗、圖形化，以及應用機械學習模型進行心智活動的預測或分類。然而台灣的相關科系仍舊依賴以 matlab 為主的套件進行腦波數據分析。mne-python 已經開發了超過10 年，也在國際上累積了眾多的使用者，幫助科學研究者發表學術成果。本人與其維護團隊的核心成員長期保持聯繫。希望藉由本次 Sprints 專題達成一些目標，以促進台灣的資料科學與腦科學相關研究者掌握 open data ，並且享受 mne-python 的強大功能。
主要解決的問題如下：
翻譯下列資訊：
  1. 4 種核心 class 之說明 (raw, epoch, evoked, time-frequency)
  2. 數據前處理的範例
  3. 視覺化工具的使用方法
  4. 訊號源分析的流程
  5. 統計檢驗之流程
  6. 機械學習的使用流程
  本人在研究上常常需要將腦波數據與結構化的語料庫配對在一起
  雖然 mne-python 有說明頁指出可以用 Pandas 把類似 spread sheet 的資料與 EEG/MEG 數據整合在一起，但是這方面的範例很少。因此希望在這次的 Sprints 專題中，找到解決這個需求的人力與創意。未來打算將 NLP 的數據和 EEG/MEG 結合在一起，進行語言學習和神經語言學的研究。
  翻譯工作以及後續公開的平台將以 HackMD 進行 (比如下列附上的專案連結)
  
- **專案連結 Project link**: 
https://hackmd.io/zjSkT_l8SveKedWJw_9E5Q

- **專案聯絡人 Project Contact**:
    - 徐峻賢 (Kevin Hsu)	
    - mail neurolang@g.ncu.edu.tw
- **先需知識**： pandas, scipy, scikit-learn, matplotlib, numpy, markdown

* 專案房間: Room 7
* 備用Google Meet連結：
https://meet.google.com/yip-whnc-jht


---

### solid-file-python

- **專案描述 Project description**:
 Solid 是 W3C 推動的下一代網路應用標準及生態系。這個專案希望讓開發者能用 Python 投入此生態系，進行相關技術開發及存取。（https://solidproject.org/）
 
- **專案連結 Project link**: 
    - https://github.com/twonote/solid-file-python
    - https://hackmd.io/@SnrDbPy9TmeoTsDWzA-C5g/solid-file-python-pycontw2021
- **專案聯絡人 Project Contact**:
    - petertc	
    - mail petertc.chu@gmail.com
    
- **先需知識**： 
歡迎想認識新一代網際網路技術、想參與開源專案、對 OAuth 2.0、 Python 或 Javascript 有經驗的夥伴加入。
* 專案房間: Room 8
* 備用Google Meet連結：
https://meet.google.com/axu-kgsn-ijz


---

::: spoiler ## 2020 歷史專案

### commitizen-tools

- 專案描述 Project description: Create committing rules for projects 🚀 auto bump versions ⬆️ and auto changelog generation 📂
- 專案連結 Project link (e.g., Github): https://github.com/commitizen-tools
- 專案聯絡人 Project Contact: Wei Lee (weilee.rx@gmail.com)
    - [x] 參與實體聚會 Participate in physical meetup

---

### Quark-Engine — An Obfuscation-Neglect Android Malware Scoring System

- 專案描述 Project description: Quark-Engine is a trust-worthy, practical tool that's ready to boost up your malware reverse engineering.
- 專案連結 Project link (e.g., Github): https://github.com/quark-engine/quark-engine
- 專案聯絡人 Project Contact: JunWei Song
    - [x] 參與實體聚會 Participate in physical meetup

---

### MLGame — A Platform For Applying Machine Learning Algorithm to Play Pixel Games

- 專案描述 Project description: MLGame is not only for the player but also for the game developer (using `pygame`). It helps establish the communication between the game and the player code, and store the game progress for training the model.
- 專案連結 Project link (e.g., Github): https://github.com/LanKuDot/MLGame
- 專案聯絡人 Project Contact: Kun-Yi Li (https://twitter.com/LanKuDot)
    - [x] 參與實體聚會 Participate in physical meetup

---


:::