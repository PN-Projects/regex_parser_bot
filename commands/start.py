from telethon import Button, events
from client import client
from database import add_user

@client.on(events.NewMessage(pattern='/start'))
async def handle_start(event):

    user_id = event.sender_id
    await add_user(user_id)

  
    add_to_group_button = Button.url(
        text="Add Me to Your Group 🚀",
        url=f"https://t.me/{client.me.username}?startgroup=true"
    )

  
    welcome_message = (
        "🎉 **Hey there! I’m the Regex Wizard!** 🧙‍♂️\n\n"
        "I can **magically transform messages** using regex patterns. Just reply to any message with a regex, and I’ll do the rest!\n\n"
        "Add me to your group to unleash my regex powers! 👇"
    )


    await event.respond(
        welcome_message,
        buttons=[add_to_group_button]
    )

    print(f"Added user: {user_id}")
