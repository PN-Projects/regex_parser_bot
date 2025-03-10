# bot.py
from client import client
from commands import start, help, regex, broadcast, stats

# Start the bot
print("Bot is running...")
client.run_until_disconnected()
