![Build](https://github.com/SemenovAV/core/workflows/Build/badge.svg)

# Django template



## first usage
If the pipenv package is not installed:

``` pip install pipenv ```

then:
```
pipenv shell
pipenv install --skip-lock --dev
pipenv lock --pre
pre-commit install --hook-type commit-msg
```

Adds ```SECRET_KEY``` and ```PERSONAL_ACCESS_TOKEN``` to SECRET section in github repository and local .env file.

...
