from pyrogram import Client, emoji, filters, types
from langdetect import detect


app = Client(
    "my_account",
    api_id=1913141,
    api_hash="94eebf5e4fca229dc7aa9d3d7f0b5b71"
)

TARGET = "-1001330524944"  # Target chat. Can also be a list of multiple chat ids/usernames
MENTION = "[{}](tg://user?id={})"  # User mention markup
MESSAGE = "{} Welcome to [Pyrogram](https://docs.pyrogram.org/)'s group chat {}!"  # Welcome message
with app:
    # Send a message, Markdown is enabled by default
    app.send_message("me", "Hi there! I'm using **Pyrogram**")

@app.on_message()
def echo(client, message):
    if message.chat.id == -1001330524944:
        if message.caption:
            lang = detect(message.caption)
            if lang == 'fa' or lang == 'ar':
                app.delete_messages(-1001330524944, message.message_id)
                print(message.message_id)
                print('deleted ^')

app.run()  # Automatically start() and idle()
