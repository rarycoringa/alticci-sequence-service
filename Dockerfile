FROM python:3.10-alpine

RUN apk update

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY ./Pipfile .
COPY ./Pipfile.lock .
RUN pip install pipenv
RUN pipenv install --deploy
COPY . .

CMD ["pipenv", "run", "server"]
