# Wait, IPython can do that? - Sebastian Witowski

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}

<iframe src="https://app.sli.do/event/xiyqjpio" height=450 width=100%></iframe>

> 從這開始
> 
## About the speaker
* https://switowski.com/blog
* Slides: bit.ly/advanced-ipython

## Notes

- Input / Output cache 很好用
    - 我們很常在看到 return value 之後，才知道我們需要這個東西
    - rerun function 的 cost 很高
        - Session expired ... etc
- IPython magic function 不是 Python dunder function
    - 所有 `%` `%%` 開頭的 function

## Magics
* `%history`
* `%edit`
    * edit a file/input history/macro...
* `%run` Run a python script
    * `%autoreload`
* `%%python2`
    * also bash, ruby..

* Writing magic function
    * Add decorator @register_line_magic / @register_cell_magic


## Events & Hooks

- Event
    - 所有 callback 都會執行
- Hook
    - 依序執行 callback，只要有一個成功及停止

## Debugging

- Use IPython as Python debugger

``` python
from IPthon import embed; embd()
```

## Profiliing
 - %prun: general profiler
 - %lprun: line profiler
 - memory profiler

###### tags: `PyConTW2019`
