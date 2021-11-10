import logging
import os

from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater

from Bot import Bot
from Handlers import commandhandlers, messagehandlers
from features import request

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

bender_bot = Bot(False, False)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BOT_NAME = os.getenv("BOT_NAME")
DEBUG = True if os.getenv("DEBUG") else False

PORT = int(os.environ.get('PORT', '5000'))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info(str(PORT))


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    request.DontStopmeNOW()

    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', commandhandlers.start))
    dispatcher.add_handler(CommandHandler('eventos', commandhandlers.eventos))
    dispatcher.add_handler(CommandHandler('repo', commandhandlers.repo))
    dispatcher.add_handler(CommandHandler('vagas', commandhandlers.vagas))
    dispatcher.add_handler(CommandHandler('mute_', commandhandlers.mute_))
    dispatcher.add_handler(CommandHandler('unmute', commandhandlers.unmute))
    dispatcher.add_handler(CommandHandler('help', commandhandlers.help))

    echo_handler = MessageHandler(Filters.text & (~Filters.command), messagehandlers.echo)
    dispatcher.add_handler(echo_handler)
    sys_handler = MessageHandler(Filters.status_update, messagehandlers.empty_message)
    dispatcher.add_handler(sys_handler)
    dispatcher.add_error_handler(error)

    updater.start_polling()

    logging.info(f'Porta de comunicação {PORT}')

    #updater.start_webhook(listen="0.0.0.0",
    #                      port=PORT,
    #                      url_path=TELEGRAM_TOKEN,
    #                   webhook_url='https://bender-opencv.herokuapp.com/' + TELEGRAM_TOKEN)
    updater.idle()


if __name__ == "__main__":
    main()
