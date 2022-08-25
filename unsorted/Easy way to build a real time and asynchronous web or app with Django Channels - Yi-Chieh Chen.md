# Easy way to build a real time and asynchronous web or app with Django Channels - Yi-Chieh Chen

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}

投影片連結：https://speakerdeck.com/chairco/pycontw-2018-easy-way-to-build-a-real-time-and-asynchronous-web-or-app-with-django-channels
範例程式：https://github.com/chairco/2018_PyConTW_Talk （包含時間不夠沒辦法 demo 的聊天室等等）

### 前情提要

👌佛系工程師👌

- PyCon TW 2017 邀請了 Django Channels 的作者 Andrew Godwin 來講 keynote 但是他有點可惜沒有講到相關的東西
- 2017 底做了 Django Channels 大改版，目前最新版本 2.1.1 版（百分之 75% 程式碼重寫）
- 2018 Django Channels 在 PyConUS 等地做了演說提供很多資訊

👌所以佛系工程師是就是不讀 SPEC. 不幫忙 controbute 不做翻譯 不求甚解 時間到了作者自己就把一切說清楚了👌


# 相關技術背景

## WebSockets

- WSGI 目標是建立一個協定讓 python 裡方便（輪詢,polling）HTTP 之間的溝通，但當時沒有處理到 WebSocket 的問題

- 常見實作 WSGI Server（Gunicorn/uWSGI)

- 2011 Define standard
- 2014 Implementation

### AJAX vs Websocket
- AJAX: 一來 一回
- Websocket: 一來 n回

### Python x websocket
- twisted / tornado
- gevent / asyncio
- uWSGI

#### Twisted 
- InlineCallbacks: Reactor
- Futures: Deferred 
- > Twisted is the mother of async in Python - Yury Selivanov
#### Tornado
- for python2.x
- implemented by fb
#### gevent
- Uses libev(callback, eventloop), greetlet(micro-thread, coroutine)
- Monkey-patching: 把一些會造成 I/O blocking 的 build-in function patch掉
- No Jython and IronPython support
- Guido 不喜歡QQ
- coroutine始祖
#### asyncio
- 前身叫 tulip
- since python3.4, 還不成熟
- Guido 喜歡<3
- Python 3.5 出了 `async` / `await` 語法
#### uwsgi
- implemented in C
- replaced http server
#### gunicorn
- implemented in Python

---

## Synchronous
- 阻塞式單一行程
- [c10k problem](https://en.wikipedia.org/wiki/C10k_problem)

## Asynchronous
- Non-blocking I/O
- Callback
- Event loop
- Coroutine

### Threads?
> Problem: Threads are bad
- race condition - solved by GIL (but slow for concurrency implementation)
    - 補充 GIL 讓 Python multithreading 更適合 I/O 頻繁的應用(concurrency)
- OS 的 context switch 比較繁雜不宜過於頻繁使用

#### context switch 解決策略
- Non-blocking I/O: many processes
- many threads
- callback
- coroutine

### Non-blocking I/O
- Event-driven
- Socket Multiplexing
- select, poll, epoll, kqueue

```python
s = socket.socket()
s.setblocking(False) ### 黑魔法!?
```

### Callback （難維護）
- Future/Promise
- Coroutine-style: `yield` / `yield from` -> `async` / `await`
```python
# lambda: 不好維護
callback = lambda: connected(s, path)
```
*Guido 94不喜歡 callback*

### Event-loop

> 給你做一件事，做完叫我 - TP

### coroutine (美)
- > Beautiful is better than ugly
- > Readability counts

## Channels

# Django Channels

## v1.x
- python2.7 兼容
- twisted for webserver
- ASGI = WSGI + async
- django是用Synchronous寫，但要如何做到非同步？->queue

client -> webserver(S) -> channel layer -> django sync worker(S)

## v2.x
- Asincio-native
- Python 3.5+
- Supports async coroutines and sync threads

2.x 後將 channel layer 從中間拿掉。

client <-> webserver(Django app) <-> channel layer(redis) 


## Daphane
- websocket 
- Twisted 作為 web server 所以可以承受很大量的連接


## ASGI
ASGI = WSGI + async


## sync to async 與 async to sync

因為如 Django ORM 等還是同步

1. sync to async: 會造成 block 給你一個 thread
2. async to sync: 無法使用 await 語法，幫你建立一個 event-loop

asgiref 提供這兩個 wrapper 讓你直接使用


* [github](https://github.com/chairco/2018_PyConTW_Talk)
    * 時間不夠 QQ 相關 demo code 可以參考裡面





###### tags: `pycontw2018`
