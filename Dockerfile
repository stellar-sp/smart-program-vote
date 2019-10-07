FROM python:2.7.15-jessie

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./vote.py" ]