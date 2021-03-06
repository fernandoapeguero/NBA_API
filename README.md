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

## Base URL

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

responses with come back in a json object every error response follow the same format.

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

Response Sample:

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

### GET/players?search_term=cu

return all the player in the databse where first or last name matches the search term.

Response Sample:

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

<br>

### GET/players/Player_ID
    
return a player base on the id provided in the url.

Response Sample:

```bash 
{
  "players": {
    "assistance_per_game": 3,
    "first_name": "Shake",
    "id": 14,
    "last_name": "Milton",
    "minutes_per_game": 32,
    "player_number": 18,
    "points_per_game": 23.2,
    "rebounds_per_game": 12.3,
    "team": "76ers"
  },
  "success": true
}
```

<br>

### GET/players/Team_ID/teams
    
return all the player of the specify team.

Response Sample:

```bash
{
  "players": [
    {
      "assistance_per_game": 1.3,
      "first_name": "Reggie",
      "id": 1,
      "last_name": "Bullock",
      "minutes_per_game": 26.2,
      "player_number": 25,
      "points_per_game": 8.6,
      "rebounds_per_game": 3.5,
      "team": "Knicks"
    },
    {
      "assistance_per_game": 2.9,
      "first_name": "Rj",
      "id": 2,
      "last_name": "Barrett",
      "minutes_per_game": 33.4,
      "player_number": 9,
      "points_per_game": 16.5,
      "rebounds_per_game": 6.1,
      "team": "Knicks"
    },
    {
      "assistance_per_game": 3.7,
      "first_name": "ELfrid",
      "id": 3,
      "last_name": "Payton",
      "minutes_per_game": 28,
      "player_number": 6,
      "points_per_game": 12.4,
      "rebounds_per_game": 3.7,
      "team": "Knicks"
    },
    {
      "assistance_per_game": 5.5,
      "first_name": "Julius",
      "id": 4,
      "last_name": "Randle",
      "minutes_per_game": 36.7,
      "player_number": 6,
      "points_per_game": 23.4,
      "rebounds_per_game": 10.9,
      "team": "Knicks"
    },
    ...
  ],
  "success": true,
  "total_players": 6
}
```

<br>

### GET/teams

return all teams in the api paginated in pages of 10 results.

Respose Sample:

```bash
{
  "success": true,
  "teams": [
    {
      "home_city": "New york",
      "id": 1,
      "logo": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/bos.png",
      "losses": "0",
      "name": "Knicks",
      "wins": "0"
    },
    {
      "home_city": "Philadelphia",
      "id": 9,
      "logo": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/bos.png",
      "losses": "0",
      "name": "76ers",
      "wins": "0"
    },
    {
      "home_city": "Houston",
      "id": 10,
      "logo": "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/hou.png",
      "losses": "0",
      "name": "Rockets",
      "wins": "0"
    },
    ...
  ],
  "total_teams": 32
}
```

<br>

### GET/teams/TEAM_ID

return specific team if found.

Response Sample:

```bash
{
  "success": true,
  "team": {
    "home_city": "Phoenix",
    "id": 16,
    "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/a/a2/San_Antonio_Spurs.svg/1200px-San_Antonio_Spurs.svg.png",
    "losses": "0",
    "name": "Suns",
    "wins": "0"
  }
}
```

<br>

### GET /venues

return all venues in the database paginated in pages of 10 results.

Response Sample

