import multiprocessing
from config import AppConfig


bind = f"{AppConfig.APP_HOST}:{AppConfig.APP_PORT}"


workers = multiprocessing.cpu_count() * 2 - 1
threads = 2
worker_class = "gthread"
worker_connections = 1000

timeout = 10
keepalive = 5
