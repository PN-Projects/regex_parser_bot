# commands/help.py
from telethon import events
from client import client

@client.on(events.NewMessage(pattern='/help'))
async def handle_help(event):
    help_text = """
    **Available Commands:**
    - `/start`: Start the bot and get added to the database.
    - `/help`: Show this help message.
    - `/stats`: Show the number of users and groups in the database.
    - `/broadcast -u <message>`: Broadcast a message to all users.
    - `/broadcast -g <message>`: Broadcast a message to all groups.
    - `/broadcast -all <message>`: Broadcast a message to both users and groups.
    - Reply to a message with a regex pattern to apply it.
    """
    await event.reply(help_text)