```bash
{
  "success": true,
  "total_venues": 4,
  "venues": [
    {
      "id": 1,
      "venue_address": "2121 Biscayne Blvd, Miami",
      "venue_city": "florida",
      "venue_description": "At AmericanAirlines Arena, it is our mission to deliver exceptional guest service, by surpassing each guest’s highest level of expectation.",
      "venue_image": "https://www.aaarena.com/assets/img/Arena-Night-Interior-Slide-be90c5bf85.jpg",
      "venue_is_available": false,
      "venue_name": "America Arena",
      "venue_zipcode": "33137"
    },
    {
      "id": 2,
      "venue_address": "1111 S Figueroa St",
      "venue_city": "los angeles",
      "venue_description": "Staples Center is a multi-purpose arena in Downtown Los Angeles. Adjacent to the L.A. Live development, it is located next to the Los Angeles Convention Center complex along Figueroa Street. The arena opened on October 17, 1999.",
      "venue_image": "https://www.aaarena.com/assets/img/Arena-Night-Interior-Slide-be90c5bf85.jpg",
      "venue_is_available": false,
      "venue_name": "STAPLES Center",
      "venue_zipcode": "33137"
    },
    {
      "id": 3,
      "venue_address": "1 Warriors Way",
      "venue_city": "San Francisco",
      "venue_description": "Chase Center is an indoor arena in the Mission Bay neighborhood of San Francisco, California. The building is the home venue for the Golden State Warriors of the National Basketball Association and occasionally for San Francisco Dons men's basketball.",
      "venue_image": "https://www.aaarena.com/assets/img/Arena-Night-Interior-Slide-be90c5bf85.jpg",
      "venue_is_available": true,
      "venue_name": "Chase Center",
      "venue_zipcode": "94158"
    },
    {
      "id": 7,
      "venue_address": "2121 Biscayne Blvd, Miami",
      "venue_city": "florida",
      "venue_description": "At AmericanAirlines Arena, it is our mission to deliver exceptional guest service, by surpassing each guest’s highest level of expectation.",
      "venue_image": "https://www.aaarena.com/assets/img/Arena-Night-Interior-Slide-be90c5bf85.jpg",
      "venue_is_available": false,
      "venue_name": "AmericanAirlines Arena",
      "venue_zipcode": "33137"
    }
  ]
}
```

<br>

### GET/venue/Venue_ID

return venue base on id.

Response Sample

```bash
{
  "success": true,
  "venue": {
    "id": 1,
    "venue_address": "2121 Biscayne Blvd, Miami",
    "venue_city": "florida",
    "venue_description": "At AmericanAirlines Arena, it is our mission to deliver exceptional guest service, by surpassing each guest’s highest level of expectation.",
    "venue_image": "https://www.aaarena.com/assets/img/Arena-Night-Interior-Slide-be90c5bf85.jpg",
    "venue_is_available": false,
    "venue_name": "America Arena",
    "venue_zipcode": "33137"
  }
}
```

<br>

### GET/events

return all events in the api paginated in pages of 10 results.

Response Sample

```bash
{
  "events": [
    {
      "id": 1,
      "start_time": "Sat, 18 Dec 2021 20:00:00 GMT",
      "team_one": "Rockets",
      "team_two": "Hornets",
      "venue": "America Arena"
    },
    {
      "id": 4,
      "start_time": "Sun, 12 Sep 2021 20:30:00 GMT",
      "team_one": "Hawks",
      "team_two": "Suns",
      "venue": "America Arena"
    },
    ...
  ],
  "success": true,
  "total_events": 6
}
```

<br>

### GET/events/Event_ID

return event base on id provided.

Response Sample

```bash
{
  "events": {
    "id": 1,
    "start_time": "Sat, 18 Dec 2021 20:00:00 GMT",
    "team_one": "Rockets",
    "team_two": "Hornets",
    "venue": "America Arena"
  },
  "success": true
}
```

<br>

### GET/events/Team_id/teams

Return all the event a team have.

Response Sample 

```bash
{
  "events": [
    {
      "id": 1,
      "start_time": "Sat, 18 Dec 2021 20:00:00 GMT",
      "team_one": "Rockets",
      "team_two": "Hornets",
      "venue": "America Arena"
    },
    {
      "id": 7,
      "start_time": "Mon, 30 Aug 2021 20:30:00 GMT",
      "team_one": "Magic",
      "team_two": "Rockets",
      "venue": "America Arena"
    }
  ],
  "success": true,
  "total_events": 2
}
```

<br>

## POST Endpoints

Post a player to the api Auth Require.

Json Object Structure spected by the endpoint Sample

```bash 
    {
	"first_name": "Derrick",
	"last_name": "Rose",
        "player_number": 4,
	"team": "Knicks",
	"mpg": 24.6,
	"ppg": 12.5,
	"rpg": 2.6,
	"apg": 4.9,
	"team_id": 1
}
```

Response Sample 

The endpoint will return the player that was posted in the response.

```bash 
    "success": true,
    {
	"first_name": "Derrick",
	"last_name": "Rose",
        "player_number": 4,
	"team": "Knicks",
	"mpg": 24.6,
	"ppg": 12.5,
	"rpg": 2.6,
	"apg": 4.9,
	"team_id": 1
}
```



