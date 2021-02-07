import requests
import json
import time
import config

BOT_URL = f"https://api.telegram.org/bot{config.telegram_pc_key}/"
OFFSET = 0

def get_updates(offset):
    tg_request = requests.get(BOT_URL + f"getUpdates?offset={offset}")
    try:
        tg_req_data = json.loads(tg_request.text)
        return tg_req_data
    except Exception as e:
        print(e)

def send_message(chat_id, text):
    data = {
        "chat_id": chat_id,
        "text": text
    }
    try:
        requests.post(BOT_URL + "sendMessage", data=data)
    except Exception as e:
        print(e)

while True:
    data = get_updates(OFFSET)
    print(data)
    try:
        result = data["result"]
        for res in result:
            OFFSET = res["update_id"] + 1
            if res["message"]["text"] == "/start":
                send_message(chat_id=res["message"]["chat"]["id"], text="Hello")
    except:
        continue


if __name__ == '__main__':
    pass


