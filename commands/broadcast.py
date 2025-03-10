# commands/broadcast.py
from telethon import events
from client import client
from database import get_users, get_groups

@client.on(events.NewMessage(pattern='/broadcast'))
async def handle_broadcast(event):
    args = event.text.split()
    if len(args) < 2:
        await event.reply("Usage: /broadcast [-u|-g|-all] [message]")
        return

    flag = args[1]
    if flag not in ['-u', '-g', '-all']:
        await event.reply("Invalid flag. Use -u, -g, or -all.")
        return

    if event.is_reply:
        message = (await event.get_reply_message()).text
    else:
        message = ' '.join(args[2:])

    if flag == '-u':
        users = await get_users()
        for user_id in users:
            await client.send_message(user_id, message)
    elif flag == '-g':
        groups = await get_groups()
        for group_id in groups:
            await client.send_message(group_id, message)
    elif flag == '-all':
        users = await get_users()
        groups = await get_groups()
        for user_id in users:
            await client.send_message(user_id, message)
        for group_id in groups:
            await client.send_message(group_id, message)

    await event.reply("Broadcast completed.")
