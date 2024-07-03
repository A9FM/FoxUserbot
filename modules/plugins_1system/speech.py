from pyrogram import Client, filters
from modules.plugins_1system.settings.main_settings import module_list, file_list
from prefix import my_prefix

from gtts import gTTS
import os


@Client.on_message(filters.command("voice", prefixes=my_prefix()) & filters.me)
async def voice(client, message):
    lang_code = os.environ.get("lang_code", "en")
    cust_lang = None
    await message.delete()
    text = message.text.split(None, 1)[1]
    tts = gTTS(text, lang=lang_code)
    tts.save("temp/voice.mp3")
    if message.reply_to_message:
        await client.send_voice(
            message.chat.id,
            voice="temp/voice.mp3",
            reply_to_message_id=message.reply_to_message.id,
        )
    else:
        await client.send_voice(message.chat.id, voice="temp/voice.mp3")
    os.remove("temp/voice.mp3")


@Client.on_message(filters.command("voice_ru", prefixes=my_prefix()) & filters.me)
async def ru_voice(client, message):
    lang_code = os.environ.get("lang_code", "ru")
    cust_lang = None
    await message.delete()
    text = message.text.split(None, 1)[1]
    tts = gTTS(text, lang=lang_code)
    tts.save("temp/voice.mp3")
    if message.reply_to_message:
        await client.send_voice(
            message.chat.id,
            voice="temp/voice.mp3",
            reply_to_message_id=message.reply_to_message.id,
        )
    else:
        await client.send_voice(message.chat.id, voice="temp/voice.mp3")
    os.remove("temp/voice.mp3")

module_list['TextToVoice'] = f'{my_prefix()}voice [Text] | {my_prefix()}voice_ru [Text]'
file_list['TextToVoice'] = 'speech.py'
