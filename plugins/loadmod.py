from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.settings.main_settings import module_list, file_list
from plugins.restarter import restart
import wget

from prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command('loadmod', prefixes=prefix) & filters.me)
async def loadmod(client: Client, message: Message):
    try:
        if not message.reply_to_message.document:
            await message.edit("<b>Load module...</b>")
            link = message.command[1]
            wget.download(link, 'plugins/')
        else:
            await client.download_media(message.reply_to_message.document, file_name='plugins/')
        await message.edit(
            f"**The module has been loaded successfully.**\nRestart..."
        )
        await restart(message, restart_type="restart")
    except:
        await message.edit("**An error has occurred**")

module_list['Loadmod'] = f'{prefix}loadmod [link to the module]'
