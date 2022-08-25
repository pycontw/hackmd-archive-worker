# The Software Engineering Part of Data Science - Niño R. Eclarin

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}

<iframe src="https://app.sli.do/event/nukpnurd" height=450 width=100%></iframe>

> 從這開始
> 

* The difference between data scientist and software enginner

### Development challenges
- no linters
- catch errors
- code quality
- no language features


### Arcbjtecbthre
- Algorithm
- models will be used

### Deployment
- Cloud or Local
- Mobile
- Micro Controllers

### Data Driven Development

1. Data Source
2. Data input -> preprocessing -> model -> output
3. Data Storage

### Coding Standards
- Code Quality
    - Data Scientists are not software developers
    - Use linters and formatting tools
        - Type hints
    - code review
- Error Handling
    - Standardize Errors
        - Meaningful errors
        - Warning v.s. Errors v.s. fatal errors
    - Specific Erros
        - specify some training or overfitting exception to improve the readability

- Data Integrity
    - Class Definition
        - explain what the parameters means and the possible values
    - Atomic Operations
    - Granularity of Data Results

### Architectural Challenges
- Memory v.s. CPU
    - CPU for training 
    - Memory for model storage
- Multithreading
    - Good for memory bound algorithms (Decision Trees)
    - Easy to implement
- Multiprocessing
    - has better throughput than Multithreading
    - Better for algorithms with high CPU consumption (NN)
    - Difficult to implement than the Multithreading
- Provide "Glue Code" for data scientists (through ABC)
    - Unified interface saves life

### Deployment
- Scaling up
    - Take note of algorithm runtime
    - O(n^2) algos won't work when you scaling up
- Scaling down


pprmint/pycontw

###### tags: `PyConTW2019`
