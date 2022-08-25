# Pycon JP 2019 Day2: Modern development environments for Pythonistas - Dustin Ingram

###### tags: `PyCon-JP-2019`

## Speaker: Dustin Ingram

[twitter](https://twitter.com/di_codes)

* Organize PyTexas
* PyPi contributor

## Note

* Focus: anything that's not code and will be check into code base


Your laptop is not production.


* Virturalenv only isolatet Python
    * but not platform-level stuff

* What if we could fully isolate environements and reproduce it?
    * Docker
        * volume
    * docker-compose


## A modern workflow for dependencies

* Don't `pip freeze > requirements.tx

> [name=Wei Lee] can't agree more

* [pip-tools](https://github.com/jazzband/pip-tools/)
    * pinning and compiling only solve 90% of the problems
        * **artifact hashing** <- solution
            * `pip install --require-hash -r requirements.txt 
            * now our deps are 100 % frozen
    * when to upgrade ->  early and often
    * how to update -> scan you repo and see your deps (automatically)
        * pyup
        * dependent bot ->

## Linting and autoformatting

[black](https://github.com/ambv/black)

## Taking your env to prod

- services that supports deployment through container
    - heroku
    - aws
    - gcp -  cloud run (the speaker is from google lol)

## Conclusion

1. Use docker
2. Use docker-compose
3. Use `pip-compile` from `pip-tools`
4. Use Dependabot/Pyup for auto-upgrade deps
5. Use black
6. Deploy your docker container to prod


## QA

> Dustin: Just don't use windows