from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
from time import perf_counter

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command('ping', prefixes=prefix) & filters.me)
async def ping(client, message):
    start1 = perf_counter()
    await message.edit("test Ping..")
    end1 = perf_counter()

    start2 = perf_counter()
    await message.edit("test pIng..")
    end2 = perf_counter()

    start3 = perf_counter()
    await message.edit("test piNg...")
    end3 = perf_counter()

    start4 = perf_counter()
    await message.edit("test pinG...")
    end4 = perf_counter()

    pinges = ((end1 + end2 + end3 + end4) / 4) - ((start1 + start2 + start3 + start4) / 4)
    ping = pinges * 1000

    if 0 <= ping <= 199:
        connect = "🟢 Stable"
    if 199 <= ping <= 400:
        connect = "🟠 Good"
    if 400 <= ping <= 600:
        connect = "🔴 Not stable"
    if 600 <= ping:
        connect = "⚠ Check you network connection"
    await message.edit(f"<b>🏓 Pong\n📶</b> {round(ping)} ms\n{connect}")


module_list['Ping'] = f'{prefix}ping'
file_list['Ping'] = 'ping.py'
