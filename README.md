# WeatherStationAPI

API for [Raspberry Pi Pico W powered weather stations](https://github.com/zNitche/PicoWeatherStation) with data preview dashboard

---

## Production Setup
1. Clone this repo.
2. Generate `.env` config file and change config values.
```
python3 generate_dotenv.py
```
3. Run docker container.
```
sudo docker compose up -d
```

## Tests
Run tests:
```
pytest -v tests/
```
