FROM python:3.9

COPY . /WeatherStationAPI
WORKDIR /WeatherStationAPI

RUN apt update && apt -y install nano

RUN pip3 install -r requirements.txt -v

CMD python3 app.py