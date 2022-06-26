# Alticci Sequence Service
![Python Tests CI](https://img.shields.io/github/workflow/status/rarycoringa/alticci-sequence-service/Python%20Tests%20CI?label=tests&logo=pytest&logoColor=white)
![Docker Image CI](https://img.shields.io/github/workflow/status/rarycoringa/alticci-sequence-service/Docker%20Image%20CI?label=docker&logo=docker&logoColor=white)
![Release](https://img.shields.io/github/v/release/rarycoringa/alticci-sequence-service?include_prereleases)
![Tag](https://img.shields.io/github/v/tag/rarycoringa/alticci-sequence-service?include_prereleases)
![License](https://img.shields.io/github/license/rarycoringa/alticci-sequence-service)

## 1. About the application

A Rest API microservice to calculate and return the **$A_n$** term of the **Alticci Sequence**.

The Alticci Sequence ($A_n$) is defined following these rules:

$$
A_n =
  \begin{cases}
    0                  & \quad \text{if } n = 0\\
    1                  & \quad \text{if } n = 1\\
    1                  & \quad \text{if } n = 2\\
    A_{n-3} + A_{n-2}  & \quad \text{if } n > 2
  \end{cases}
$$

| Programming Language | Web Framework | Cache Technology |
|-|-|-|
| **Python** 3.10 | **Flask** 2.1 | **Redis** 7 (using docker env) and **Flask Caching** (using pipenv local env) |  


## 2. Clone service from repository

The first step is clone the repository of the project available at the GitHub:

```bash
$ git clone https://github.com/rarycoringa/alticci-sequence-service.git
```

After cloned, make sure you are accessing the project root directory using this command:

```bash
$ cd alticci-sequence-service
```

## 3. Run service using docker

If you just would like to use the service's resources, please make sure that Docker and docker-compose is installed and available on your local machine and then run this command on your bash:

```bash
$ docker-compose up --build
```

Presuming you don't have any resource running on the port `8080`, you are now able to use all the service's resources on your local machine.

The following endpoint will to provide a Swagger UI with all required documentation about that resources:

- **GET** `http://localhost:8080/`

## 4. Run service using pipenv

### 4.1. Environment settings

The configuration endpoint is optional, since we have default values for the required configurations. But you can custom development settings with this following environment variables:

```bash
DEBUG=True
USE_REDIS=False
CACHE_DEFAULT_TIMEOUT=60
CACHE_REDIS_HOST=0.0.0.0
CACHE_REDIS_PORT=6379

```

### 4.2. Run unit tests

To run the unit tests and receive the report about the coverage is just to run this following command:

```bash
$ pipenv run tests
```

### 4.3. Run server

Ensuring that the tests was completed without issues, it's possible to run the server with development settings just with the following command:

```bash
$ pipenv run server
```
