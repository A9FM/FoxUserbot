from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.settings.main_settings import module_list, file_list
import wget
from prefix import my_prefix
from plugins.restarter import restart

prefix = my_prefix()

@Client.on_message(filters.command('loadmod', prefixes=prefix) & filters.me)
async def load_module(client: Client, message: Message):
    if not message.reply_to_message.document:
    	await message.edit("<b>Загрузка модуля...</b>")
    	link = message.command[1]
    	wget.download(link, 'plugins/')
    	await message.edit(
            f"<b>✅ | Модуль загружен!</b>\n⏳ | Пожалуйста, дождитесь окончания перезагрузки"
        )
    	await restart(message, restart_type="restart")
    else:
        await client.download_media(message.reply_to_message.document, file_name='plugins/')
        await message.edit(
            f"<b>✅ | Модуль загружен!</b>\n⏳ | Пожалуйста, дождитесь окончания перезагрузки"
        )
        await restart(message, restart_type="restart")
    
module_list['Loadmod'] = f'{prefix}loadmod [link to the module]'
