# Alticci Sequence Service

🧮 A microservice responsible to calculate and return the **$A_n$** term of the **Alticci Sequence**.

The Alticci Sequence ($A_n$) is defined following these rules:

$A_0=0$

$A_1=1$

$A_2=1$

$A_n=A_{n-3}+A_{n-2}$

## 1. About the application

| Programming Language | Web Framework | Cache Technology |
|-|-|-|
| **Python** 3.10 | **Flask** 2.1 | **Redis** 7 (using docker env) and **Flask Caching** (using pipenv local env) |  


## 2. Clone service from repository

The first step is clone the repository of the project available at the GitHub. You need just to run this command on your bash:

```bash
$ git clone https://github.com/rarycoringa/alticci-sequence-service.git
```

After cloned, please access the project root directory using this command:

```bash
$ cd alticci-sequence-service
```

## 3. Run service using docker

If you just would like to use the service's resources, please make sure that Docker and docker-compose is installed and available on your local machine and then run this command on your bash:

```bash
$ docker-compose up --build
```

You are now able to use the service's resources on your local machine with a request that looks like this:

- **GET** `http://127.0.0.1:8080/alticci/<term>`

The `term` on the URL must be replaced by the integer term you want the value, like this example: `http://127.0.0.1:8080/alticci/10`.

This endpoint will to return a status code `200 OK` and a json following these format:

```json
{
  "term": 10,
  "value": 9
}
```

... where `"term"` is the integer you passed on the URL and `"value"` is the calculated value of that passed term.

## Run service using pipenv

### Configure environment

```
[env vars]
```

### Run unit tests

```bash
$ pipenv run tests
```

### Run server

```bash
$ pipenv run server
```
