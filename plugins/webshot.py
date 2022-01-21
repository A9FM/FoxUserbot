from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command("webshot", prefixes=prefix) & filters.me)
async def webshot(client: Client, message: Message):
    try:
        user_link = message.command[1]
        await message.delete()
        try:
            full_link = f"https://mini.s-shot.ru/1920x1080/JPEG/1024/Z100/?{user_link}"
            await client.send_photo(message.chat.id, full_link, caption=f"**Screenshot of the page ⟶** {user_link}")
        except:
            full_link = f"https://webshot.deam.io/{user_link}/?width=1920&height=1080?delay=2000?type=png"
            await client.send_photo(message.chat.id, full_link, caption=f"**Screenshot of the page ⟶** {user_link}")
    except:
        await message.delete()
        await client.send_message(
            message.chat.id, "**Something went wrong...**"
        )
        
module_list['Webshot'] = f'{prefix}webshot [link]'
file_list['Webshot'] = 'webshot.py'
