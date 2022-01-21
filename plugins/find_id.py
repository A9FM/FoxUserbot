from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.settings.main_settings import module_list, file_list
import asyncio

from prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command('find_id', prefixes=prefix) & filters.me)
async def find_id(client: Client, message: Message):
  await message.edit(f'**ID of this chat: ** ```{message.chat.id}```')
  
module_list['FindIDThisChat'] = f'{prefix}fing_id'
file_list['FindIDThisChat'] = 'find_id.py'
