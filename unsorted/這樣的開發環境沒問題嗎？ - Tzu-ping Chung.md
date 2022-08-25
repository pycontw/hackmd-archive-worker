# 這樣的開發環境沒問題嗎？ - Tzu-ping Chung

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}

投影片：https://speakerdeck.com/uranusjr/zhe-yang-de-kai-fa-huan-jing-mei-wen-ti-ma

跟90%會眾表示你們的開發環境有問題。

anaconda 不在今天的議程中，~~請不要浪費時間聽這場~~。

目標會眾環境: pip/easy_install + emacs + terminal

~~可以用jupyter寫django嗎？🙃~~

---

[The law of leaky abstractions](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/): 沒有包裝是完美的


本議程是很多來自 django girls 的經驗。

- pipenv核心貢獻者 (今天主題關聯)

---

這樣裝備沒有問題嗎? ~~大丈夫萌大奶~~モンダイナイ

```
Intepreters (eg. Python)
-> Tools  (eg. virtualenv)
-> Dependencies  (eg. Django)
-> Application (Your stuff)
```

# bottom up 來看

## Application

沒啥好講的跳過

## Dependencies: virtaulenv(python3內建)

```shell
$ python3 -m venv --prompt="project" .venv
$ . .venv/bin/activate
(project) $ pip install -r requirements.txt
```

### 講師提及的 Dependencies 問題1: 套件版本控制
```
# 抽象依賴：環境主要需要的套件（最少量資訊原則）
requests[security]
flask
gunicorn==19.4.5

v.s.

# 實體依賴：環境所有需要的套件 concrete dependency
enum34==1.1.2
requests==2.9.1
Flask==0.10.1
six==1.10.0
```

abstract dependency: easier to upgrade, but hard to realize what/which version will be installed
concrete dependency: you have to figure out dependency yourself

pyOpenSSL 安全性更新為例：抽象依賴比較好些


### 講師提及的 Dependencies 問題2: 環境PATH
virtualenv會直接改PATH。

[Virtualenv's bin/activate is Doing It Wrong](https://gist.github.com/datagrok/2199506)


## 推銷 pipenv / pipenv-cli

### 跟使用者的開法工序衝突 -> 作者正在模組化

~~sudo pip install pipenv~~ 🤔🤔🤔🤔🤔

how to install pipenv in virtual environment? (chicken/egg)
```shell
$ mkdir -p ~/.local/bin ~/.local/venvs
$ python3 -m venv ~/.local/venvs/pipenv
$ ~/.local/venvs/pipenv/bin/pip install pipenv
$ ln -s ~/.local/venvs/pipenv/bin/pipenv ~/.local/bin
```
actually pipsi did that ，但因爲 pipsi 作者好像失去興趣進行更新了，所以推薦使用以上 script

Rules of Thumb
1. Do not use sudo Ever
2. always use virtual environment
3. Use --user if desperate


## 要怎麼裝 python

1. 各位的電腦有幾個python？
mac內建：2.6, 2.7, 3.3~3.5
ubuntu內建：3.6
Don't use OS built-in python


### Linux
ubuntu:
    1. use "deadsnakes" PPA
    2. 自己編
    3. try not to use apt install python
    4. be careful with the package manager (every package manager installs lib in different path)

### MAC
1. ❎ **Do not use** system python 
2. ❎ **Do not use** homebrew python
3. ✅ must compile your own

### Compile Your Python
1. install some build dependencies
2. pyenv install `<version>`
3. Use 
    - `python-build 3.6.5 ~/.local/pythons/3.6`
    - `ln -s ~/.local/pythons/3.6 ~/.local/bin`


### Windows
1. No global Python to worry about (ha, look at you!)
2. No support from pyenv
3. Building is *drastically* more difficult
(PythonUp works for Windows too!)

http://vstinner.readthedocs.io/cpython_windows.html

## Tradeoff:
核心開發者社群議題：要有好用的作業系統內建python，還是系統內應該要沒有python？


## Summary
* don’t use homebrew python
* prefer self-compiling if possible
* always use virtual environments
* you can call scripts in venv directly
    * avoid “activate” scripts
    * pipfile / pipenv abstrats them
* don’t use setup.py to develop a package

###### tags: `pycontw2018`
