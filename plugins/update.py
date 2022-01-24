from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
import os
import wget
import zipfile

from prefix import my_prefix

prefix = my_prefix()


@Client.on_message(filters.command('update', prefixes=prefix) & filters.me)
async def update(client, message):
    try:
        await message.edit('**Updating...**')
        link = "https://github.com/FoxUserbot/FoxUserbot/archive/refs/heads/main.zip"
        wget.download(link, 'temp/archive.zip')
        with zipfile.ZipFile("temp/archive.zip", "r") as zip_ref:
            zip_ref.extractall("./..")
        os.remove("temp/archive.zip")

        await message.edit('**The userbot has been successfully updated**')
    except Exception as error:
        await message.edit(f"**An error occured...**\nLog: {error}")


module_list['Update'] = f'{prefix}update'
file_list['Update'] = 'update.py'
