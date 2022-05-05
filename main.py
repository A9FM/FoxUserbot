# -*- coding: utf-8 -*-

# Check Library
print("AutoUpdate library python...\n")
from install import check
check()

import logging
logging.basicConfig(
    filename="temp/fox_userbot.log",
    filemode="w",
    format="%(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.INFO
)

# Start userbot
from start_UB import start_userbot
start_userbot()
