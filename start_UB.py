# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.CRITICAL)


def get_req():
    requirements = ["install", "telegraph", "pyrogram", "requests", "wget", "rich", "wikipedia", "--upgrade"]
    return requirements


def start_userbot():
    from pyrogram import Client
    from configurator import my_api
    from prestarter import prestart
    from check import check_structure
    check_structure()
    api_id, api_hash, device_mod = my_api()
    prestart()
    plugins = dict(root="plugins")
    Client = Client("my_account", api_id=api_id, api_hash=api_hash, device_model=device_mod, plugins=plugins).run()


if __name__ == "__main__":
    start_userbot()
