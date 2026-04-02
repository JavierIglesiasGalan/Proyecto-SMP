import time
import requests
import psutil
from config import API_URL, SERVER_ID, INTERVAL


def get_metrics():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
        "server_id": SERVER_ID
    }


def send_metrics(data):
    try:
        response = requests.post(API_URL, json=data, timeout=5)
        if response.status_code == 200:
            print("Sent:", data)
        else:
            print("⚠️ Error:", response.status_code, response.text)
    except Exception as e:
        print("Connection error:", e)


def main():
    print("Agent started...")

    while True:
        metrics = get_metrics()
        send_metrics(metrics)
        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()