from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
import asyncio

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("q", prefixes=prefix) & filters.me)
async def quotly(client, message):
    idstick = 0
    if not message.reply_to_message:
        await message.edit("Reply to message")
        return

    await client.unblock_user("QuotLyBot")
    await message.edit("Create quotes... wait...")
    await message.reply_to_message.forward("QuotLyBot")

    is_sticker = False

    while not is_sticker:
        try:
            msg = await client.get_history("@QuotLyBot", limit=1)
            idstick = msg[0].sticker.file_id
            is_sticker = True
        except:
            await asyncio.sleep(1)

    await asyncio.gather(
        message.delete(),
        client.send_sticker(message.chat.id, idstick)
    )


module_list['Quotes'] = f'{prefix}q [reply]'
file_list['Quotes'] = 'quotes.py'
