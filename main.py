import logging
import sys
from pyrogram import Client
from configurator import my_api

logging.basicConfig(
    filename="temp/fox_userbot.log",
    filemode='w',
    format='%(asctime)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    level=logging.INFO
)

api_id, api_hash = my_api()

# Restart
app = Client("my_account")
with app:
    if len(sys.argv) == 4:
        restart_type = sys.argv[3]
        if restart_type == "1":
            text = "<code>Update process completed!</code>"
        else:
            text = "**Userbot succesfully Restarted**"
        try:
            app.send_message(sys.argv[1], text)
        except Exception as f:
            app.send_message("me", f"Got error: {f}\n\n" + text)
            pass
    app.join_chat("foxteam0")
    app.stop()

# start
plugins = dict(root="plugins")
Client = Client("my_account", api_id=api_id, api_hash=api_hash, plugins=plugins).run()
