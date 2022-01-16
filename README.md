# car-rest-api
The API is available at: https://kochansky-car-rest-api.herokuapp.com/


# Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Environment](#environment)
* [Available API requests](#available-api-requests)


## General info
Simple rest api in pure Django <br/> 
<li> Django application </li><br/> 
<li> Database(postgresql) </li></br>
<li> Admin Panel(pgadmin) </li>



## Setup
To run this project use the following command in project directory:
```
$ docker-compose build 
$ docker-compose up
```

## Environment
You need to define variables in the environment to build an application in .env file, recommended for quick run just copy and paste: 
```
DEBUG="FALSE"
POSTGRES_USER="root"
POSTGRES_PASSWORD="root"
POSTGRES_DB="test_db"
PGADMIN_DEFAULT_EMAIL="root@root.com"
PGADMIN_DEFAULT_PASSWORD="root"
DB_IPV4_ADDRESS="192.167.0.2"
PGADMIN_IPV4_ADDRESS="192.167.0.3"
APP_IPV4_ADDRESS="192.167.0.4"
SUBNET_IPV4_ADDRESS="192.167.0.0/24"
GATEWAY_IPV4_ADDRESS="192.167.0.1"
```


## Available API requests
List of available API requests.
```
POST /cars/
```
Adds a new car to the database if it exists in an external vpic database.

```
GET /cars/
```
Returns a list of vehicles found in the database with an average ranking
```
DELETE /cars/{id}
```
Removes the vehicle with the specified ID from the database.

```
POST /rate/
```
Adds a new rating to the vehicle with the given id.

```
GET /popular/
```
Returns a list of vehicles based on their number of ratings.
