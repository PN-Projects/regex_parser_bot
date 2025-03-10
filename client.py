# client.py
from telethon import TelegramClient
from config import API_ID, API_HASH, BOT_TOKEN

client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
