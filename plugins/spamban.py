from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
import asyncio

from prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command("spamban", prefix) & filters.me)
async def spamban(client, message):
    await message.edit("Checking your account for Spamban...")
    await client.unblock_user("spambot")
    await client.send_message("spambot", "/start")
    await asyncio.sleep(1)
    iii = await client.get_history("spambot")
    await message.delete()
    await client.forward_messages(message.chat.id, "spamBot", iii[0].message_id)

module_list['SpamBan'] = f'{prefix}spamban'
file_list['SpamBan'] = 'spamban.py'
