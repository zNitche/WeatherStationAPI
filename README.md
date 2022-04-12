# WeatherStationAPI

API for Raspberry Pi Pico powered weather stations

---

### Setup Docker container
#### Note: for Raspberry Pi use `python:3.9-buster` as Docker image

   1. Build image: 
   ```
   sudo docker build -t weather_station_api .
   ```
   2. Run container:
   ```
   sudo docker run -d \
    -p 8080:8080 \
    -v <path_to_data_dir>:/WeatherStationAPI/data \
    -v /etc/timezone:/etc/timezone:ro \
    -v /etc/localtime:/etc/localtime:ro \
    --name weather_station_api weather_station_api
   ```
   3. Make container auto startup:
   ```
   sudo docker update --restart unless-stopped weather_station_api
   ```
