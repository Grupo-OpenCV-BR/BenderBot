import logging, os
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)
import logging

from Bot import Bot
from Handlers import commandhandlers, messagehandlers
from features import request

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

bender_bot = Bot(False, False)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BOT_NAME = os.getenv("BOT_NAME")
DEBUG = True if os.getenv("DEBUG") else False

PORT = int(os.environ.get('PORT', '5000'))

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info(str(PORT))


async def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():

    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Adicionando handlers diretamente ao application
    application.add_handler(CommandHandler('start', commandhandlers.start))
    application.add_handler(CommandHandler('tutoriais', commandhandlers.tutoriais))
    application.add_handler(CommandHandler('facematch', commandhandlers.facematch))
    application.add_handler(CommandHandler('medicas', commandhandlers.medicas))
    application.add_handler(CommandHandler('eventos', commandhandlers.eventos))
    application.add_handler(CommandHandler('repo', commandhandlers.repo))
    application.add_handler(CommandHandler('vagas', commandhandlers.vagas))
    application.add_handler(CommandHandler('mute_', commandhandlers.mute_))
    application.add_handler(CommandHandler('unmute', commandhandlers.unmute))
    application.add_handler(CommandHandler('help', commandhandlers.help))

    # Adaptando filtros
    echo_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, messagehandlers.echo)
    application.add_handler(echo_handler)

    sys_handler = MessageHandler(filters.StatusUpdate.ALL, messagehandlers.empty_message)
    application.add_handler(sys_handler)

    application.add_error_handler(error)

    logging.info(f'Porta de comunicação {PORT}')

    # Iniciando via webhook
    application.run_polling()



if __name__ == "__main__":
    main()
