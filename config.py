import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MISTRAL_TOKEN = os.getenv("MISTRAL_TOKEN")