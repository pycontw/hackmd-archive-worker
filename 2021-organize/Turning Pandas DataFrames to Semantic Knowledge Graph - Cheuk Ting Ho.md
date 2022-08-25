---
title: Turning Pandas DataFrames to Semantic Knowledge Graph - Cheuk Ting Ho
tags: PyConTW2021, 2021-organize, 2021-共筆
---

# Turning Pandas DataFrames to Semantic Knowledge Graph - Cheuk Ting Ho

{%hackmd f0JLCtZCTiWo4ZBRNKd8cg %}

<iframe src="https://app.sli.do/event/v8gqeoiz" height=450 width=100%></iframe>

<iframe src="https://wall.sli.do/event/v8gqeoiz?section=054a6fcf-7b4d-4ec9-b385-464129ba2dc1" height=450 width=100%></iframe>

> To start the collaborative writing here

### Pandas Dataframe
* Pandas is prety wonderful (especailly for tabular data form.)
* Does not handle nested structure well

### Nested Data
* Nested data can be handled in graph format.

#### Semantic Knowlege Graph
* A graph-structured **data model**
##### Turn Pandas Dataframe into Semantic Knowlege Graph

###### Preparation
* Like extract data from a data lake, define a proper schema and data types.
* Might need to restrict the size while loading data.
* Data type matters.
* `to_dict()` converts pandas to a dictionary.
* NA value handling: skip record all together or make it optional.

###### Flattening
* `from_records` load json records back into pandas dataframe.
* `json_normalize` to flatten nested structures.


### Demo
load csv to pandas dataframe and then load to terminus db.




###### Speaker and the relative information

Cheuk Ting Ho

1. [github](https://github.com/Cheukting)
2. [twitter](https://twitter.com/cheukting_ho)

TerminusDB

1. [tutorial repo](https://github.com/terminusdb/terminusdb-tutorials)
2. [python client](https://github.com/terminusdb/terminusdb-client-python)


###### tags: `PyConTW2021`