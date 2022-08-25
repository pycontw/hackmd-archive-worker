# Real-Time Automatic Accompaniment Implementation in Python - 范斯越 Szu-Yueh Fan

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}

<iframe src="https://app.sli.do/event/dy4qee8u" height=450 width=100%></iframe>

> 從這開始
      
###### tags: `PyConTW2019`


[https://github.com/yychen/livespring](https://github.com/yychen/livespring)

* 即時伴奏（AI）
* what is automatic accompaniment?
    * 第一input: 樂譜 (包含主奏和伴奏)
    * 第二input: 真人演奏
    * 效果：像是樂團
    * video demo
        * 不管吹奏的快慢，AI仍然可以即時伴奏
* Roger Dannenbergs
    * 三十年前就被提出來的方法
* Input
    * 第一種input: MIDI
        * use midi file to present sheet music
        * midi's time period: ticks
        * midi pitch
            * frequency=2^(MIDI pitch-69)*440 Hz
        * MIDI ≈ Sheet Music
            * 不完全相等
            * 但可用
            * 互相轉換會遺失資訊
    * 第二種input: performer's signal
        * analog -> digital
* System
    * 四個模組：midi module, data module, performance modeule, synthesis module
    * midi module
        * python package: 
            * `music21`
            * `pretty_midi`
        * separate track
        * adjust bpm
        * track bucketization
    * data module
        * note & signal generator
        * dataset: MusicNet, Bach10v1.1
    * synthesis module
        * `pyFluidSynth`
    * performance module
        * package `sounddevice`: 收音
        * feature extraction
            * performer signal -> constant Q Transform(CQT) -> CQT Chroma (12 dimension)
                * 去掉音色的影響
            * package `librosa`
    * Online processing
* Research Problem
    * Audio-to-score synchronization
        * offline: 拿到整個樂譜、完整的聲音訊號
            * 應用：interpretation switcher
        * online：
            * 應用：自動翻譜
            * 應用：自動伴奏
* Decision Model
    * online dynamic time wraping
        * 主奏者訊號 match 樂譜
        * 問題：match的並不好
    * performance hidden Markov model
        * 從決定性的模型轉到機率性的模型
        * emission probability
        * 問題：第一個音下後，伴奏就很急的往前進
    * hierarchical hidden semi-Markov model
        * hidden state transition ~ geometric distribution
        * autoregressive model to predict P
* Performance Measurement
    * hard limit: 46.43 miliseconds
    * performance average 41.46 < 46.43 miliseconds
* Github: 18fanfan




