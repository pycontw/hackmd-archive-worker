# Threshold Cryptography with Python - 陳昶吾

{%hackmd JgQsr94hSFK427iUDWF9NQ %}
:::warning
Slido 連結: https://app.sli.do/event/g2vrjdmg
:::
> 從這開始
      
* Split key 的問題是拼起來 private key 會被大家知道
    * Threshold Signature：多個Emphemeral Puzzle可以用來產生交易內容，但是私鑰不會被產生
* Shamir's Secrect Sharing (aka SSS)
    * 用來切割祕密，多鑰匙才能解密
    * 但是一開始一定要有個人產生並密碼就是
    * Hashi Corp 的 Vault 一開始產生的五組密碼就是用 Shamir's Secret 

## EDCSA

基於 Discrete Logarithm Problem (DLP)
相較於RSA，ECC size較小
橢圓曲線上的加法跟一般運算的加法不一樣


###### tags: `PyConTW2020`

### Materials for Tutorial

- [https://github.com/changwu-tw/PyConTW](https://github.com/changwu-tw/PyConTW)

```bash
$ git clone https://github.com/changwu-tw/PyConTW
$ cd PyConTW
$ docker pull sagemath/sagemath
$ docker run -p8888:8888 -v "$PWD":/home/sage/pycontw sagemath/sagemath:latest sage-jupyter
```

東西在 docker container 裡面，要另外用 `docker cp` 複製出來

### 16:15 ~ 16:30

- Computation Techniques for Encrypted Data using Python - Gajendra Deshpande
