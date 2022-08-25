# LED 眼鏡背後的蟒蛇魂 - Chiung-ting Chen

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}

Computer(Engineering)+Music

架構： midi keyboard -> python + midi listener -> web 

偵測彈奏內容 -> Pattern match -> display at frontend (websocket)

音高偵測 (比較單純)。節奏偵測 (偵測預先設好的音位置計算間距)

The LED Glasses is Arduino-compatible
So it can communicate via serial port


Portable charger -> raspberry pi 3 -> LED Glasses <- wireless connection-> Wifi
* Design trigger chord

[GITHUB](https://github.com/yychen/livespring)

###### tags: `PyConTW2019`
