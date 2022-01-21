from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.settings.main_settings import module_list, file_list, settings
import wget

prefix = settings['prefix']

@Client.on_message(filters.command('loadmod', prefixes=prefix) & filters.me)
async def loadmod(client: Client, message: Message):
    try:
        link = message.command[1]
        wget.download(link, 'plugins/')
        await message.edit("**The module has been loaded successfully.**")
    except:
        await message.edit("**An error has occurred**")
    
module_list['Loadmod'] = f'{prefix}loadmod [link to the module]'
