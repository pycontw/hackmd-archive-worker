# 使用 airflow 執行爬蟲單元測試來打造網站改版自動偵測通知服務

{%hackmd JgQsr94hSFK427iUDWF9NQ %}
:::warning
Slido連結 : https://app.sli.do/event/hamswujz
:::
> 從這開始

## 爬蟲系統的問題
### 漏資料
- 爬的太頻繁而被 band
    - solution: proxy IP pool
    - solution: 調整爬取速度
- 網站不定期改版
    - 單元測試
## some solutions:
### ELK count error log
- 可以看到詳細的爬蟲錯誤
- 尚未解決的問題
    - 但還是會有過多假警報如: 爬蟲被檔、文章被刪除
    - 發文量較少的爬蟲容易被忽略

## 爬蟲單元測試
- 使用 Scrapy 開發
- 把爬蟲程式變成通用的 class ，有各自的調整才特別調整成另外的 class ，因此就可以針對個別 class 進行單元測試
- 因為單元測試會排除對環境的依賴，但是爬蟲需要網路依賴，因此會使用 betamax 這個可以 mock request 的套件，來進行單元測試
- 實作測試樣板生成機制

## Q&A
1. 
2. 如何避免爬取重複文章
    - 給每篇文章 MD5 hash
3. GitLab CI Scheduling
###### tags: `PyConTW2020`
 