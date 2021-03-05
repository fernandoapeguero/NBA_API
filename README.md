# Introduction 

### NBA Api

This projects is base on the nba it have endpoints for teams, players, venues and events. I Implemented a roles base access to the api depending on who you are the teams manager, venue management or the nba commission 
you have different access too the api depending on your role you may be restricted from accesing, updating or creating information for the api

# Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## running the project localy 

Running the project locally is very simple there are a couple of things you have to change to be able to use.

* Change the database path in the models.py file to your local posgres uri.
* Change the 2 environment variable in the auth.py file to your own auth0 information.
* Create a database to use in the project 
* Run upgrage for flask migrate to create your tables 

## How to run migration 

for reference [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/) a database migrations for Flask applications using Alembic.

In this project i'm using a file to manage the migration and that way is able to work on heroku as well so the way you will call it is the same but you have to use the file itself for example.

* Normal migration call flask db migrate -m "some change to models"
* Using manage.py file - python managepy. db migrate -m "some change to models"

The same examle apply for upgrading the database using the manage.py file.


## Testing 

The project is using postman and unittest to check that the endpoint are working correctly and a runner file is provided with the project so you can check that every endpoint is working corretly.

Unittest is use to check for public endpoint 
Postman is use to check the public and jwt authentificated endpoint

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 


