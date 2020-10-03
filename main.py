import os

import telegram
from telegram.ext import CommandHandler, Updater

from log import logger
from telegram_handler import echo_handler, start_handler

if __name__ == "__main__":
    log_ctx = {}

    # set token
    TOKEN = os.getenv("TOKEN", "")
    log_ctx["token"] = TOKEN

    # create updater
    updater = Updater(token=TOKEN, use_context=True)

    # introduce dispatcher locally
    dispatcher = updater.dispatcher

    # register handlers to dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)

    # start bot
    logger.info("About to start a Telegram bot - {}".format(log_ctx))
    updater.start_polling()
