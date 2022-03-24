import logging
import os


def log():
    if not os.path.exists("temp"):
        os.mkdir("temp")
    logging.basicConfig(
        filename="temp/fox_userbot.log",
        filemode="w",
        format="%(asctime)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
        level=logging.INFO
    )
