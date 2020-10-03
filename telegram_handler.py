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


# define handlers
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
