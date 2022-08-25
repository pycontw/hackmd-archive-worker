# Start Wrap Episode 11: A New Rope - Yung-Yu Chen

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}

> 請從這裡開始

## Why C++
- Python is slow
- Access external code written in any language
- Detail control and abstraction

## Hard problems take time
> HPC(high perfomance computing) is pard
> Pyhsics is harder
> Don't mingle

## Best of both worlds
- C++: fast runtime: slow to coding
- Python: fast prototyping: slow to run
- So, Hybrid system is everywhere

## [pybind11](https://gitub.com/pybind/pybind11)
- expose c++ entities to python
- use python from c++ (list, tuple, dict, str, handle object and none)

## c++11(/14/17/20)
- Lots of new features

## New features need to know
- (python)
- shared pointer: manage resource ownership between c++ and python
- lambda expression: ease the wrapping code
- moved sematics: speed

## Ownership in PyObject 
- All Python objects are dynamically allocated on the heap
    - reference counting
- A owner of the reference to and object is responsible for deallocating the object

## Shared pointer in C++11
- Use shared pointer like raw pointer
- and enjoy resource management(garbage collection) done by the library

## Lambda
- Code as free as Python, as fast as C

## Move semantic
- Problem with lots datas and they aren't supposed to be copied frequently
- shared pointers should manage large chucks of memory.

## Ownership
- new reference to an object: copy constructor of shared pointer
- borrowed reference: 
- stolen reference: move constructor of shared pointer

## Manipulate Python
## Don't mingle Python withc C++
- Python has GIL: don't use python.h
- pybind11 provides helper classes for all built-in containers
    - list
    - tupe
    - dict
    - str

## Generic Python Objets
- handle: no builtin reference count
- object: base on handle and have reference count

## None
- It's worth nothing that pybind11 has "none" type.
- In Python, None is a singleton, and accessible as Py_None in the C API.

## How fast is fast
## Wisely use arrays
- Array are used as booth
    - interface bwtween python and c++ and
    - internal storage in the c++ engine
## Arrays in Python
- numpy

## Why are arrays

## The Python way

## Why not just to do it in c++
- The good
    - Data organization is free: your own structure
    - control every detail
    - no cap when you need spped
- The bad is *C++*

## Expose memory buffer
- in C++: array controlled by shared pointer
- in python: ndarray

## Internal array meta data

## Organied arrays

## Fast and complicate code

## Use pybind11
- header-only library

## Useful trick: variadic template

## Other tools
- Wrapping
    - boost.python: when you need to wrap pre-11 c++
    - cython: quick way to access c and a portion of c++ features
    - python C API
- Speed-up
    - Numba: jit for ndarray
    - Cython: fast loop inside ndarray
- Nothing is faster than c++(except some fortran)


## Final notes

- aovid python when you need spped
- resource management is in the core of the hybrid architecture: do it in c++
- Use array(look-up tables) to keep large data
- Don't access PyObject from your code
- Always keep in mind the differences in typeing systems

###### tags: `pycontw2018`