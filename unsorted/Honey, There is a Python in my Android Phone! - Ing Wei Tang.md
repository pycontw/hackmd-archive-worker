# Honey, There is a Python in my Android Phone! - Ing Wei Tang

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}


      
###### tags: `PyConTW2019`

- Android phones are similar to a powerful small computer in our pocket. 
- it is possible to connect to the sensors in our Android phone by Python. The problem is, how?
- The problem Ing-wei would like to solve is to scan the ISBN of books.
- How to access the lower level API in android phone? 
    
- They developed an prototype called: SnapBooks

### Digging Deeper
- How does Python talks to Android API?
    - `self._rpc`
    - SL4A, QPython3

### QPython
- He built an traffic logger by QPython
    - androidhelper + flask + vue.js
    - live demo