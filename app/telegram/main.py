from random import shuffle

import telebot
from telebot import types

from app import classifier, converter, settings

from . import replies


bot = telebot.TeleBot(settings.BOT_TOKEN)


def save_picture(picture: bytes, filepath: str = settings.DEFAULT_IMAGE_PATH) -> str:
    with open(filepath, 'wb') as file:
        file.write(picture)
        return filepath


def process_picture(photo: list) -> bytes:
    file_id = photo[-1].file_id
    file = bot.get_file(file_id)
    downloaded_file = bot.download_file(file.file_path)
    return downloaded_file


@bot.message_handler(commands=['start'])
def start_handler(message: types.Message) -> None:
    print("%s: %s" % (message.chat.id, message.text))
    bot.send_message(message.chat.id, replies.START_REPLY.format(message.from_user.username))


@bot.message_handler(commands=['help'])
def start_handler(message: types.Message) -> None:
    print("%s: %s" % (message.chat.id, message.text))
    bot.send_message(message.chat.id, replies.HELP_REPLY)


@bot.message_handler(content_types=['photo'])
def recognize_object(message: types.Message) -> None:
    print("%s sent a picture" % message.chat.id)
    picture = process_picture(message.photo)
    filepath = save_picture(picture)
    image = converter.convert_image(filepath)
    predictions = classifier.predict_class(image)
    for k, v in predictions.items():
        print(f"{k}: %.5f" % v)
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
    bot.send_message(message.chat.id, reply.format(prediction.lower()))


@bot.message_handler(func=lambda message: True)
def unknown_message(message: types.Message) -> None:
    print("%s: %s" % (message.chat.id, message.text))
    bot.send_message(message.chat.id, replies.HELP_REPLY)
