# Python Profilers we Built for Efficiency - Jimmy Lai

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}

> 

https://github.com/jimmylai/talks

**11:31**

## Instagram Introduction

- Efficiency Issues at Scale

## 3 types of efficiency issue

- Latency
- CPU
- Memory 

## Metrics
- ncall
- tottime (total time)
- cumtime

Goal -> Know which function to optimize

## cProfiler Limits

1. unstable timer
2. no detailed callstack
3. not support for asyncio 

## cProfiler Limits Solution

1. CPU Instruction Counter
2. Collect callstack and instrcution counter
  - **perf** (Difficult)
  - profiler hook (Easier in python, in this presentation)
3. frame approach won't work for asyncio (You will only get event loop function)
  - `setattr` (Add your own frame attribute to async function)

## Profile hooks

- `sys.setprofile(function)`
- `sys.settrace(function)`

## Methodology (In code)

- Get the time_delta (by parent frame)
  - `call`, `c_call` (Add time delta to parent frame)
  - `return`, `c_return` (Add time delta to current frame)

## How to optimize your code to be more efficient?
- String
- Iterator Comprehension
- Async
- others: call_count, timestamp (he showed the example of this), lru_cache

## Result

- 12% CPU efficiency from python2 to python3
- Many many instagram previous talks

###### tags: `PyConTW2019`
