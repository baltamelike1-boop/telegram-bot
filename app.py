from flask import Flask, request
import telegram
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telegram.Bot(token=8461627596:AAG_AEvozCCFL_JrV5ZeJ9pGKPN75rn2Zfk)
app = Flask(__name__)

@app.route('/')
def hello():
    return "Bot is alive"

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text
    bot.send_message(chat_id=chat_id, text=f"Mesajın: {text}")
    return 'ok'

if __name__ == "__main__":
    app.run()
