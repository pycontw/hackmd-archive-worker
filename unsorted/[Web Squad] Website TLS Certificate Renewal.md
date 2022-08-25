---
tags: dev team, web team
---

# [Web Squad] Website TLS Certificate Renewal

## Production

Production 的 certificate renewal 是有自動化的，不需手動更新。

因為 production GCE 有掛 load balancer，所以目前是直接在 GCE 設 cron job 定期戳一份 shell script 來透過 gcloud cli 更新掛在 LB 上的 certificate：

```bash=
#!/usr/bin/env bash
set -euxo pipefail

KEY_NAME=pycontw-ssl-cert-$(date +%Y-%m-%d)

sudo dehydrated -c --force

sudo gcloud compute ssl-certificates create $KEY_NAME \
    --certificate /var/lib/dehydrated/certs/tw.pycon.org/fullchain.pem \
    --private-key /var/lib/dehydrated/certs/tw.pycon.org/privkey.pem \

sudo gcloud compute target-https-proxies update pycontw-lb-target-proxy-2 --ssl-certificates $KEY_NAME

echo "Update $KEY_NAME"
```


## Staging

Staging 沒掛 load balancer，就也沒有像 production 能做這些自動化操作，需要每隔三個月就進機器手動更新 certificate。


```bash=
# ssh login to the GCE
ssh <account>@staging.pycon.tw

# Renew cert with dehydrated using root permission
sudo su - dev
sudo dehydrated -c --force

# Restart nginx container
cd ~/pycontw-nginx
docker-compose build --no-cache
docker-compose up --build -d
```

Staging nginx conf 和 codebase master branch 不同（not a good practice），為的是將 certificate 掛進 nginx，以下是部份 staging nginx conf：

```nginx=
# 上略

server {
    listen 80 default_server;
    listen 443 ssl;    
    server_name staging.pycon.tw;
    charset utf-8;

    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;
    
    ssl_certificate /var/lib/dehydrated/certs/staging.pycon.tw/fullchain.pem;
    ssl_certificate_key /var/lib/dehydrated/certs/staging.pycon.tw/privkey.pem;

    resolver 1.1.1.1 8.8.8.8 ipv6=off;
    client_max_body_size 10M;

    # http redirect to https
    if ($http_x_forwarded_proto = "http") {
        return 301 https://$host$request_uri;
    }

    location /.well-known/acme-challenge {
        alias /var/www/letsencrypt;
    }

    # 下略
}
```