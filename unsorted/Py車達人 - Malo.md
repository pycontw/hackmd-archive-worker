# Py車達人 - Malo

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}

> 從這開始
> 

用 Python 擷取車的資料

## CANBus

* Controller Area Network
* 相較 modbus 來說容錯率更高
* 使用兩條線傳輸
* Node 1 送資料，Node 2/3 都會收到
* [值得一看的文章](https://www.youtube.com/watch?v=FqLDpHsxvf8)
    * 駕駛座下面的梯形接口可以撈出車子的資料

## BeagleBone 上的 CANBus 通訊

* CAN interface: socketCAN
* 使用 python-can
* 速度: Max 1000k
* 設備: can0
* 需要使用 ip link 設定 canbus 界面(can0)，可用 ifconfig 查詢資訊
* 建立 can0 以後，操作起來和 TCP/IP 的 socket 使用很像(建立 socket, bind 界面, read, write)
* cansdk:
    * 編譯出 `libcansdk.so`
    * 使用 NON_BLOCK flag

## 案例分享

* Baundrate: 500kbps
* 確定每個 CAN id 代表的資料


## 課程簡報

* [連結](https://github.com/maloyang/pycon-tw-2019)


###### tags: `PyConTW2019` `IoT`
