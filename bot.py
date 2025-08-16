import os
import requests
import time

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
API_URL = f"https://api.telegram.org/bot{TOKEN}"

def send_message(chat_id, text):
    url = f"{API_URL}/sendMessage"
    data = {'chat_id': chat_id, 'text': text}
    requests.post(url, data=data)

def get_updates(offset=None):
    url = f"{API_URL}/getUpdates"
    params = {'timeout': 100, 'offset': offset}
    resp = requests.get(url, params=params)
    return resp.json()

def main():
    print("Bot çalışıyor...")
    offset = None

    while True:
        updates = get_updates(offset)
        if 'result' in updates:
            for update in updates['result']:
                offset = update['update_id'] + 1
                if 'message' in update:
                    chat_id = update['message']['chat']['id']
                    text = update['message'].get('text', '')
                    send_message(chat_id, f"Gelen mesaj: {text}")
        time.sleep(1)

if __name__ == '__main__':
    main()
