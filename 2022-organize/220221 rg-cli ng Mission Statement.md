---
tags: 2022-organize
---

🔙 Back to [歷年 PyCon TW Organizing 共筆](/ryPr7SFyP/%2FHM5mHCFKQCu7-W5ea8ITcw%3Fview)
🔙 Back to [PyCon TW 2022 Organizing 共筆](/F4qRbwIsQXWH5B6cZ6Pzyw)
🔙 Back to [PyCon TW 2021 Organizing 共筆](/Wb9vQrfJQk-5tPoPR23hwA)


[ToC]

# 220221 rg-cli ng Mission Statement

Mission Statement - https://trello.com/c/uqhmF9BM/33-%E8%87%AA%E5%8B%95%E5%8C%96-2022-%E8%B4%8A%E5%8A%A9%E7%B5%90%E6%A1%88%E5%A0%B1%E5%91%8A-alpha-version
Approach - https://trello.com/c/coTnaoy4/92-infra-implement-rg-cli-aka-post-event-report-generator-ng-next-generation

# Meeting Minutes

## Next
- rg-cli 先作到這邊 https://github.com/pycontw/pycontw-postevent-report-generator/pull/53
    - 不知道為什麼沒有自己 release
    - 另外再包 more data for jonathon


## 220530
- completed PR https://github.com/adinpearce/cli_test/pull/5
- [name=tai] will pick up docker file
- a.o.b.: gather town

## 220502
- talked about the plan to invite where
- talked about the email draft process for gather is good.
- talked about the usage of github
    - create pull request and merge it to a specific repo
    - how to assign reviewer and review
- "firstly" use click in the repo

## 220404
- https://github.com/adinpearce/cli_test.git
- [Tai chi](https://www.youtube.com/watch?v=Skt6hRErR7c)
- comittizen https://pypi.org/project/commitizen/

### 未來的功課 (long-term)
- [name=jonathon] study how to package python packages and release it
    - play with https://test.pypi.org/ before you are confident of doing/releasing anything
    - 相關的社群裡可以做/回饋的事情 https://trello.com/c/pzIdyPWV/109-pypi-donation-%E4%B8%8D%E7%9F%A5%E9%81%93%E8%A6%81%E6%94%BE%E9%80%99%E9%82%84%E6%98%AF-pr-%E5%85%88%E4%BA%82%E6%94%BE
    - https://trello.com/c/quUmjLJc/130-%E9%BC%93%E5%8B%B5%E6%A0%B8%E5%BF%83%E6%88%90%E5%93%A1%E4%B8%8A%E5%82%B3%E4%B8%80%E5%80%8B-python-package-to-pypi

### Next time
- tai/jonathon 各自再發一個 pull request 到 jonathon's repo (feature 與實做方向自由發揮)
    - 發 pull request 是為了培養 async 工作模式，而不是要驗收什麼。沒空弄沒興趣弄就當天弄就好 XD

## 220321
- How to learn something that I don't know what I don't know?
    - 第一手資訊 (是資料不是教學)
        - 官方文件 (systematic)
        - discussion
        - PEP
    - 教學材料
        - 一大堆，但總是入門/基礎
    - 弱連結 (oppurtunatics)
        - [TP 的分享 regarding venv](https://www.youtube.com/watch?v=6Nl0IYkU0hU)
- keyword when setting up github: `ssh gen key pair` and [the backgroud knowledge](https://zh.wikipedia.org/wiki/%E5%85%AC%E5%BC%80%E5%AF%86%E9%92%A5%E5%8A%A0%E5%AF%86).

### Next time
- tai/jonathon/michelle 各自再發一個 pull request (feature 與實做方向自由發揮)

## 220307
- tai - ubuntu mate - pycharm/vscode
- michelle - macOS - vscode
- jonathon - windows - vscode
- allen - windows - vscode

### Homework
- [name=everyone] make sure you can use vscode debugger and stop at your breakpoints
- [name=michelle] create a github repository for this project
- [name=jonathon] create a pull request to the above githut repository
- [name=allen] 自由發揮 XD

## 220307 minus 2 weeks
### Homework - Honor Program
- 回頭去看初代 rg-cli 跟第一個 example 相似的地方 https://github.com/pycontw/pycontw-postevent-report-generator/blob/master/report_generator/controller/report_generator_cli.py
- [bonus] 打造一個超級陽春的 command line tool based-on click
- [super bonus] try rich-click

## 今天要有的共識
- Next Step
    - 屬於個人的 next step
        - jonathon/ michelle
            - 試玩 click official site 第一個 example
            - 回頭去看初代 rg-cli 跟第一個 example 相似的地方 https://github.com/pycontw/pycontw-postevent-report-generator/blob/master/report_generator/controller/report_generator_cli.py
            - [bonus] 打造一個超級陽春的 command line tool based-on click
            - [super bonus] rich-click
    - 屬於 team 的 next step
        - 兩週後 bi-weekly 1hr hacking hour

## Necessary Knowledge
- python
- python virtual environment https://docs.python.org/zh-tw/3/library/venv.html
- click
    - python decorator

## Randome Notes
- Some tips
    - google "pycon click"
    - click repo https://github.com/pallets/click
    - rich-click repo https://github.com/ewels/rich-click
        - https://github.com/pycontw/pycontw-postevent-report-generator/blob/master/report_generator/controller/report_generator_cli.py
        - https://click.palletsprojects.com/en/8.0.x/
- complains about gather.town https://discord.com/channels/752904426057892052/925741901003493396/945290772134121512
- commandline design pattern https://zh.tai271828.me/articles/programming-code-01-12-factor-cli.html
