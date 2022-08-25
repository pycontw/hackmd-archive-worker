---
title: '2021 mail-handler 使用手冊'
tags: 2021-dev-infra, 2021-organize
disqus: hackmd
---
🔙 [PyCon TW 2021 Organizing 共筆](/Wb9vQrfJQk-5tPoPR23hwA)
🔙 [PyCon TW 2021 dev-infra 主頁](/@pycontw/Bkp2vRQEu)

# pycontw-mail-handler 使用手冊

[TOC]

---


## 建立信件內容
### `render_mail [OPTIONS] TEMPLATE_PATH RECEIVER_DATA`
- **[OPTIONS]**
  `--mails_path PATH  [default: mails_to_sent]`：儲存信件內容位置，預設會新增於當前目錄下新增的 mails_to_sent 的資料夾中
  `--separator ' TEXT '`：設定輸出信件檔名分隔符號/文字
- **TEMPLATE_PATH**：內容基本格式檔案位置，接受 *.j2* 檔案
- **RECEIVER_DATA**：需替換的輸入資料檔案位置，接受 *.json* 檔案
    - 預設需有以下格式資訊
        ```
        {
            "common_data": {},
            "unique_data": [
                {"receiver_email": "somerec@somedomain"}
            ]
        }
        ```
    - common_data：每封 email 共用之資料
    - unique_data：每封 email 所需特定資料
### 使用範例
- 修改 <font color=#808080>template</font> 文件（可參考 *sponsors_invite.j2* 撰寫）
- 修改 <font color=#808080>reveiver data</font> 文件（可參考 *sponsors_invite* 撰寫）
![](https://i.imgur.com/Trf5AbK.png)
- 使用 <font color=#808080>render_mail</font> 輸出信件內容
    ```
    render_mail sample/sponsors_invite.j2 sample/sponsors_invite.json
    ```
    - 如添加 `--separator '-'`，則輸出信件檔名為 *{receiveremail}-{receviername}*
- 完成後會在目錄下建立一個 *mails_to_sent* 的資料夾，內有以receiver_email 為檔名之檔案，確認輸出無誤
![](https://i.imgur.com/YHD7Ycm.png)
- 確認內文
![](https://i.imgur.com/gpcuZA7.png)




## 寄出
### `send_mail [OPTIONS] CONFIG_PATH`
- **[OPTIONS]**
  `--mails_path PATH  [default: mails_to_sent]`：信件內容檔案夾位置，預設為 mails_to_sent，如非預設位置才使用
  `--attachment_file PATH`：如需夾帶附件可使用此填寫附件檔案位置
  `--separator ' TEXT '`：`render_mail` 如有使用到 separator 則此也必須加上相同項目
- **CONFIG_PATH**：寄件者資料設定檔，接受 *.json* 檔案
    - 需具備以下格式資訊，以`,`分隔多個收件者
    ```
    {
        "Subject": "some subject",
        "From": "somebody@somedomain",
        "CC": "somebody1@somedomain, somebody2@somedomain"
    }
    ```

### 使用範例
- 修改 <font color=#808080>config</font> 檔案內容（可參考 *mail_config.json* 撰寫）
- 使用 <font color=#808080>send_mail</font> 寄送 mail_to_sent 資料夾內之信件
    ```
    send_mail sample/mail_config.json
    ```
- 系統詢問是否確認寄出，輸入`y`
    ```
    You are about to send the mails under "mails_to_sent". Do you want to continue? [y/N]:  y
    ```
- 輸入寄件者 email account (目前僅支援 gmail)
    ```
    Please enter your mail account: xxxxxxxx@gmail.com
    ```
- 輸入設定過的 password (設定方式請參考 驗證問題 部分進行設定)
    ```
    Please enter you mail password: xxxxxxxx
    ```
- 寄送成功系統會顯示以下資訊
    ```
    Email sent to xxxxxxxx@gmail.com!
    ```
- 收件者收到的透過 mail handler 寄送的信件
![](https://i.imgur.com/4NamR1X.png)

## 驗證問題
- 在 **登入 Google 的部分中**，將 **兩步驟驗證** 修改為 **開啟**，開啟後會出現 **應用程式密碼** 欄位，點選
![](https://i.imgur.com/wR2tsdZ.png)
- 選擇 **其他(自訂名稱)**，隨意填入名稱可辨識為何種用途即可，點選產生
![](https://i.imgur.com/Cvo3HC3.png)
- 此時會跳出 **系統產生的應用程式密碼** 視窗，記下此組密碼，此組密碼即在使用 mail handler 時所需的 password
![](https://i.imgur.com/FZv4N7i.png)

## 補充 / 常見問題
- 如需安裝請參考 [pycontw/mail_handler@GitHub](https://github.com/pycontw/mail_handler)


