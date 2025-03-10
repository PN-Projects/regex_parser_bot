# commands/regex.py
import re
from telethon import events
from client import client

@client.on(events.NewMessage)
async def handle_regex(event):

    if event.is_reply:
        replied_message = await event.get_reply_message()
        try:
            
            pattern = event.text
  
            result = re.sub(pattern, '', replied_message.text)
          
            await event.reply(f"Result: {result}")
        except re.error:
    
            await event.reply("Invalid regex pattern.")
