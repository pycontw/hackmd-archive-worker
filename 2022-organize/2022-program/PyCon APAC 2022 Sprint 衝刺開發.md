---
tags: 2022-organize, 2022-program, sprint
---

# PyCon APAC 2022 Sprint 衝刺開發

* 日期 Date: 3/13  10:00 ~ 17:00 (台北標準時間 TST)
* 地點 Location: Gather Town
* 當日流程 Schedule: [PyCon APAC Sprint rundown online](https://docs.google.com/spreadsheets/d/1fKimCtiVNuIvebypaZTVk2iT25SfuAI8Vetv4OpqvHM/edit?usp=sharing)

[TOC]

## 如何組織一個衝刺開發 Organizing your sprint

* 介紹你的專案 Introduce your project

    你可以在 HackMD 中詳述你的專案內容與特色，以及想要參與者協助的地方。你也可以錄製一個小影片，讓參與者能夠迅速瞭解你的專案內容。例如一個簡短的教學影片，包括專案介紹與操作、如何佈建、測試，觀看 Issue、Pull Request 等等。讓參與者可以很快上手，並瞭解可以從哪開始著手貢獻。
    
    You can detail your project description and features in HackMD, as well as where you need participants to help. You can also provide a pre-recorded video for participants to quickly pick up the knowledge of your project. For example, a short tutorial video, including project introduction and functionality, how to deploy, test, view issue, pull request, etc. Make participants get started quickly and understand where to start contributing.


* 與參與者互動 Interact with participants

    專案主持人可以透過聚會分享、信件、聊天群組 (Slack, discord) 等等與參與者互動，交流意見，並協助參與者貢獻你的專案。如此一來，貢獻開源便不受限於時間與地點，而是一個長期的社群經營。
    
    The project host can interact with participants, share ideas with each other, and help participants contribute to your project through meetup sharing, email, chat groups (slack, discord), etc. In this way, contributing to open source is not limited to time and place, but a long-term community promotion.

* 提供參與者貢獻的方向 Provide direction for participants to contribute

    你可以從專案中現有需要幫忙的 issue 或是需要幫助的 pull requests 中提供參與者貢獻的方向，也可以透過與參與者相互討論，尋找可以更好的方向。
  
    You can provide the direction for participants from the existing issues or pull requests that need help in your project, and you can also discuss with participants to find a better direction.

* 因應 Covid-19 疫情，我們將透過線上的方式，組織你的 Sprints。
  Due to Covid situation, we will organize this event online.
    
## 如何報名你的專案 How to apply?

報名時間 Time：Now ~ 2/28 (Mon.) 23:59:59 (台北標準時間 TST)
報名網址 Link：https://forms.gle/AsamvLnWmPeiyfzg8

## 如何報名成為參加者 How to register as a attendee?

在 [KKTIX 註冊頁面報名](https://pycontw.kktix.cc/events/pyconsprint2022-1)
Register on [KKTIX](https://pycontw.kktix.cc/events/pyconsprint2022-1)

---

## 2022 春 專案列表 Projects List

### Pycon News Feed
- **專案描述 Project description**:
    **今天的 [Agenda](https://hackmd.io/Aah_fCbgSUqHO11gfV75Ww)**
    來做推薦系統吧！PyconTW 提供的有趣服務越來越多了，如 `PySafe`、`PyCast`、`徵才`等廣告，以及我們的本業也就是`演講`。
    所以我們想在 FB Messenger 上提供一個 news feed，用 ML 的方式來推薦用戶適合他的資訊。
    在本場 Sprint 的實作分成三個部分，歡迎大家加入！
    1. BE-side：Flask + FB API
    2. Recommendation-side：algorithm to design
    3. ELT-side（負責整理用戶的 feature、event，並蒐集文章來推薦）：Airflow + Crawler

- **專案連結 Project link**:
    - GitHub: https://github.com/pycontw/pycon-fb-chatbot
    - [推薦系統](https://heliotrope-podium-fc5.notion.site/Sprint-0e46144427484a78ac86ebada23cdd5c)
- **專案聯絡人 Project Contact**: @davidtnfsh  
- **先需知識 Background knowledge**: 推薦系統、Git、Backend、ML、想學的心（擇二）
- **進行語言 Language**: 中文
* 專案房間: Topic 1
* 備用Google Meet連結：
---
### SOLVCON 
- **專案描述 Project description**:
SOLVCON is a collection of conservation-law solvers that use the space-time Conservation Element and Solution Element (CESE) method [Chang95].

- **專案連結 Project link**: https://doc.solvcon.net/en/latest/
- **專案聯絡人 Project Contact**: @tai271828 
- **先需知識 Background knowledge**：
Python (Beginner), Shell scripting (preferred), Github Action (optional), Physics (optional, CFD is preferred), C++ and pybind11 (optional but will be excellent)
- **進行語言 Language**: English
* 專案房間: Topic 2
* 備用Google Meet連結：
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
    - 請先按照 [Contributing](https://commitizen-tools.github.io/commitizen/contributing/) 上的教學設定環境
- **進行語言 Language**: 中文
* 專案房間: Topic 4
* 備用Google Meet連結：

---

### Apache Airflow

- **專案描述 Project description**:
  從 Airflow committer 學習如何設定開發環境、選擇適合你的 issue、並提交貢獻。

- **專案連結 Project link**: 
https://github.com/apache/airflow/

- **專案聯絡人 Project Contact**:
  TP @uranusjr 
  uranusjr@gmail.com

- **先需知識**：
  請按照連結說明完成 Prerequisites 的部分：https://github.com/apache/airflow/blob/main/BREEZE.rst#prerequisites
- **進行語言 Language**: 中文
* 專案房間: Topic 6
* 備用Google Meet連結：
https://meet.google.com/yrt-qfju-qkx

---

### Oh!Shown 黑熊出沒痕跡通報

- **專案描述 Project description**:
  Oh!Shown是一個黑熊出沒通報平台，主旨在於讓山友或居民等提供黑熊出沒資訊給研究人員（台灣黑熊保育協會）進行彙整與後續研究推廣等。專案的程式碼是從Disfactory（違章工廠通報平台）fork出來，後端的部分使用Python Django framework（前端主要是vue.js）。

 
- **專案連結 Project link**: 
https://github.com/tai271828/disfactory-backend/projects/3

- **專案聯絡人 Project Contact**:
Eagle	qazx142www@gmail.com

- **先需知識**：
git, Django (加分：docker, vue.js)
- **進行語言 Language**: 中文
* 專案房間: Topic 7
* 備用Google Meet連結：

---
### COSCUP Volunteer 志工服務系統

- **專案描述 Project description**:
  目前專案希望逐步補足缺少的部分：type hints, dev environment, backend / service workflow / Helper docs, new feature for volunteer recruitment or skills.

 
- **專案連結 Project link**: 
https://github.com/COSCUP/COSCUP-Volunteer

- **專案聯絡人 Project Contact**:
Toomore	toomore0929@gmail.com

- **先需知識**：
Python, Flask, Celery, Vue.js, Docker, MongoDB, Nginx
- **進行語言 Language**: 中文
* 專案房間: Topic 8
* 備用Google Meet連結：

---

### RustPython
- **專案描述 Project description**:
大家一起來用 Rust 寫 Python interpreter 吧～～

- **專案連結 Project link**: 
https://github.com/RustPython/RustPython

- **專案聯絡人 Project Contact**: 
Jeong YunWon <jeong@youknowone.org>
Jihong <sinjihng@gmail.com>

- **先需知識 Background knowledge**：
  - 請事先按照這頁面做事先準備，不然隔天會沒時間一起寫 code Orz  https://rustpython.github.io/blog/2020/04/04/how-to-contribute-by-cpython-unittest.html
  - Nice-to-have: Rust (不會也沒關係辣)、 Python
- **進行語言 Language**: English
* 專案房間: Topic 9
* 備用Google Meet連結：

:::spoiler Project template
---
### Project Name
- **專案描述 Project description**:
- **專案連結 Project link**: 
- **專案聯絡人 Project Contact**: 
- **先需知識 Background knowledge**：
- **進行語言 Language**: 
* 專案房間: Room OO
* 備用Google Meet連結：
:::
---
::: spoiler ## 2021 歷史專案範例
### commitizen-tools （範例）

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