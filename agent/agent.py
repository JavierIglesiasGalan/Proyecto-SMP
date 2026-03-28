import psutil
import requests
import time

API_URL = "http://localhost:8000/metrics"

while True:
    data = {
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent
    }

    requests.post(API_URL, json=data)
    time.sleep(5)