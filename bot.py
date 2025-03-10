from client import client
from commands import start, help, regex, broadcast, admin

# Start the bot
print("Bot is running...")
client.run_until_disconnected()
