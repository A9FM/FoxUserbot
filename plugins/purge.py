from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("del", prefixes=prefix) & filters.me)
async def delete_messages(client, message):
    if message.reply_to_message:
        message_id = message.reply_to_message.id
        await client.delete_messages(message.chat.id, message_id)
    await message.delete()


@Client.on_message(filters.command("purge", prefixes=prefix) & filters.me)
async def purge(client, message):
    try:
        if message.reply_to_message:
            r = message.reply_to_message.id
            m = message.id
            msgs = []
            await message.delete()
            while r != m:
                msgs.append(int(r))
                r += 1
            await client.delete_messages(message.chat.id, msgs)
            r = message.reply_to_message.id
            msgs = []
            while r != m:
                msgs.append(int(r))
                r += 1
            await client.delete_messages(message.chat.id, msgs)
            await client.send_message(message.chat.id, f"<b>Messages deleted!</b>")
        else:
            await message.edit("<i>I don't see reply</i>")
    except:
        await message.edit("<i>Don't have permision.</i>")

module_list['Purge'] = f'{prefix}del [reply] | {prefix}purge [reply]'
file_list['Purge'] = 'purge.py'
