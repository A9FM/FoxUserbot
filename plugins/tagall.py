import asyncio
from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("tagall", prefixes=prefix) & filters.me)
async def tagall(client, message):
    delay = message.command[1]
    string = ""
    if len(message.text.split()) >= 2:
        string += f'{message.text.split(prefix + "tagall " + delay, maxsplit=1)[1]}\n'
    await message.delete()
    chat_id = message.chat.id
    limit = 1
    icm = client.iter_chat_members(chat_id)
    async for member in icm:
        if limit <= 7:
            string += f"{member.user.mention}\n"
            limit += 1
        else:
            await client.send_message(chat_id, text=string, disable_web_page_preview=True)
            limit = 1
            string = ""
            try:
                delay = int(delay)
            except ValueError:
                delay = float(delay)
            await asyncio.sleep(delay)


module_list['Tagall'] = f'{prefix}tagall [delay] [text]'
file_list['Tagall'] = 'tagall.py'
