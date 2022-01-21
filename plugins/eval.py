from pyrogram import Client, filters
from pyrogram.types import Message
import sys
from io import StringIO
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command(["eval"], prefix) & filters.me)
def user_exec(client: Client, message: Message):
    reply = message.reply_to_message
    code = ""
    try:
        code = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        try:
            code = message.text.split(" \n", maxsplit=1)[1]
        except IndexError:
            pass

    result = sys.stdout = StringIO()
    try:
        exec(code)

        message.edit(
            f"<b>Code:</b>\n"
            f"<code>{code}</code>\n\n"
            f"<b>Result</b>:\n"
            f"<code>{result.getvalue()}</code>"
        )
    except:
        message.edit(
            f"<b>Code:</b>\n"
            f"<code>{code}</code>\n\n"
            f"<b>Result</b>:\n"
            f"<code>{sys.exc_info()[0].__name__}: {sys.exc_info()[1]}</code>"
        )


module_list['Eval'] = f'{prefix}eval'
file_list['Eval'] = 'eval.py'