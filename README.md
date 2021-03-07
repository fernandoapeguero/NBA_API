# Introduction 

### NBA Api

This projects is base on the nba it have endpoints for teams, players, venues and events. I Implemented a roles base access to the api depending on who you are the teams manager, venue management or the nba commission 
you have different access too the api depending on your role you may be restricted from accesing, updating or creating information for the api

## Motivation 

My motivatin behind this project is to created an api that is not necessarily use in the nba but it can be use openly by any entity that plays basketball to have for their teams games for example high schools, colleges can use it and change the structure to suit them. I think this is a good starting point for a open source api that can expand and even be use in more places.

# Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies in the directory:

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

In this project for unnitest in your local machine pleas update the postgres URI information on the test_api file to match your own postgres database.

### Importing Data to Postgres

There is a file call db_nba.dump that is with the project it haves some data thtat can be use for testing purposes. To import the data to your postgress database use this command 

```bash
psql -U (postgres username) --dbname=(database name) db_nba.dump
```
> :warning: **You will need to run the command more than once because of the database contraint**: The contraint causes for some data to imported first because is needed for other to exists in the database!

### How to run unittest in this project 

You will need to change a couple of things. First create the database you want to use for testing or use the same name that is already declare. 
Change the DATABASE_URL environment variable to LOCA_DATABASE_URL environ variable so you are able to perfom the database migration localy to the test database.




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

## Roles and Access

This is the role structure for this project is does not represent everyway the project can be use you can update or change it to fit your needs.

Team Management - Permission for this Role.

```bash
Post Players

Patch Players
Patch Teams

Delete Players
```

Venue Management
```bash
Post Venues
Post Events

Patch Venues
Patch Events

Delete Venues
Delete Events


```

Nba Comission
```bash
Post Players
Post Teams

Patch Players
Patch Teams

Delete Player
Delete Teams 
Delete Events
```

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

### POST/players

Role: Team Management, Nba comission

Post a player to the api Auth Require.

Json Object Structure expected by the endpoint Sample

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

