from pyrogram import Client, emoji, filters, types
from langdetect import detect


app = Client(
    "my_account",
    api_id=yourid,
    api_hash="hash"
)

TARGET = "-1001330511111"  # Target chat. Can also be a list of multiple chat ids/usernames
MENTION = "[{}](tg://user?id={})"  # User mention markup
MESSAGE = "{} Welcome to [Pyrogram](https://docs.pyrogram.org/)'s group chat {}!"  # Welcome message
with app:
    # Send a message, Markdown is enabled by default
    app.send_message("me", "Hi there! I'm using **Pyrogram**")

@app.on_message()
def echo(client, message):
    if message.chat.id == {targetgroup}:
        if message.caption:
            lang = detect(message.caption)
            if lang == 'fa' or lang == 'ar':
                app.delete_messages({targetgroup}, message.message_id)
         elif message.message:
             lang = detect(message.caption)
            if lang == 'fa' or lang == 'ar':
                app.delete_messages({targetgroup}, message.message_id)
          

app.run()  # Automatically start() and idle()
