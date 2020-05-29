from random import shuffle

import telebot
from telebot import types

from app import classifier, settings

from . import replies


bot = telebot.TeleBot(settings.BOT_TOKEN)


def process_picture(photo: list):
    file_id = photo[-1].file_id
    file = bot.get_file(file_id)
    downloaded_file = bot.download_file(file.file_path)
    return downloaded_file


def save_picture(picture: bytes) -> None:
    with open('last_picture.png', 'wb') as file:
        file.write(picture)


@bot.message_handler(commands=['start', 'help'])
def help_handler(message: types.Message) -> None:
    print("%s: %s" % (message.chat.id, message.text))
    bot.send_message(message.chat.id, replies.START_REPLY.format(message.from_user.username))


@bot.message_handler(content_types=['photo'])
def recognize_object(message: types.Message) -> None:
    print("%s sent a picture" % message.chat.id)
    picture = process_picture(message.photo)
    if settings.STAGE == 'dev':
        save_picture(picture)
    predictions = classifier.predict(picture)
    classes = sorted(predictions.items(), key=lambda item: item[1], reverse=True)
    prediction = classes[0][0]
    print("The prediction is %s" % prediction)
    if classes[0][1] > settings.CONFIDENCE_THRESHOLD:
        answers = replies.CERTAIN_DECISION_REPLIES
        print("The object surely is %s" % prediction)
    elif classes[0][1] < settings.UNCERTAINTY_THRESHOLD:
        answers = replies.NO_DECISION_REPLIES
        print("The object was not recognized")
    else:
        answers = replies.UNCERTAIN_DECISION_REPLIES
        print("The object probably is %s" % prediction)
    shuffle(answers)
    reply = answers[0]
    bot.send_message(message.chat.id, reply.format(prediction))


@bot.message_handler(func=lambda message: True)
def unknown_message(message: types.Message) -> None:
    print("%s: %s" % (message.chat.id, message.text))
    bot.send_message(message.chat.id, replies.START_REPLY)
