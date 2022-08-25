# Adopting Python Asyncio in Large Scale Project (Instagram) - Jimmy Lai

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}

{%slideshare jimmy_lai/the-journey-of-asyncio-adoption-in-instagram %}

> [slideshare](https://www.slideshare.net/jimmy_lai/the-journey-of-asyncio-adoption-in-instagram)

# About me

- Infrastructure engineer in instagram
- Focusing on
    - profiling
    - Cython
    - asyncio

# Instagram Backend

- Python + Django
- uwsgi
- Data fetching from backends
- Processes > CPU
    - all IO is blocking mode before using asyncio
- memcachd/cassandra/thrift services

# Blocking I/O problems

- Slow API
    - waiting I/O
- CPU idle
    - context switch overhead
- uwsgi Harakiri
    - timeouted request will terminate process

# What is Async IO?

- blocking IO mode: 
    - run IO sequencially
- Async IO mode:
    - run IO concurrently

(Example: [Professional chess player play with several non-expert players](https://rarehistoricalphotos.com/samuel-reshevsky-age-8-france-1920/))

# Async I/O solution

- Slow API
    - no need to wait I/O
- CPU idle
    - In thread context switch 
- uwsgi Harakiri
    - ?

# Myths about asyncio
1. single-threaded
    - only one function could be executed in the same time
    - only I/O could run concurrently
2. not always faster

# asyncio example

```python
async def sleep_and_return(sec)
    await asyncio.sleep(sec)
    return sec
```
`sleep_and_return` is a `<coroutin object sleep_and_return at xxx>`

```python
async def run():
    results = await asyncio.gather(
       sleep_and_return(1),
       sleep_and_return(1),
       sleep_and_return(2),
    )
    print(results)
    // return [1,1,2] in 2 secs
```

How asyncio works?

- nonblockling IO mode, in Python can use socket.setblocking(False)
- register IO to EpollSelector and wait until IO ready by select()

```python
class BaseSelectorEventLoop:
    async def sock_recv(self, sock, n):
        ...
        return await fut

    def _sock_recv(self, fut, registered_df, sock, n):
        try:
            data.recv()
        except BlockIOError:
            #TODO
        
    def run_until_complete(...):
        #TODO

    def run_forever(self):
        """Run until stop() is called."""
        while True:
            self._run_once()
            if self._stopping:
                break

    def _run_once(self):
        """Run one full iteration of the event loop."""
        event_list = self._selector.select(None)
        self._process_events(event_list)
        ntodo = len(self._ready)
        for i in range(ntodo):
            handle = self._ready.popleft()
            handle._run()

```

# asyncio Adoption in Instagram Just Like


# asyncio addption challenges
- scale: large code base
- usablility: no bug
- priority
- automation
- efficiency

# Backend Client Libraries asyncio Support

- Thrift
    - fbthrift for py3
- HTTP
    - aiohttp for replacing requests

- Other backends
    - https://github.com/aio-libs/https://github.com/aio-libs/https://github.com/aio-libs/

# Helper function

```python
import asyncio

def wait_for(coro):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(coro)
    
result = wait_for(async_func())
```

## Migration to asyncio

```python
def func():
   blocking_thrift_call()
   
async def func():
   await async_thrift_call()
```

## Identify Blocking Calls
- Blocking call finder
- latency computation: finding high latency and optimizing them first

```python
def f():
    blocking_thrift_call()

def g():
    h()

def h():
    blocking_http_call()

def api():
    f()
    g()
```

## When Too Many Dependency in Stack
- use sync wrapper
  - async function caller uses async callee
- `func = sync(async_func)`
  - Async group call async_func
  - Sync group still call func (original name, no need to commit)
  - Handle classmethod, staticmethod function differently
```python
def sync(async_func):
    is_classmethod = False
    if isinstance(async_func, classmethod):
        async_func = async_func.__func__
        is_classmethod = True
    elif isinstance(async_func, staticmethod):
        async_func = asyncio.coroutin(async_func)

    @functools.wraps(async_func)
    def _no_profile_sync(*args, **keargs):
        return wait_for(async_func(*args, **kwargs))

    if is_classmethod:
        return classmethod(_no_profile_sync)
    else:
        return _no_profile_sync

func = sync(async_func)
```

## Nested Event Loop
- contextmanager to handle this situation
- creating a loop pool to reuse it

## Runtime Error: Loop stopped before future completed.

[It's Python's bug](https://github.com/python/cpython/pull/1688)
- Put callback function into Finally section

## Global variable issue
- case: accessing same global variable at two different async functions at the same time
- contextvars: make sure different caller have consistent value of global variable.
```python
# python3.7
import contextvars
var = contextvars.ContextVar('var')
async def f():
    var.set(await read_from_db1())
    await write_to_db1(var.get())
async def g():
    var.set(await read_from_db2())
    await write_to_db2(var.get())
async def run():
    await asynclib.gather(f(), g())
```

## Reorganizing design pattern

```python
async def identity(value):
    return value
# and then calling this async in if-else loop of async function
```

## Lint
- ast + flask8
- Rules
    1. async_func should named with async_ prefix
    2. change gather await in loop to `asyncio.gather`
    3. warning when adding new blocking calls

## Automation

source code -> ast -> code modifier -> change set -> (CR)pull request
- use pyan static analysis and runtime profiling

## CPU Overhead

- cost 20% cpu instruction
- -CPython was slow (Asyncio should be written in C, but they were written in Python)
- Optimization strategies:
    - Simplify the code and remove redundant computation
    - use Cython
    - use C API
- Available optimiztions:
    - uvloop: **libuv** + Cpython binding for event loop
    - CPython3.6 implement *Future* and *Task* in C
    - Cpython3.7 implement `get_event_loop()` in C. Future and `gather()` also become fast

## Custom optimization 
- gather() -> ensure_future() -> isfuture/iscoroutine/isawaitable
    - Reorder: check iscoroutine first
    - deduplicate coroutines using a dict, remove assumption.
    - Implement helper function in C

- reduced overall asyncio CPU overhead by 2X (10%)

## Result (Current)
- API latency -> 30% faster on service side
- Better user engagement
- 100% async + concurrent request handling

mail: jimmylai_at_instagram.com

## Q&A

- Django is syncio, how to write asyncio in Django?
    - we make asyncio patches for Django

- Is your asyncio migration related to python2 to python3 migration?
    - We spend on Python3 migration almost 1 year, finished in early last year.

###### tags: `pycontw2018`
