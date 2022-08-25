# Crossing the Python 3 Rubicon - Claudiu Popa

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}

> 請從這裡開始

{%slideshare ClaudiuPopa10/pycon-taiwan-2018claudiupopa %}

- 投影片連結：[slideshare](https://www.slideshare.net/ClaudiuPopa10/pycon-taiwan-2018claudiupopa)

- pylint maintainer
- 爲了~~帶女友~~到處玩而投稿 pycon tw
- Software engineer at Zapier

- 題目由來：[Cross the Rubicon](https://en.wikipedia.org/wiki/Crossing_the_Rubicon)

## Why we should upgrade from Python2 to Python3
- 2.7 End Of Life 還剩下 1 year and 6 months
- 3.6+ is better language
- Django, pandas, numpy, ipython 將不再支援 python 2 
- no more security fixes

## Python 在 CPU 和 MEMORY 的優化
- CPU on uwsgi 20% saved
- Memory on celery 30% saved

## Why Python 3.6 ?
* Easier to migrate nowadays
* Performance improvements
* ordered dicts by default
* shared dict implementation
* f-strings, async/await, parameter-less function
* example: In pycon US this year，instagram said that after migrating to python3, the performance also improved a bit.

## 2 kinds of approaches 
* Stop the world: move everything to python 3
* granular approach: 2/3 compat

## gradual approach
* compatibility shims for python 2/3 in same codebase
* canary python 3 in prod
* run with python 3 in prod
* remove python 2 once done

### Updates: can i use python 3
- [can i use python3 github repo](https://github.com/brettcannon/caniusepython3)

### "futures"
```python
# useful almost in every case
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
# controversial treatment: str vs bytes
from __future__ import unicode_literals
```

### detour throught bytes: python3
* str() - equivalent to Python2's **unicode**
* bytes() - sequence of integers (0~255)
* No unicode() anymore!


### detour through bytes: coercion
* default encoding on python 2 is ascii
* no vague coercion anymore in python3 (treat it controversially)

```python
# python2
value = u'很好'
interpolate = 'Taiwan is {}'
interpolate.format(value)
```

### unicode "sandwich"
* use bytes at the edge of application
* use unicode in between
* use bytes only in some cases

```requests```'s response.text is not cached -- decodes on access, which hits perf 


### shims: six and future

### Tools: futurize
http://python-future.org/futurize.html

### Tools: modernize

### Tools: pylint --py3k
* can find issues that futurize and modernize cannot find

### Tools: python -b
```
bytes comparison checks
$ python -b
$ python3 -bb
```

### Tools: python -3
comparison checks

### other gotchas
* don't compare objects of different types

```python
>>> 2 < '2'
```
* hash randomization (?)

## references

* [python future](http://python-future.org/compatible_idioms.html)

## Takeaways
* pick six / future
* automate: futurize, moderize, pylint


###### tags: `pycontw2018`

