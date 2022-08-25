# Develop Numerical Software - Yung-Yu Chen

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}

<iframe src="https://app.sli.do/event/vprp9ahm" height=450 width=100%></iframe>

###### tags: `PyConTW2019`

Talk link: https://tw.pycon.org/2019/en-us/events/talk/870171889119527188/

Slide deck: https://speakerdeck.com/yyc/develop-numerical-software-pycontw-2019

Open space: https://hackmd.io/JkVMAE6oR-qwUMeGeKmpjA

> Starts here

## What is numerical software?
* Problem to Solve
    * Mathematics
    * Physics
    * Engineering
    * and many others...
* Numerical software
    * Research code
    * Niche markets
* It is not practical to ask everyone to have deep understanding inside math.
    * Engineering works here!
    * Create a numerical software for engineers easy to use.

## Languages of Numerical Software
* Numerical programmers speaks Fortran back then.
* BLAS and LAPACK after Fortran.
* **NumPy!!** yay!

## [NumPy](https://numpy.org/)
* 5.24 sec (pure Python) / 58.3 ms (NumPy) = 89.87x faster!
* Multi-dimentional arrays
    - Be careful of majoring! (row/column major)
* memory management: zero-copy!
    - During cross-language programming, make one language to allocate memory, the other just access it.
    - Reduce memory use.
* High performance code
    * number crunching code is in deep or long loops.
    * try to optimize the calculation kernel as possible.

## How to optimize calculation kernel
1. Timing for hotspots
    * Do not optimize without any time measurement!
    * time measurements
        1. CPU time
            - user time
            - system time
        2. Wall time: the time duration in real world (clock on the wall)
    * Linux `time` command
    * Python `timeit` module
        * By default if only calculates wall time
        * Alternative is to use `perf_counter()` or `perf_counter_ns()` from `time` module
2. Memory management
    * Memory hierarchy
    ```
    registers(0 cycles)
    L1 cache (4 cycles)
    L2 cache (10 cycles)
    ...
    Memory
    ...
    Disk     (100,000 cycles)
    ```
    * Locality: access memory consecutively.
    * Profiling
        * profile of memory is much harder than for runtime.
        * Need your own malloc, realloc, calloc, free.
    * Large memory
        * 10,000 x 10,000 matrix of double takes 800MB
    * Instance counting
    * Tips
        * When modularizing code, put a memory manager in each module.
        * Allow system to switch between different global memory managers. (glibc/jemalloc/tcmalloc/...)
        * Use runtime analyzers like valgrind
        * Learn PyMem
3. Software Engineering
    * Keyword: **Automation**
    * Version control is foundation.
    * Build system
        * Makefile
        * CMake
        * Python `distutil` is still useful if you don't have too complicated system combined multiple languages.
    * Unit testing
        * Google-test
        * Python stdlib unittest and py.test
    * Code review and paper writing
        * Write down papers which is acceptable for version control.
            * TeX/LaTeX is worth to consider for mathematical formula.

## System design patterns
* Data Object
* Nested loop
    * Except in high-level flow control, there 's no room for fancy things like list comprehension
* Evolution design
    * **Congrats! You should celebrate about it!**
    * Doesn't go right in the first place.
    * Insert debug logs
* Release and distribution
    * Packing and deliver is the first step to move from research code to product code!
