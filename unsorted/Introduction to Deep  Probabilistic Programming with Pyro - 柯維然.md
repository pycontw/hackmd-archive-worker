# Introduction to Deep  Probabilistic Programming with Pyro - 柯維然

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}

<iframe src="https://app.sli.do/event/5fy5gnfh" height=450 width=100%></iframe>

> 從這開始

[Slide](https://docs.google.com/presentation/d/1qOIqK5MmE-b43yTYgQL7b7Opu-AmkqGGCgmvgdHhqfg/edit#slide=id.p)
      
###### tags: `PyConTW2019`
* PL $\cap$ ML $\cap$ STAT
* 主要focus在probabilistic programming
* probabilistic programming
    * 經過特化的程式語言
    * 基於機率的程式語言
    * 結合 3 種 AI paradigms
        * Symbolic: logic and reasoning
        * Bayesian: Inference and uncertainty
        * Connection: learning from complicated data
    * 比較
        * 一般
            * input+configuration -> program -> output
        * probabilistic programming
            * parameters+latent variables(隱變量) -> program(sampling) -> output/sample
            * parameters+latent variables(隱變量) <- program(inference) <- data/observation
* Pyro
    * Pyro bulit on Pytorch and another version on JAX(NumPyro)
    * Support GPU and JIT mode
    * sampling
    * trace
    * evaluation probability - 可以把sample fix 住(類似seed)
    * evidence lower bound
        * 難點在於inference 
        * ex. maximum likelihood