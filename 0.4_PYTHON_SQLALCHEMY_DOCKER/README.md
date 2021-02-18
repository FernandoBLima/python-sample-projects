# Sample Python Microservice using SQLAlchemy Dockerized #

Follow the instructions below to configure an run this example Python application.

## How to configure

### Example using Docker Compose

In the project's root folder, run the following command to build and run the image.
```bash
$ docker-compose up --build
```

The configuration will create a cluster with 3 containers
- server container
- db container
- pgadmin container

It'll take a few seconds to come up. Then, the server will be accessible on http://localhost:8000

### Pgadmin - PostgreSQL

The Pgadmin is a web application and works as a browser-based client for PostgreSQL that can be accessed on http://localhost:5050 using login with user=pgadmin4@pgadmin.org and password=admin 

### Swagger

The swagger, an automatic interactive API documentation, will be accessible on http://localhost:8000/api/doc

