# Alticci Sequence Service
![Python Tests CI](https://img.shields.io/github/workflow/status/rarycoringa/alticci-sequence-service/Python%20Tests%20CI?label=tests&logo=pytest&logoColor=white)
![Docker Image CI](https://img.shields.io/github/workflow/status/rarycoringa/alticci-sequence-service/Docker%20Image%20CI?label=docker&logo=docker&logoColor=white)
![Release](https://img.shields.io/github/v/release/rarycoringa/alticci-sequence-service?include_prereleases)
![Tag](https://img.shields.io/github/v/tag/rarycoringa/alticci-sequence-service?include_prereleases)
![License](https://img.shields.io/github/license/rarycoringa/alticci-sequence-service)

## Table of Content

- [About the application](#about-the-application)
  - [Alticci sequence definition](#alticci-sequence-definition)
  - [Technologies](#technologies)
- [Clone the repository](#clone-the-repository)
- [Run using docker and docker-compose](#run-using-docker-and-docker-compose)
- [Run in development mode](#run-in-development-mode)
  - [Environment settings](#environment-settings)
  - [Run unit tests](#run-unit-tests)
  - [Run server](#run-server)


## About the application

This is a Rest API microservice which aims to calculate and return the **$A_n$** term of the **Alticci Sequence**.

### Alticci sequence definition

The Alticci Sequence ($A_n$) is defined following these math rules:

$$
A_n =
  \begin{cases}
    \nexists           & \quad \text{if } n < 0\\
    0                  & \quad \text{if } n = 0\\
    1                  & \quad \text{if } n = 1\\
    1                  & \quad \text{if } n = 2\\
    A_{n-3} + A_{n-2}  & \quad \text{if } n > 2
  \end{cases}
$$

### Technologies

This service is using these technologies:

![Python Badge](https://img.shields.io/badge/Python-v3.10-lightgrey?style=flat&logo=python&logoColor=white&labelColor=gray)
![Flask Badge](https://img.shields.io/badge/Flask-v2.1-lightgrey?style=flat&logo=flask&logoColor=white&labelColor=gray)
![Redis Badge](https://img.shields.io/badge/Redis-v4.3-lightgrey?style=flat&logo=redis&logoColor=white&labelColor=gray)
![Docker Badge](https://img.shields.io/badge/Docker-v20.10-lightgrey?style=flat&logo=docker&logoColor=white&labelColor=gray)

## Clone the repository

The first step is to clone the repository of the project available in the GitHub:

```bash
$ git clone https://github.com/rarycoringa/alticci-sequence-service.git
```

After cloned, make sure you are accessing the project root directory using this command:

```bash
$ cd alticci-sequence-service
```

## Run using docker and docker-compose

If you just would like to use the service's resources, please make sure that Docker and docker-compose is installed and available on your local machine and then run this command on your bash:

```bash
$ docker-compose up --build
```

Presuming you don't have any resource running on the port `8080`, you are now able to use all the service's resources on your local machine.

The following endpoint will to provide a Swagger UI with all required documentation about that resources:

- **GET** `http://localhost:8080/`

> You can use a browser to access http://localhost:8080/ and read the API documentation.

## Run in development mode

### Environment settings

The configuration endpoint is optional, since we have default values to the required configurations. But you can custom development settings with this following environment variables:

```bash
DEBUG=True
USE_REDIS=False
CACHE_DEFAULT_TIMEOUT=60
CACHE_REDIS_HOST=0.0.0.0
CACHE_REDIS_PORT=6379

```

### Run unit tests

To run the unit tests and receive the report about the coverage is just to run this following command:

```bash
$ pipenv run tests
```

### Run server

Ensuring that the tests was completed without issues, it's possible to run the server with development settings just with the following command:

```bash
$ pipenv run server
```
