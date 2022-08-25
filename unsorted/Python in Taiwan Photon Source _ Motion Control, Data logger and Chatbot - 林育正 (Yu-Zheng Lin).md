# Python in Taiwan Photon Source : Motion Control, Data logger and Chatbot - 林育正 (Yu-Zheng Lin)

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}

> 請從這裡開始

[TOC]

## What is synchrotron light source?
 * 把電子加速到接近光速 -> 經過轉彎電場 -> 產生 X 光

## TPS Front-End system
 * Open/Close synchrotron light
 * Monitor beam position
 * Radiation safety protection of beamline user
 * protect the vacuum status of TPS Storage ring.
 * ...
 * 透過工業用數據採集系統整合感測器的資料
 * 採集後透過EPICS節點連結整個光子源的控制系統

## What is EPICS
 * Experimental Physic and Industrial Control System(EPICS)
   - open-source software tool
   - TCP/IP based channel access network protocol
   - use to create soft real-tome distribution control systems.
   - like key-value DB
   - Developed by Argonne National Lab
 * Famous Project using EPICS
   - 重力波觀測
   - 國際核融合實驗室

 * Soft real-time

https://epics.anl.gov/


## TPS Front-end X-ray beam position monitor

 * Data logger
   - XBPM Data -> HDF5 File 
 * HDF5 data format

 * Beam Stability Analysis
     * Kernel Density Estimation
     * Scatter Draw

## Motion Control

 * [gclib](https://github.com/RahmanQureshi/pygclib) - Motion control lib.
     * e.g. 移動鑽石刀片，讓刀片刮過平面空間掃出光束強度分布

## LINE bot
 * Rule-based NLP + Webhook Service

## Front-end linebot demo
![Linebot demo](https://i.imgur.com/T6f8fd8.jpg)

## Q&A
* Why EPICS?
    * 反應快, 易用

* Linebot介面的安全性問題?
  - 讓程式不會touch到執行單元與信任的LineID



###### tags: `pycontw2018`
