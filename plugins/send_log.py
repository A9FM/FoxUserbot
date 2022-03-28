from pyrogram import Client, filters
from plugins.settings.main_settings import module_list

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command('send_log', prefixes=prefix) & filters.me)
async def send_log(client, message):
	await message.delete()
	await client.send_document(message.chat.id, "temp/fox_userbot.log")


module_list['SendLog'] = f'{prefix}send_log'