```bash 
    "success": true,
    {
    	"id": 18,
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

<br>

### POST/teams

Post a team to the api Auth Require.


Json Object Structure expected by the endpoint Sample

```bash
{
    "name": "Timberwolves",
    "home_city": "Minnesota",
    "losses": 0,
    "wins": 0,
    "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/Minnesota_Timberwolves_logo.svg/1200px-Minnesota_Timberwolves_logo.svg.png"
}
```

Response Sample

```bash
"success": true,
{
    "id": 4, 
    "name": "Timberwolves",
    "home_city": "Minnesota",
    "losses": 0,
    "wins": 0,
    "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/Minnesota_Timberwolves_logo.svg/1200px-Minnesota_Timberwolves_logo.svg.png"
}
```

<br>

### POST/venues

Post a venue to the api Auth Require

Json Object Structure expected by the endpoint Sample

```bash 
{
    "name": "AmericanAirlines Arena",
    "address": "2121 Biscayne Blvd, Miami",
    "city": "florida",
    "zipcode": "33137",
    "is_available": false,
    "image": "https://www.aaarena.com/assets/img/Arena-Night-Interior-Slide-be90c5bf85.jpg",
    "description": "At AmericanAirlines Arena, it is our mission to deliver exceptional guest service, by surpassing each guest’s highest level of expectation."
}
```

Response Sample

```bash
"success": true,
{
    "id": 15,
    "name": "AmericanAirlines Arena",
    "address": "2121 Biscayne Blvd, Miami",
    "city": "florida",
    "zipcode": "33137",
    "is_available": false,
    "image": "https://www.aaarena.com/assets/img/Arena-Night-Interior-Slide-be90c5bf85.jpg",
    "description": "At AmericanAirlines Arena, it is our mission to deliver exceptional guest service, by surpassing each guest’s highest level of expectation."
}
```

<br>

### POST/events

Post a event to the api Auth Require.

```bash
{
    "team_id": 23,
    "team_id_two": 26,
    "venue_id":  2,
    "start_time": "2021-12-18 20:00:00"
}
```

Response Sample

```bash
"success": true,
{
  "id": 42,
  "venue": "Madison Square Garden",
  "team_one": "knicks",
  "Team_Two": "Spurs",
  "Start_time": "2021-12-18 20:00:00"
}
```

<br>

## PATCH Endpoints

### PATCH/players/PLAYER_ID

Role Require: Team Management, Nba comission

Updates a player information in the api

Sample Json Structure.


```bash
{
    "first_name": "Joel"
}
```

Response Sample

```bash 
    "success": true,
{
    "id": 12,
    "first_name": "Joel",
    "last_name": "spenser",
    "player_number": 4,
    "team": "Knicks",
    "mpg": 24.6,
    "ppg": 12.5,
    "rpg": 2.6,
    "apg": 4.9,
    "team_id": 1
}
```

<br>

### PATCH/teams/TEAM_ID

Updated a team information in the api.

Json Structure Sample 

```bash
{
    "name": "Timberwolves Grounders",

}
```

Response Sample

```bash
"success": true,
{
    "id": 1,
    "name": "Timberwolves Grounders",
    "home_city": "Minnesota",
    "losses": 0,
    "wins": 0,
    "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/Minnesota_Timberwolves_logo.svg/1200px-Minnesota_Timberwolves_logo.svg.png"
}
```

<br>

### PATCH/venues/VENUE_ID

Updated a venue information on the api 

Json Structure Sample

```bash 
{
    "name": "American Airlines Arena",
    "is_available": true,
   
}
```

Response Sample

```bash 
"success": true,
{
    "name": "American Airlines Arena",
    "address": "2121 Biscayne Blvd, Miami",
    "city": "florida",
    "zipcode": "33137",
    "is_available": false,
    "image": "https://www.aaarena.com/assets/img/Arena-Night-Interior-Slide-be90c5bf85.jpg",
    "description": "At AmericanAirlines Arena, it is our mission to deliver exceptional guest service, by surpassing each guest’s highest level of expectation."
}
```

<br>

### PATCH/events/EVENT_ID

Updated a venue information in the api.

Json Sample Structure 

```bash 
{
    "team_id": 14,
    "venue_id": 8
}
```


```bash
"success": true,
{
  "id": 42,
  "venue": "American Airlines arena",
  "team_one": "Heat",
  "Team_Two": "Spurs",
  "Start_time": "2021-12-18 20:00:00"
}
```

<br>

## DELETE Endpoints

### DELETE/players/PLAYER_ID

Role Require: Team Manager, Nba comission

Deletes a player from the api.

the endpoint will return the deleted player in the response.

```bash
"success": true,
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
}
```

### DELETE/teams/TEAM_ID

Deletes a team from the api.

the endpoint will return the deleted team in the response.

```bash
"success": true,
{
    "id": 1,
    "name": "Timberwolves Grounders",
    "home_city": "Minnesota",
    "losses": 0,
    "wins": 0,
    "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/Minnesota_Timberwolves_logo.svg/1200px-Minnesota_Timberwolves_logo.svg.png"
}
```

<br>

### DELETE/venues/VENUE_ID

Deletes a venue from the api .

The endpoint will return the deleted venue in the response.

```bash
"success":true,
{
    "name": "American Airlines Arena",
    "address": "2121 Biscayne Blvd, Miami",
    "city": "florida",
    "zipcode": "33137",
    "is_available": false,
    "image": "https://www.aaarena.com/assets/img/Arena-Night-Interior-Slide-be90c5bf85.jpg",
    "description": "At AmericanAirlines Arena, it is our mission to deliver exceptional guest service, by surpassing each guest’s highest level of expectation."
}

```

<br>

### DELETE/events/EVENT_ID

Delete a Event From the api.

The endpoint will return the deleted event in the response. 

```bash
"success": true,
{
  "id": 42,
  "venue": "AMerican Airlines Arena",
  "team_one": "Heats",
  "Team_Two": "Spurs",
  "Start_time": "2021-12-18 20:00:00"
}

```
