import telebot
from telebot import apihelper
from object_recogniser.secret import tel_token, cool_id

photo_name = 'last_photo.png'

proxy = {
    'https': 'socks5://127.0.0.1:9150'
}
apihelper.proxy = proxy
bot = telebot.TeleBot(token=tel_token)


def send_last_photo_to_admins():
    with open('last_photo.png') as photo:
        bot.send_photo(cool_id, open(photo_name, 'rb'))
