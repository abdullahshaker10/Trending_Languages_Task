# Trenfding_Languages_Task

# Motivations 
it is a Django Project for getting 
the first 100 programming language used in GitHub repositories last month: 
- Django. 
- Django Rest Framework. 

## Getting Started

### Pre-requisites and Local Development
Developers using this project should already have Python3, Django, and pipenv installed in their local machines.

#### PIP Dependencies
run this command in the root of the project that will create a virtual environment and install dependencies. 
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
   
   - Return a data object which has the returned trending languages and its data(cont and repositories) for every language.
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
## Note 
I realized that there are repositories with "null" programming language and I think it is helpful to show it 
with others.

