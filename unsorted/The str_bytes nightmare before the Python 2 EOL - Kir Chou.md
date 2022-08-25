# The str/bytes nightmare before the Python 2 EOL - Kir Chou

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}

> 從這開始
      
## Python3

* Default: text, unicode

## Python2

* Default: auto-encoded bytes
`u''`: text

## Treatment

### Be Explicit with Encoding

Always provide encoding for bytes

### ?

Python2: sys.stdin/sys.stdout
Python3: sys.buffer.stdin/sys.buffer.stdout

### Unicode Sandwich

### 2, 3 Compatibility
```python
from __future__ import unicode_literals
```

### Typing

Recommended by Dropbox

```python
def encrypt(data, key): # Is data str or bytes???
    return cipher
```

```python
def encrypt(data: bytes, key: bytes): # Now we know
    return cipher
```

###### tags: `PyConTW2019`


