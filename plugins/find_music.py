from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
import asyncio
import time

from prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command("m", prefix) & filters.me)
async def send_music(client, message):
    await message.edit("Search...")
    song_name = ""
    if len(message.command) > 1:
        song_name = " ".join(message.command[1:])
    elif message.reply_to_message and len(message.command) == 1:
        song_name = (
                message.reply_to_message.text or message.reply_to_message.caption
        )
    elif not message.reply_to_message and len(message.command) == 1:
        await message.edit("Enter the name of the music")
        await asyncio.sleep(2)
        await message.delete()
        return

    song_results = await client.get_inline_bot_results("deezermusicbot", song_name)

    try:
        # send to Saved Messages because hide_via doesn't work sometimes
        saved = await client.send_inline_bot_result(
            chat_id="me",
            query_id=song_results.query_id,
            result_id=song_results.results[0].id,
            hide_via=True,
        )

        # forward as a new message from Saved Messages
        saved = await client.get_messages("me", int(saved.updates[1].message.id))
        reply_to = (
            message.reply_to_message.message_id
            if message.reply_to_message
            else None
        )
        await client.send_audio(
            chat_id=message.chat.id,
            audio=str(saved.audio.file_id),
            reply_to_message_id=reply_to,
        )

        # delete the message from Saved Messages
        await client.delete_messages("me", saved.message_id)
    except TimeoutError:
        await message.edit("That didn't work out")
        await asyncio.sleep(2)
    await message.delete()


module_list['FindMusic'] = f'{prefix}m [Title of music]'
file_list['FindMusic'] = 'find_music.py'
