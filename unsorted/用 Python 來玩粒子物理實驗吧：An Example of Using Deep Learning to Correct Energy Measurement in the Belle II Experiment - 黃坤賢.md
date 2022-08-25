# 用 Python 來玩粒子物理實驗吧：An Example of Using Deep Learning to Correct Energy Measurement in the Belle II Experiment - 黃坤賢

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}

> 請從這裡開始
[slide](/6n5PA7KkTfuAh3wO_OCspg)

前方高能注意！

https://www.youtube.com/watch?v=nGCrrgXSEOk

KEK實驗是將電子與正子對撞之後，產生高能量的環境來模擬大爆炸之後的宇宙。


 * B 介子開始衰變

## Big Data
* Data Size: 1MB
* Bella 2 30~50PB  和Google Search 差不多
* LHC Science ~ 500 PB
 
資料分析使用 ROOT 軟體[Root Analysis Framwork]
https://root.cern.ch/

python binding

[Belle2 VR](https://store.steampowered.com/app/810020/Belle_II_in_Virtual_Reality/)
(supports HTC Vive, Oculus Rift...)

量測光子的能量使用CsI晶體，使用Geant4模擬
Crystal Simulation for Detector
https://geant4.web.cern.ch/

用 30x30 晶體陣列的排列做模擬

其實是解回歸問題

###### tags: `pycontw2018`
