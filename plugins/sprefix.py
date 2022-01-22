from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.settings.main_settings import module_list, file_list
import configparser
import os
import sys

from prefix import my_prefix
prefix = my_prefix()

config_path = os.path.join(sys.path[0], "config.ini")
config = configparser.ConfigParser()
config.read(config_path)

@Client.on_message(filters.command("sp", prefixes=prefix) & filters.me)
async def sprefix(client: Client, message: Message):
    if len(message.command) > 1:
        prefix = message.command[1]
        config.set("prefix", "prefix", prefix)
        with open(config_path, "w") as config_file:
            config.write(config_file)
        await message.edit(
            f"<b>✅ | Префикс [ <code>{prefix}</code> ] установлен!</b>\n⏳ | Пожалуйста, дождитесь окончания перезагрузки"
        )
    else:
        await message.edit("<b>⚠️ | Префикс не может быть пустым!</b>")

module_list['Sprefix'] = f'{prefix}sp'
file_list['Sprefix'] = 'sprefix.py'