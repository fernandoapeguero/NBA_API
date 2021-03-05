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

## Base Url 

the base url returns a list of all the question in the api and the categories in the trivia. Pagination is integrated into the api each page will get 10 questions each.

    https://udacity-nba-api.herokuapp.com/

the base url just return welcom to nba api.
  
 ## Error Handling 
 
 Type of error the api handles

   * 400 Bad Request
   * 404 Not Found
   * 405 Method Not Allowed
   * 422 Unproccesable Entity
   * 500 Server Error 
   
Error Handling Response 

```bash
{
  'success': False,
  'error':  400,
  'message': 'Bad request'
}

```

responses with come back in a json object format 

<br>

# Endpoint Library 

Here you will find all the endpoint you need to work with the api 

The Structure of the EndPoint library is simple since you will deploy the backend localy for this app we know the domain will be https://udacity-nba-api.herokuapp.com/
and you will only need the path for example /players in this library we will prefix the path with the method needed for the call. 

### Pagination 

The project paginates the result in pages of 10 objects by passing what page you what in the query example: https://udacity-nba-api.herokuapp.com/players?page=2 will return the second page of the players results 

* Pagination amount change in future release of the project so you can pass how many results per page you will need.

<br>

## GET Endpoints 

### GET/players

return all players in the database paginated in pages of 10.

Response

```bash
  {
   "players":[
      {
         "assistance_per_game":1.3,
         "first_name":"Reggie",
         "id":1,
         "last_name":"Bullock",
         "minutes_per_game":26.2,
         "player_number":25,
         "points_per_game":8.6,
         "rebounds_per_game":3.5,
         "team":"Knicks"
      },
      {
         "assistance_per_game":2.9,
         "first_name":"Rj",
         "id":2,
         "last_name":"Barrett",
         "minutes_per_game":33.4,
         "player_number":9,
         "points_per_game":16.5,
         "rebounds_per_game":6.1,
         "team":"Knicks"
      },
      ...
   ],
   "success":true,
   "total_players":16
}
```

<br>

### GET/Player?search_term=cu

return all the player in the daatabse where first or last name matches the search term.

Response

```bash
{
  "players": [
    {
      "assistance_per_game": 3.7,
      "first_name": "Seth",
      "id": 10,
      "last_name": "Curry",
      "minutes_per_game": 25,
      "player_number": 11,
      "points_per_game": 15.4,
      "rebounds_per_game": 1.9,
      "team": "76ers"
    }
  ],
  "success": true,
  "total_players": 1
}
```






