from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.settings.main_settings import module_list, file_list
from pathlib import Path

from prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.text & filters.incoming & filters.regex("^\-$") & filters.reply)
async def repDown(client: Client, message: Message):
    try:
        if message.reply_to_message.from_user.is_self:
            if Path(f"temp/reputation").is_file():
                with open("temp/reputation", "r+") as f:
                    NowReputation = int(f.read())
                    f.close()
            else:
                NowReputation = 0
            with open("temp/reputation", "w+") as f:
                reputation = str(NowReputation - 1)
                f.write(reputation)
                f.close()
            await message.reply_text(f"❎ Reputation lowered (-1)\n🌐 Your reputation: {str(reputation)}")
    except:
        pass


@Client.on_message(filters.text & filters.incoming & filters.regex("^\+$") & filters.reply)
async def repUp(client: Client, message: Message):
    try:
        if message.reply_to_message.from_user.is_self:
            if Path(f"temp/reputation").is_file():
                with open("temp/reputation", "r+") as f:
                    NowReputation = int(f.read())
                    f.close()
            else:
                NowReputation = 0
            with open("temp/reputation", "w+") as f:
                reputation = str(NowReputation + 1)
                f.write(reputation)
                f.close()
            await message.reply_text(f"✅ Reputation increased (+1)\n🌐 Your reputation: {str(reputation)}")
    except:
        pass

module_list['Reputation'] = 'reply "+" or "-" from another user'
file_list['Reputation'] = 'reputation.py'
