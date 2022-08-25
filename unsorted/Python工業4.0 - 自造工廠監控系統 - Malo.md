# Python工業4.0 - 自造工廠監控系統 - Malo

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}
[toc]
## Outline
 * 工廠監控
 * 工業4.0
 * 工廠監控的現況
 * Modbus
 * Modbus套件
 * PLC
 * Power Meter
 * MQTT
 * Web API

## 工廠監控
 * 為何在工控應用中導入Python
   - 工作中使用語言繁雜，欲有統一的程式開發語言
 * 使用Python跟[PLC](https://zh.wikipedia.org/wiki/%E5%8F%AF%E7%BC%96%E7%A8%8B%E9%80%BB%E8%BE%91%E6%8E%A7%E5%88%B6%E5%99%A8)電表溝通的demo


## 工業 4.0
 * [wiki](https://zh.wikipedia.org/wiki/%E5%B7%A5%E6%A5%AD4.0)
 * 水力>電力>資訊化>工業4.0
 * 智慧插頭
 
## 工廠監控
 * SCADA+HMI+PLC+IO module ([SCADA wiki](https://zh.wikipedia.org/zh-tw/%E6%95%B0%E6%8D%AE%E9%87%87%E9%9B%86%E4%B8%8E%E7%9B%91%E6%8E%A7%E7%B3%BB%E7%BB%9F))
 * [HMI](https://zh.wikipedia.org/wiki/%E4%BA%BA%E6%9C%BA%E4%BA%A4%E4%BA%92)+PLC+IO module
 * PLC+SCADA
 * [食品廠工業4.0 檢重機雙機互聯網實作 Checkweigher sample video](https://www.youtube.com/watch?v=LSuRcf0ua6c)

* Why SCADA 這麼常出現 （工控領域）
  - 缺點: 不便宜

## [Modbus](https://zh.wikipedia.org/wiki/Modbus)
 * 工廠監控中最常見的協定 (Modbus/TCP & Modbus RTU...)
 * 公開發表且無版稅要求的通訊協定。
 * 相對容易的工業網路部署(兩條訊號線)
 * Function: Digital In (DI), Digital Out (DO), Analog In (AI), Analog Out (AO)
 * ![Modbus message format](https://www.cooking-hacks.com/media/cooking/images/documentation/Modbus/Serial_Frame_1_big.jpg)

## Modbus套件
 * [Modbus-tk](https://github.com/ljean/modbus-tk)
     - Modbus TCP在產業界較常見
 * [pymodbus](https://github.com/riptideio/pymodbus) : 實作最完整, loading 較重
 * [MinimalModbus](https://github.com/pyhys/minimalmodbus)：沒有 Modbus/TCP

## Modbus Installation
<pre syntax='bash'>pip install serial modbus_tk</pre>

## PLC
[python與PLC共舞](https://github.com/maloyang/PLC-Python)
 * 如何通訊、控制?
    1. 自有協定 
    2. Modbus

## Live Demo
* 透過 Modbus protocol 控制繼電器啟動110v電燈
    * 高電位：0xFF00
    * 低電位：0
* 透過 Modbus protocol 讀取電表值
    * 讀取: 電壓、功率、頻率
    * IEEE 754
    * `unpack()`
* MQTT
    * 即時收資料
    * 手機控制
    * WebAPI (RESTful + Postgresql)
    * 存到firebase
* ThingSpeak
    * 上傳資料自動畫成趨勢圖
    * raspberry pi+modbus 

## Q&A
 * 通訊規格 OPC-DA/UA)的推廣程度如何
    * 逐步導入OPC-UA. OPC-UA可更好的支援Linux, 仍需要Linux開發者的進一步整合
 * 目前實作的環境裡連接的Device有多少才能維持講者提的反應速度
    * RS485連線下, Modbus Master-slave目前通常為1個master對應到16個slaves, 
    * 此架構正常情況下request-response turn-around time約為10~50ms

###### tags: `pycontw2018`
