![Build](https://github.com/SemenovAV/core/workflows/Build/badge.svg)

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

Edit the code

and commit the changes using the command:
```angular2html
cz commit
```
