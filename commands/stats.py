# commands/stats.py
from telethon import events
from client import client
from database import get_users, get_groups

@client.on(events.NewMessage(pattern='/stats'))
async def handle_stats(event):

    users = await get_users()
    groups = await get_groups()


    stats_message = (
        f"**Bot Statistics:**\n"
        f"Total Users: {len(users)}\n"
        f"Total Groups: {len(groups)}"
    )

    # Send the stats message
    await event.reply(stats_message)
