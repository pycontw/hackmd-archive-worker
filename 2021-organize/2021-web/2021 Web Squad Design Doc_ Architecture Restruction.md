---
tags: 2021-organize, 2021-web, dev team
---

🔙 [PyCon TW 2021 Organizing 共筆](/Wb9vQrfJQk-5tPoPR23hwA)

# 2021 Web Squad Design Doc: Architecture Restruction



## Current Architecture

The graph below displays the current architecture of our multi-year website.

- All the services are dockerized and launched with docker-compose on a GCE machine.
- `pycontw-nginx`: handle the request by the year info in the URL to desired web app.
- web:
    - 2012 to 2015: a static hosted web app for each conference
    - 2016 to 2020: a Django web app for each conference
- `pycontw-postgresql`: The postgresql server connected by the website for 2016, 2017, ..., & 2020 (only one database named `pycontw` is commonly used).

![](https://i.imgur.com/tpLBokh.png)

### Pain Point

- All database changes need to be backward-compatible.
    - Increase the complexity of codebase
    - A simple field deletion can paralyze all previous web apps (e.g. [`pycon.tw#975`](https://github.com/pycontw/pycon.tw/pull/975)).


## Draft of New Architecture

![](https://i.imgur.com/tA0pNeu.png)

### What've Changed?

- All currently existing architecture remain the same.
- From 2021, each conference website is consisted of:
    - a frontend app 
        - can be deployed beyond GCE
    - a backend server (proposal system + API server)
        - each connecting to a **dedicated database** within pycontw-postgresql

### Downsides

- Could be harder to collect cross-year information
- Need to import a copy of database after conference ended

### Discussion

- Can we forbidden users to access the old proposal system?
- Potential next step: one common Django app for proposal system? (since this part is rarely changed across past few year)



## Reference

- [draw.io & pictures used in this page](https://drive.google.com/file/d/1pGjBWPKTdRNSCHbxZmprbzDRYZMAAkoE/view?usp=sharing)
- [Web repo list](./HyEWz0S0D)