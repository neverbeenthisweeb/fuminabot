import os
import random

import telegram
from telegram.ext import CommandHandler, Filters, MessageHandler

from log import logger


def start(update: telegram.update.Update, context: telegram.ext.callbackcontext.CallbackContext):
    logger.debug(
        "Received an update on start handler - {}".format(update))
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Hi, I am Fumina Hoshino!")


def echo(update: telegram.update.Update, context: telegram.ext.callbackcontext.CallbackContext):
    logger.debug(
        "Received an update on echo handler - {}".format(update))
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text)


def img(update: telegram.update.Update, context: telegram.ext.callbackcontext.CallbackContext):
    logger.debug(
        "Received an update on img handler - {}".format(update))
    # get image
    img_file = open("imgs/{}".format(_get_img()), "rb")

    # get quotes for caption
    quotes = random.choice(_get_quotes())

    context.bot.send_photo(
        chat_id=update.effective_chat.id, photo=img_file, caption=quotes)


def _get_quotes() -> list:
    list_of_quotes = open("captions/quotes.txt", "r")

    return list_of_quotes.readlines()


def _get_img() -> str:
    list_of_images = os.listdir("imgs/")

    return random.choice(list_of_images)


# define handlers
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
img_handler = CommandHandler('img', img)
