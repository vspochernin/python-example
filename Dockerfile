# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

CMD [ "python3", "server.py" ]
CMD [ "python3", "client.py" ]
