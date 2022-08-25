# Async contextmanager for Python 3.7 - Sammy Wen

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}

<iframe src="https://app.sli.do/event/6b6xgmld" height=450 width=100%></iframe>

> 從這開始

[slide](https://gamekingga.com/pycontw2019.pdf)

## `asyncio` vs **Context manager**
* `asyncio`
    * concurrency in single thread
    * run tasks(wrapped coroutine) in an event loop
* Context manager
    * [PEP343](https://www.python.org/dev/peps/pep-0343/) - the `with` statement
    * allow to allocate and release resource precisely when you want to.
    * 2 types of implement
        * Class
          * implement `__enter__` and `__exit__`
        * Generate
            * add decorator `@contextlib.contextmanager`

## async context manager
* decorator `@asynccontextmanger`
* class with `__aenter__` and `__aexit__` methods
* asyncio.run(): 執行 co-routine



###### tags: `PyConTW2019`
