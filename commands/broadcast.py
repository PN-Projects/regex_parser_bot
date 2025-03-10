from telethon import events
from client import client
from config import GOD_USER_ID, PRIVILEGED_USER_IDS
import os

@client.on(events.NewMessage(pattern='/addprivileged'))
async def handle_add_privileged(event):
    if event.sender_id != GOD_USER_ID:
        await event.reply("🚫 You do not have permission to use this command.")
        return

    # Extract user ID from the command
    try:
        user_id = int(event.text.split()[1])
    except (IndexError, ValueError):
        await event.reply("Usage: /addprivileged <user_id>")
        return

    # Add the user to the privileged list
    if user_id not in PRIVILEGED_USER_IDS:
        PRIVILEGED_USER_IDS.append(user_id)
        os.environ['PRIVILEGED_USER_IDS'] = ','.join(map(str, PRIVILEGED_USER_IDS))
        await event.reply(f"✅ User {user_id} has been added to the privileged list.")
    else:
        await event.reply(f"ℹ️ User {user_id} is already privileged.")

@client.on(events.NewMessage(pattern='/removeprivileged'))
async def handle_remove_privileged(event):
    if event.sender_id != GOD_USER_ID:
        await event.reply("🚫 You do not have permission to use this command.")
        return

    # Extract user ID from the command
    try:
        user_id = int(event.text.split()[1])
    except (IndexError, ValueError):
        await event.reply("Usage: /removeprivileged <user_id>")
        return

    # Remove the user from the privileged list
    if user_id in PRIVILEGED_USER_IDS:
        PRIVILEGED_USER_IDS.remove(user_id)
        os.environ['PRIVILEGED_USER_IDS'] = ','.join(map(str, PRIVILEGED_USER_IDS))
        await event.reply(f"✅ User {user_id} has been removed from the privileged list.")
    else:
        await event.reply(f"ℹ️ User {user_id} is not privileged.")
