from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
from plugins.restarter import restart
import os

from prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command('unloadmod', prefixes=prefix))
async def unloadmod(client, message):
        module_name = message.command[1]
        file = file_list[module_name]
        os.remove(f'plugins/{file}')
        del module_list[module_name]
        await message.edit(
            f"<b>✅ | Модуль выгружен!</b>\n⏳ | Пожалуйста, дождитесь окончания перезагрузки"
        )
        await restart(message, restart_type="restart")
        
module_list['Unloadmod'] = f'{prefix}unloadmod [module name]'