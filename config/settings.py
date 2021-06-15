import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BOT_NAME = os.getenv("BOT_NAME")
DEBUG = os.getenv("DEBUG")
PORT = int(os.environ.get('PORT', 5000))

#BASE_API_URL = os.getenv("BASE_API_URL")