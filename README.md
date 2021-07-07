# Trenfding_Languages_Task

# Motivations 
it is a Django Project for getting 
the first 100 programming language used in github repos last month: 
- Django. 
- Django Rest Framework. 

## Getting Started

### Pre-requisites and Local Development
Developers using this project should already have Python3, Django and pipenv installed in their local machines.

#### PIP Dependencies
run this command in the root of the project that will create virtual environment and install dependencies. 
```bash
pipenv install
``` 
to activate the virtual env run this. 
```bash
pipenv shell
```   
to migrate.
```bash 
python manage.py migrate
```   
To run the server, execute this command in the root folder:
```bash 
python manage.py runserver
``` 
## API Reference

### Endpoints

#### GET '/languages/100/'

   - get the first 100 trending languages.
   
   - Return an data object which hase the returned trending langiages and it's data(cont and repos) ffor every language.
     ```
      "data": {
        "AutoIt": {
            "count": 1,
            "repositories": [
                {},
                {},
           ]
           :
           :
           :
       }
     ```
## Tests
 
```bash 
python manage.py test
``` 
