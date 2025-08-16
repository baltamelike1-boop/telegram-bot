import os
import requests

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

API_URL = f"https://api.telegram.org/bot{TOKEN}"

def send_message(chat_id, text):
    url = f"{API_URL}/sendMessage"
    data = {'chat_id': chat_id, 'text': text}
    requests.post(url, data=data)

def main():
    print("Bot çalışıyor...")

if __name__ == '__main__':
    main()
