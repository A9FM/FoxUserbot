from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command('kickall', prefix) & filters.me)
async def kickall(client: Client, message: Message):
    await message.edit("kick all chat members!")
    member = client.iter_chat_members(message.chat.id)
    async for all in member:
        try:
            await client.ban_chat_member(message.chat.id, all.user.id, 0)
        except:
            pass


@Client.on_message(filters.command('kickall hide', prefix) & filters.me)
async def kickall(client: Client, message: Message):
    await message.delete()
    member = client.iter_chat_members(message.chat.id)
    async for all in member:
        try:
            await client.ban_chat_member(message.chat.id, all.user.id, 0)
        except:
            pass


module_list['KickallSubs'] = f'{prefix}kickall [Hide/No]'
file_list['KickallSubs'] = 'kickall.py'