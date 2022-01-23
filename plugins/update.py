from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.settings.main_settings import module_list, file_list
import os
import wget
import zipfile

from prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command('update', prefixes=prefix) & filters.me)
async def update(client: Client, message: Message):
  try:
    await message.edit('**Updating...**')
    link = "https://github.com/FoxUserbot/FoxUserbot/archive/refs/heads/main.zip"
    wget.download(link, 'temp/archive.zip')
    with zipfile.ZipFile("temp/archive.zip", "r") as zip_ref:
      zip_ref.extractall("./..")
    os.remove("temp/archive.zip")

    await message.edit('**The userbot has been successfully updated**')
  except:
    await message.edit("**An error occured...**")
    
module_list['Update'] = f'{prefix}update'
file_list['Update'] = 'update.py'
