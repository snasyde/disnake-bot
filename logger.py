import logging
import disnake

# Definieren des Log-Formats
log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')

# Console-Handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(log_format)

# Disnake-Logger
disnake_logger = disnake.logging.getLogger('disnake')
disnake_logger.setLevel(logging.DEBUG)
disnake_handler = logging.FileHandler(filename='logs/disnake.log', encoding='utf-8', mode='w')
disnake_handler.setFormatter(log_format)
disnake_logger.addHandler(disnake_handler)

# Bot-Logger
bot_logger = logging.getLogger('bot')
bot_logger.setLevel(logging.DEBUG)
bot_handler = logging.FileHandler(filename='logs/bot.log', encoding='utf-8', mode='w')
bot_handler.setFormatter(log_format)
bot_logger.addHandler(bot_handler)
bot_logger.addHandler(console_handler)
