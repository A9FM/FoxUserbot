import logging
import os
import sys
import configparser
import prefix
from pyrogram import Client

logging.basicConfig(filename="fox_userbot.log", filemode='w', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

plugins = dict(root="plugins")
Client("my_account", plugins=plugins).run()