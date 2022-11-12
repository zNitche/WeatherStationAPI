#FROM python:3.9-buster for RaspberryPi
FROM python:3.9

COPY . /WeatherStationAPI
WORKDIR /WeatherStationAPI

RUN apt update && apt -y install nano curl

RUN curl -o weather_station_api/static/js/libs/chart.js  https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js
RUN pip3 install -r requirements.txt -v

CMD gunicorn -c gunicorn.conf.py app:app --preload