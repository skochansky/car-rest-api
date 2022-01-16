# car-rest-api


# Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Environment](#environment)


## General info
Budget and investment management application with containerized: <br/> 
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



