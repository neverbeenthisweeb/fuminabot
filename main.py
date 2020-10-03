import os

import telegram
from telegram.ext import CommandHandler, Updater

from log import logger


def start(update: telegram.update.Update, context: telegram.ext.callbackcontext.CallbackContext):
    logger.info(
        "Received an update on start handler - {}".format(update))
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Hi, I am Fumina Hoshino!")


if __name__ == "__main__":
    log_ctx = {}

    # set token
    TOKEN = os.getenv("TOKEN", "")
    log_ctx["token"] = TOKEN

    # create updater
    updater = Updater(token=TOKEN, use_context=True)

    # introduce dispatcher locally
    dispatcher = updater.dispatcher

    # define handler
    start_handler = CommandHandler('start', start)

    # register handler to dispatcher
    dispatcher.add_handler(start_handler)

    # start bot
    logger.info("About to start a Telegram bot - {}".format(log_ctx))
    updater.start_polling()
