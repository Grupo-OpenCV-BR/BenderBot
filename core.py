import os

from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater

from Handlers import commandhandlers
from Handlers import messagehandlers
from conf.settings import TELEGRAM_TOKEN
from features import request

PORT = int(os.environ.get('PORT', 5000))

class Bot:

    def __init__(self, offenseOn, muteOn):
        self.offenseOn = offenseOn
        self.mute = muteOn


bender_bot = Bot(False, False)


def main():
    request.DontStopmeNOW()

    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', commandhandlers.start))
    dispatcher.add_handler(CommandHandler('mute_', commandhandlers.mute_))
    dispatcher.add_handler(CommandHandler('unmute', commandhandlers.unmute))
    dispatcher.add_handler(CommandHandler('help', commandhandlers.help))

    echo_handler = MessageHandler(Filters.text & (~Filters.command), messagehandlers.echo)
    dispatcher.add_handler(echo_handler)
    sys_handler = MessageHandler(Filters.status_update, messagehandlers.empty_message)
    dispatcher.add_handler(sys_handler)

    updater.start_polling()

    # updater.start_(listen="0.0.0.0",
    #                       port=int(PORT),
    #                       url_path=TELEGRAM_TOKEN)
    # updater.bot.set('https://bender-opencv.herokuapp.com/' + TELEGRAM_TOKEN)

    updater.idle()


if __name__ == "__main__":
    main()
