import asyncio
import datetime
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from plugins.settings.main_settings import module_list, file_list
from plugins.restarter import restart_get

from prefix import my_prefix
prefix = my_prefix()


async def afk_handler(client, message):
    try:
        global start, end
        end = datetime.datetime.now().replace(microsecond=0)
        afk_time = end - start

        if message.from_user.is_bot is False:
            await message.reply_text(
                f"❕ This user AFK.\n" f"<b>💬 Reason:</b> {reason}.\n" f"<b>⏳ Duration:</b> {afk_time}")
    except NameError:
        pass


@Client.on_message(filters.command("afk", prefixes=prefix) & filters.me)
async def afk(client, message):
    try:
        global start, end, handler, reason
        start = datetime.datetime.now().replace(microsecond=0)
        handler = client.add_handler(
            MessageHandler(afk_handler,
                           (filters.private & ~filters.me | filters.group & filters.mentioned & ~filters.me)))
        if len(message.text.split()) >= 2:
            reason = message.text.split(" ", maxsplit=1)[1]
        else:
            reason = "Unknown"
        await message.edit(f"❕ You are going to <b>AFK</b>.\n<b>💬 Reason:</b> {reason}.\n")
    except Exception as f:
        await message.edit(f"error {f}")


# No AFK
@Client.on_message(filters.command("unafk", prefixes=prefix) & filters.me)
async def unafk(client, message):
    try:
        global start, end
        end = datetime.datetime.now().replace(microsecond=0)
        afk_time = end - start
        await message.edit(
            f"❕ This user no longer <b>AFK.</b>\n⏳ Duration <b>AFK:</b> {afk_time}"
        )
        await asyncio.sleep(5)
        await restart_get(client, message)
    except Exception as error:
        await message.edit(f"<b>Error. You don't be AFK</b>\n`{error}`")
        await asyncio.sleep(3)
        await message.delete()


module_list['AFK'] = f'{prefix}afk | {prefix}unafk'
file_list['AFK'] = 'afk.py'
