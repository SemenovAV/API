![Build](https://github.com/SemenovAV/core/workflows/Build/badge.svg)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# Django template



## First usage

If the pipenv package is not installed:

``` 
pip install pipenv 

```

then:
```
pipenv shell
pipenv install --skip-lock --dev
pipenv lock --pre
pre-commit install --hook-type commit-msg
```
Create file .env to project root.

Add:
 * ```SECRET_KEY``` - django secret key,
 * ```POSTGRES_DB```,
 * ```POSTGRES_USER``` ,
 * ```POSTGRES_PASSWORD ```,
 * ```POSTGRES_HOST ``` ,
 * ```POSTGRES_PORT ```  
   
   variables to SECRET section in github repository and local .env file.

## Usage

Edit the code.

Commit the changes using the command:
```
cz commit
```
