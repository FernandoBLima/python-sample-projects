# Sample Python Microservices Dockerized using AIOHTTP #
---

## How to configure

### Run using Docker Compose
In the project's root folder, run the following command to build the image.
```bash
$ docker-compose up --build
```

### Run using Docker
Build the image of server or gateway project in the root path of each project using the following command:
```bash
$ docker build -t <IMAGE_NAME> .
```

Then, run the docker container using the command shown below:
```bash
$ docker run -p <HOST_PORT>:<CONTAINER_PORT> <IMAGE_NAME>
```

In the command above, it used the -p flag that means publish on the docker run command. The application will be accessible at http://localhost:<HOST_PORT>


### Run locally
Run the server or gateway project locally on the root path of each project using the following command:

Installation requirements:
```bash
install -r requirements.txt
```

Running locally:
```bash
python api/index.py
```
