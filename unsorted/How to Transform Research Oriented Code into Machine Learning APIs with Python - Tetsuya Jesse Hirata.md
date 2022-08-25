# How to Transform Research Oriented Code into Machine Learning APIs with Python - Tetsuya Jesse Hirata

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}

> 從這開始
> 
講者簡報 [slides]( https://speakerdeck.com/tetsuya0617/how-to-transform-research-oriented-code-into-machine-learning-apis-with-python?fbclid=IwAR1cUkcCBYq6duaiWAmlEhcW4-lz6wcrISHMcK2-IYcelFJSPTwMoY6iE5E)

## Transforming Research oriented code into Machine learning API in 4 steps

1. Understand
2. Modulize
3. Refactory
4. Check

## Research: Difference between codes

- Research Oriented Code: Easy / Visualizable
- Machine Learning APIs: Fast / Readability / Testable (Modulizable)

### Step 1. Understand

- What is research oriented code
- What are ML APIs
- How should engineers handle research oriented code

### Step 2. Modurized in 3 part: make it testable

1. Preparation (input)
2. Preprocessing (filter)
3. ML Code (calculation)

### Step 3. Refactor

- Design structured folder
- Simplify I/O
- Use wrappers

### Step 4. Check
- write decorators to check parameters
    - e.g. with json schema validator (can be found in stackoverflow)
        - [Flask: Decorator to verify JSON and JSON Schema](https://stackoverflow.com/questions/24238743/flask-decorator-to-verify-json-and-json-schema)
- set-up production-like environments with Flask
    - Visualize data
    - Auto CI
    - Deployment


## Q&A:

- Q: Hi, It is a very helpful talk, thank you! If I am trying to covert a research code, how would you suggest the timeframe in man hours? (in days/ or months?)
    - A. 2-3 months

- Q: Do you think serverless like AWS lambda is a good way to deploy ML models?
    - A: Not sure about that.

- Q: How to test the refactored code?
    - A: 

- Q: When do you decide to refactor research oriented code into production code:
    - A: Right after they finish the research oriented code


### 講者資訊:
- twitter: https://twitter.com/jessetetsuya

###### tags: `PyConTW2019`
