# GraphQL with Graphene and Django, laughter and tear - Keith Yang

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}


<iframe src="https://app.sli.do/event/hnycsmnz" height=450 width=100%></iframe>

> 從這開始

## REST-ful?
* Aging REST API docs & schemes
    * [Stoplight](https://stoplight.io/) or [Swagger](https://swagger.io/)
    * Hard to maintain
    * Easily outdated
* [Django REST Framework (DRF)](https://www.django-rest-framework.org)
    * many light crafted serializers to be discovered/followed
    * many endpoints and different resolutions to be discovered/followed

## [GraphQL](https://graphql.org/)
* Alternative to REST-based architectures
* Tool: [GraphIQL - An in-browser IDE for exploring GraphQL.](https://github.com/graphql/graphiql)
* Pros
    - Flexible
        - Multiple resource in single request
        - Flexible Query Versionless
    - Type-safe, self-documenting API
        - Typed schema
    - Reusable resource on API spec level
* [Graphene](https://graphene-python.org/) - GraphQL in Python
    - Pros
        - 只要出一個 endpoint 就收工了
    - Cons
        - 跟傳統 rest 相比，不能限流量，要再額外開一個新的 url
## GraphQL at iChef
* With front-end
    * Apollo + React
* Generate GraphQL for iOS
    * `apollo-ios`

## Lesson learned
* Try split modules by resource, instead of input/output
* Use standard type String, instead of extend type UUID, decimal... until it's ready.
* Simplify authentication


## Reference
* [Win back lovely API - GraphQL in Python](https://yang.keitheis.org/talks/win-back-lovely-api-graphql-in-python/) - Keith Yang in PyCon 2018
* [howtographql.com](https://www.howtographql.com/graphql-python/0-introduction/): Python branch
* 




###### tags: `PyConTW2019`
