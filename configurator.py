import os
import sys
import configparser

config_path = os.path.join(sys.path[0], "config.ini")
config = configparser.ConfigParser()
config.read(config_path)

config_id = "2860432"
config_hash = "2fde6ca0f8ae7bb58844457a239c7214"


def api():
    get_id = config.get("pyrogram", "api_id")
    get_hash = config.get("pyrogram", "api_hash")
    return get_id, get_hash


def my_api():
    try:
        api_id, api_hash = api()
    except configparser.NoSectionError:
        config.add_section("pyrogram")
        config.set("pyrogram", "api_id", config_id)
        config.set("pyrogram", "api_hash", config_hash)
        with open(config_path, "w") as config_file:
            config.write(config_file)
        api_id = config_id
        api_hash = config_hash
    return api_id, api_hash
