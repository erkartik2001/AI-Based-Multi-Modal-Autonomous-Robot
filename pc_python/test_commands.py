import requests

ESP_IP = "192.168.1.19"

while True:
    cmd = input("Enter your command (F/B/L/R/S): ")

    if cmd.isalpha():
        cmd = cmd.upper()

    requests.get(f"http://{ESP_IP}/{cmd}")