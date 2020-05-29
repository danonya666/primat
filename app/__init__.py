from datetime import datetime
from time import time

import telebot
from flask import Flask, request

from app import settings
from app.telegram import bot

server = Flask(__name__)
server.config.from_object(settings)


@server.route(f'/{settings.BOT_TOKEN}', methods=['POST'])
def webhook() -> str:
    timestamp = datetime.fromtimestamp(time())
    print(f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} - Got new telegram bot request")
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return ''


if __name__ == '__main__':
    server.run(debug=False)
