import os
from dotenv import load_dotenv
from bot import Bot

# Lade Umgebungsvariablen aus der .env-Datei
load_dotenv()

# Erstelle eine Instanz des Bots
bot = Bot()

# Lade Erweiterungen
bot.load_extensions()

# Bestimme den Token
def get_bot_token() -> str:
    return os.getenv('DEV_TOKEN' if os.getenv('dev') else 'BOT_TOKEN')

# Starte den Bot
bot.run(get_bot_token())