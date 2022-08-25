# Deep dive into smart contracts and blockchains - Anand Sai and Aditthya Ramakrishnan

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}

# 區塊鏈
- 不可更改，分散式，重複的公開資料庫
- 解決拜占庭將軍問題
- 新的模式，新的組織方式
- 不需要信用即可使用
- 中村聡(Satoshi nakamoto)是第一個發明區塊鏈，解決付兩次錢問題的人
- 避開中央信用系統的單一弱點問題
- 使用工作證明(挖礦)來驗證交易內容

https://anders.com/blockchain/hash.html

# 以太坊 Ethereum

- 去中心化的應用是未來趨勢，如智慧合約

- 外部擁有的帳號 (EOAs)
    - 有以太幣
- 智慧合約 (Smart Contracts)
    - 用來交易的協定，隨時可以驗證而不需要信任任何人
    - 保證獨立於任何機構之外
- [Vyper](https://github.com/ethereum/vyper)
    - 下一代 Ethereum 智慧合約用的 programming language
- [Solidity](https://zh.wikipedia.org/wiki/Solidity) vs Vyper
    - 文件較少，實驗性質
- Use Cases
    - [0xSHG](https://github.com/SatoshiNextTechLab/0xSHG)
    - Maersk - 貨物移動追蹤
    - American Express - 減少紙本文件轉移風險
    - TOKIT - 保護專利，獲利，全力
    - AXA - 降低紙本, 人工作業的時間成本
- Terminologies
    - Wei
    - Gas
    - Ether
    - Testnet

## 程式碼
- 線上測試程式碼 [Vyper Online Compiler](https://vyper.online)
- 會編譯成 Bytecode
- 有ABI [Application Binary Interface](https://zh.wikipedia.org/wiki/%E5%BA%94%E7%94%A8%E4%BA%8C%E8%BF%9B%E5%88%B6%E6%8E%A5%E5%8F%A3)
- LLL (Low-level Lisp-like Language)
- 發布
    - [Go Ethereum](https://github.com/ethereum/go-ethereum)
    - [Ethereum JavaScript API](https://github.com/ethereum/web3.js/)
- 副檔名 `.vy` or `.v.py`
    - `.v.py` 較佳, 因 vyper 是 based on python 以 `.v.py` 結尾可以套用 Python lint 工具
- 指尖陀螺，每次有交易就會旋轉一下
- [CryptoKitties](https://www.cryptokitties.co/)

# Q&A

- 智慧合約如何運作
    - 智慧合約是所有人共用的虛擬機狀態的變化，可以驗證所以安全
- 我們將會放資料在社群與Github

###### tags: `pycontw2018`
