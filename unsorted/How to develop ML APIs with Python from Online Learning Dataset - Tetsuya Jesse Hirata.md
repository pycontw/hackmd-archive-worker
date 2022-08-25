# How to develop ML APIs with Python from Online Learning Dataset - Tetsuya Jesse Hirata

{%hackmd JgQsr94hSFK427iUDWF9NQ %}
:::warning
Slido連結 : https://app.sli.do/event/1ualxnit
:::
> 從這開始
      
###### tags: `PyConTW2020`
## Differences Between Research-Oriented Code and Production Code
- Research Oriented Code: Easy / Visually Tracable
- Machine Learning APIs: Fast / Readability / Testable (Modulizable)
- [作者在 Medium 寫的文章，介紹什麼是 research oriented code](https://towardsdatascience.com/research-oriented-code-in-ai-ml-projects-f0dde4f9e1ac)
- [作者在 pycon jp 的投影片](https://speakerdeck.com/tetsuya0617/how-to-transform-research-oriented-code-into-machine-learning-apis-with-python-ccff3060-5de1-4e52-a726-2b7160611685)
- [PyCon TW 2019 Speech Note](https://hackmd.io/@pycontw/SJEpwWmvH/%2F%40pycontw%2FBkNpHs28B)

## Transforming Research-Oriented Code to Production Code
### 1. Understand
### 2. Modularize
#### 2.1 Categorize Code
- Preparation Code
- Preprocessing Code
- ML Code
#### 2.2 Break Them Into Functions and Make Them Testable
#### 2.3 Clarify Input & Output of the Whole Code and Define URI
### 3. Refactoring
#### 3.1 Prepare for Refactoring
- Choose doc string style
#### 3.2 Simplify I/O in Preparation Code
- Google Cloud BigQuery / Storage
- Simplify more by using wrapper
#### 3.3 Pandas to Python in Preprocessing Code
- Know differences between pandas code and python code
- Write test code (start from easy one)
- Refactor pandas code in a pythonic way
### 4. Check
#### 4.1 Write Decorators to Check Parameters
- Request parameter check with JSON Schema
#### 4.2 Set up Prod-like Envs with Flask


## Reference
[Tutorial Slides](https://speakerdeck.com/tetsuya0617/how-to-transform-research-oriented-code-into-machine-learning-apis-with-python-ccff3060-5de1-4e52-a726-2b7160611685)
[Twitter](https://mobile.twitter.com/JesseTetsuya)