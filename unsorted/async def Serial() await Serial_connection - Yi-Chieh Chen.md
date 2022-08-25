# async def Serial() await Serial_connection - Yi-Chieh Chen

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}

> slides: https://hackmd.io/@Uvz_vZj7SYajJAhdNwxlFA/BJnJ2J9IH#/
> sampel code: https://github.com/chairco/asyncio-pySerial/

如何使用 asyncio 搭建一個 RS232 序列阜非同步程式經驗？
Protocol or transport？

Synchronous:
* 程式 blocking 造成問題

Async:
* non-blocking I/O

Protocol: 
* application 抽象
    * web socket application
Transport 
* socket connection 抽象 
    * socket 協定

Open Space: Async flow
  * async producer
  * async queue (when comsumer wifi disconnect, data will be storaged in queue)
  * async comsumer

如何使用 concurrent.futures 裡的 threadpool 與 asyncio 裡的 run_in_executor 方法讓 Synchronous 從 callable 變成 awaitable

step 1: 原本 synchronous 作法
```python=
from serial import Serial

ser = Serial('com3', 9600)

def get(ser):
    msg = ser.read_until('\r\n')
    return msg
```

step 2: 建立一個可以將程式放進 event_loop 中的 run_in_executor 裝飾器，這裡參考 Andrew goldwin ASGI 專案
```python=
class SyncToAsync
    ...略
    
    async def __call__(self, *args, **kwargs):
        loop = asyncio.get_event_loop()
        future = loop.run_in_executor(
            None,
            functools.partial(self.thread_handler, loop, *args, **kwargs),
        )
        return await asyncio.wait_for(future, timeout=None)
        
    ...略
    
sync_to_async = SyncToAsync
```

step 3: 接者將使用這個裝飾器，接著原先的函式就會成為一個 awaitable 的函式
```python=
from serial import Serial
from SyncToAsync import *

ser = Serial('com3', 9600)

@sync_to_async
def get(ser):
    msg await ser.read_until('\r\n')
    return msg

```



###### tags: `PyConTW2019`
