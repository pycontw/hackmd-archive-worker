# Python實作運彩下注策略 - 陳建安 and 廖子慶

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}

簡報: https://drive.google.com/openid=1H5twARImwjIo0gbfcHLOF0XRMnkXFpqY
https://drive.google.com/file/d/1H5twARImwjIo0gbfcHLOF0XRMnkXFpqY/view

GitHub:
https://github.com/LukeCCA/SportLottery


- NBA優點：球員不太會變動，資料量豐富，官網資料也很多(從初接到進階)
- 使用PTT LYS的文章(因為ptt鄉民都說他是反指標)
- [ptt-web-crawler](https://github.com/jwlin/ptt-web-crawler)
- [凱利公式](https://zh.wikipedia.org/wiki/%E5%87%B1%E5%88%A9%E5%85%AC%E5%BC%8F)

* 利用基因演算法從600多的特徵值中找出200多個出來來訓練模型，LYS的文章沒有太直接影響
* Traing set 和 Validation set 拿2012~2017 的資料作訓練大約六千多筆, Test set 為2018的例行賽程
* 訓練模型時遇到資料的不連續，例如:中間可能會有2015新選秀球員加入球隊，造成沒有前面三年的數據


###### tags: `pycontw2018`