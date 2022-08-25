# PEP 572: The Walrus Operator - Dustin Ingram

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}


## Python Governance

## BDFL
Benevolent dictator for life
Guido Van Rossum

## What is PEP?

determine how python works

PEP 8 by Guido

PEP 566 by Dustin
- metadata

### How does a PEP got accepted?
- 1) submit draft
- 2) BDFL review and approval 


## PEP 572
- Walrus operator: `:=`
- What is good about PEP 572
    - Avoid unnecessary variable scope
    - processing streams in chunks
    - Fewer lines are better
    - fewer lines are more efficient?
![](https://upload.wikimedia.org/wikipedia/commons/2/22/Pacific_Walrus_-_Bull_%288247646168%29.jpg)


```
foo = [y: f(x), y**2, y**3]
```


```
results=[ y for x on data if (y:=f(x)) ]
```
```
a[i] = x # yes
a[i] := x # no
```


## Problems while introducing walrus operator
- Backward compatability
- Teachability
- Attractiveness: it is just ugly
- Discussions on mailing list:
    - after a long long discussion...
    - It got accepted and will be included in Python 3.8 which would be release soon. 
    - But, Guido decided to step down for this

> People are people, too.

<!-- -->

- 經過 2x 年的單人管理，Python 終究是要解決立法的程序問題。
- 壓垮神的不是垃圾 PEP，而是把 PEP 稱作垃圾的人們。

###### tags: `PyConTW2019`