import asyncio
from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("tagall", prefixes=prefix) & filters.me)
async def tagall(client, message):
    try:
        delay = message.command[1]
    except:
        delay = 0

    if len(message.text.split()) >= 2:
        text = f'{message.text.split(prefix + "tagall " + delay, maxsplit=1)[1]}'
    else:
        text = ""

    await message.delete()
    icm = []
    chat_id = message.chat.id

    gg = client.get_chat_members(chat_id)
    async for member in gg:
        icm.append(member)

    useres = len(icm)
    limit = 0
    i = useres // 10
    g = useres % 10
    l = 0
    string = ""

    for member in icm:
        if int(l) == int(i):
            if int(limit) == (g - 1):
                await client.send_message(chat_id, text=(f"{text}\n||{string}||"), disable_web_page_preview=True)
                string = ""
                limit = 0
            else:
                string += f"{member.user.mention('*')} "
                limit += 1

        else:
            if limit < 10:
                string += f"{member.user.mention('*')} "
                limit += 1
            else:
                await client.send_message(chat_id, text=(f"{text}\n||{string}||"), disable_web_page_preview=True)
                string = ""
                limit = 0
                l += 1

        try:
            delay = int(delay)
        except ValueError:
            delay = float(delay)
        await asyncio.sleep(delay)


module_list['Tagall'] = f'{prefix}tagall [delay] [text]'
file_list['Tagall'] = 'tagall.py'
