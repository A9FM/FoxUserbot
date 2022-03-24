from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()


the_regex = r"^r\/([^\s\/])+"
i = filters.user([])


@Client.on_message(i)
async def ignored(client, message):
    await message.delete()


@Client.on_message(filters.command("ignore", prefixes=prefix) & filters.me)
async def add_ignore(client, message):
    try:
        try:
            users = message.command[1]
        except:
            users = message.reply_to_message.from_user.id

        try:
            users = int(users)
            users = str(users)
        except:
            useres = Client.get_users(users)
            users = useres.id

        if users in i:
            i.remove(int(users))
            await message.edit(f"Ignor {str(users)} deactivated")
        else:
            i.add(int(users))
            await message.edit(f"Ignor {str(users)} activated")
    except Exception as h:
        print(h)


module_list['IgnoreUser'] = f'{prefix}ignore [ID/Username]'
file_list['IgnoreUser'] = 'ignore.py'
