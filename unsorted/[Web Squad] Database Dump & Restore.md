---
tags: dev team, web team
---

# [Web Squad] Database Dump & Restore

目前官網 backend 有一台 PostgreSQL ([GitHub Repo](https://github.com/pycontw/pycontw-postgresql)) 在跑，為了資料備份或是希望用 production data 做測試，網站組時常會需要執行 DB dump & restore。

此頁面紀錄了將 production DB data 倒進 staging DB 的步驟與對應指令。

**TODO**: DB dump & restore 的自動化方案

## DB Dump

1. ssh 到 production GCE 後，確認 postgres 有在運作
    ```sh
    $ docker ps
    CONTAINER ID   IMAGE            COMMAND                  CREATED       STATUS        PORTS                    NAMES
    ...
    a9b19a775cbb   postgres:11.1    "docker-entrypoint.s…"   6 weeks ago   Up 2 weeks    0.0.0.0:5432->5432/tcp   pycontw-postgresql
    ...
    ```
2. 執行指令將 db data dump 到 `/tmp` 底下
    ```sh
    $ docker exec -it pycontw-postgresql pg_dump -U pycontw pycontw2022 > /tmp/db.dump.`date +%Y%m%d`.sql
    ```
3. 將 DB dump 用任何方式傳到 staging GCE 上，例如用 scp
    ```sh
    scp <username>@<production_host>:/tmp/db.dump.20220509.sql /your/path/db.dump.20220509.sql
    scp /your/path/db.dump.20220509.sql <username>@<staging_host>:/tmp/db.dump.20220509.sql
    ```
    
## DB Restore

1. 進到 postgres container 將當年度 database 資料清除（刪除 db 並重建）
    ```
    $ docker exec -it pycontw-postgresql psql -U <username>                                       
    psql (11.1 (Debian 11.1-3.pgdg90+1))
    Type "help" for help.

    pycontw=# drop database <db_name>;
    DROP DATABASE
    
    pycontw=# create database <db_name>;
    CREATE DATABASE
    
    pycontw=# \q
    ```
2. 將 data dump restore 進當年度 database
    ```sh
    $ docker exec -i pycontw-postgresql psql -U <username> <db_name> < /tmp/db.dump.20220603.sql
    ```