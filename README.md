<p align="center">
        <img src="https://github.com/FoxUserbot/FoxUserbot/raw/main/logo.jpg" width="500" alt="FoxUserbot">
    </a>
    <br>
    <b>FoxUserbot</b>
    <br>
    <b>Telegram userbot with the easiest installation</b>
    <br>
    <a href='https://github.com/FoxUserbot/Modules'>
        Custom modules
    </a>
    <br>
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge" alt="Code style">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/FoxUserbot/FoxUserbot?style=for-the-badge">
    <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/FoxUserbot/FoxUserbot?style=for-the-badge">
</p>



<h1>Custom modules</h1>

<p>To add your module to the bot, create a pull request in the <a href='https://github.com/Dragon-Userbot/custom_modules/'>custom_modules</a> repository</p>

```python3
from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command("example_edit", prefixes=prefix) & filters.me)
async def example_edit(client: Client, message: Message):
    await message.edit("<code>This is an example module</code>")


module_list['Example'] = f'{prefix}example_edit'
file_list['Example'] = 'example.py'
```
