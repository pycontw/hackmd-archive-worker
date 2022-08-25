# Notes about moving from Python to C++ - Yung-Yu Chen

{%hackmd JgQsr94hSFK427iUDWF9NQ %}
:::warning
https://app.sli.do/event/nlpgsiiy/
:::
> 從這開始

:::warning
Slides: https://www.slideshare.net/YungYuChen/notes-about-moving-from-python-to-c-py-contw-2020
:::

## Speed is the King
* Python controls execution flow
* C++ manages resources
* Use C++ to generate fast assembly code
* Glue Python and C++

## glue
* For performance and compile-time checking, we do not want to use Python.
* For flow control and configuration, we do not want to use C++.

## Pybind11
| Pros        | Cons          |
| ----------- | ------------- |
| easy-to-use | require C++11 |
* Write Python-like code in C++

### Zero-copy
* recommanded method:
    * Python on Top: To access array
    * C++ at the bottom: To manage the array

### Manage resources
* Python: reference count 
* C++ by using pointer.

## Conclusion
* Github repository: https://github.com/yungyuc/nsd

## Questions



###### tags: `PyConTW2020`
