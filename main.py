import logging
import os
import sys
import configparser
import prefix
from pyrogram import Client

logging.basicConfig(filename="temp/fox_userbot.log", filemode='w', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

# restart
app = Client("my_account")
with app:
    if len(sys.argv) == 4:
        try:
            restart_type = sys.argv[3]
            if restart_type == "1":
                text = "<code>Update process completed!</code>"
            else:
                text = "**Userbot succesfully Restarted**"
            app.send_message(sys.argv[1], text)
        except:
            app.send_message(self, text)
    # app.join_chat("foxteam0")
    app.stop()

# start
plugins = dict(root="plugins")
Client = Client("my_account", plugins=plugins).run()