<p align="center">
    <img src="https://github.com/FoxUserbot/FoxUserbot/raw/main/logo.png" width="500" alt="FoxUserbot">
    </a>
    <br>
    <b>FoxUserbot</b>
    <br>
    <b>Telegram userbot with the easiest installation</b>
    <br>
    <a href='https://github.com/FoxUserbot/Modules'>
        Custom modules
    </a>
<br><br>
<a href="https://github.com/FoxUserbot/FoxUserbot/commits/main">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/FoxUserbot/FoxUserbot?style=for-the-badge">
</a>

<a href="https://github.com/FoxUserbot/FoxUserbot/issues">        
    <img alt="GitHub Issues" src="https://img.shields.io/github/issues/FoxUserbot/FoxUserbot?style=for-the-badge">
</a>

<a href="https://github.com/FoxUserbot/FoxUserbot">    
    <img alt="GitHub Repo Stars" src="https://img.shields.io/github/stars/FoxUserbot/FoxUserbot?style=for-the-badge">
    <img alt="GitHub Repo Size" src="https://img.shields.io/github/repo-size/FoxUserbot/FoxUserbot?style=for-the-badge">
    <img alt="GitHub CodeFactor" src="https://www.codefactor.io/repository/github/FoxUserbot/FoxUserbot/badge?style=for-the-badge">
</a>



</p>



<h1>Custom modules</h1>

<p>To add your module to the bot, create a pull request in the <a href='https://github.com/FoxUserbot/Modules/'>custom_modules</a> repository</p>

```python3
from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("example_edit", prefixes=prefix) & filters.me)
async def example_edit(client, message):
    await message.edit("<code>This is an example module</code>")


module_list['Example'] = f'{prefix}example_edit'
file_list['Example'] = 'example.py'
```

<h1>Install and Start</h1>
<h2>Termux / Linux (deb)</h2>
<h3>Install</h3>

curl
```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/FoxUserbot/FoxUserbot/main/install.sh)"
```


wget
```
sh -c "$(wget https://raw.githubusercontent.com/FoxUserbot/FoxUserbot/main/install.sh -O -)"
```

<h3>How to start</h3>

```
cd FoxUserbot && python3 main.py
```

<h2>Windows</h2>
<h3>Install</h3>
Install <a href="https://www.python.org/downloads/">python3</a>

Download and Unzip <a href="https://github.com/FoxUserbot/FoxUserbot/archive/refs/heads/main.zip">This file (!don't rename the directory!)</a>

Open install.py

<h3>How to start</h3>
Open windows.bat

<h1>Groups and support</h1>
<a href="https://t.me/foxteam0">
<img alt="Telegram" src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram">
</a>

<h1>Credits</h1>
➤ Gh0stC0der1 <a href="https://github.com/gh0stc0der1">Github</a><br>
➤ Terexdev <a href="https://github.com/terexdev">Github</a> | <a href="https://t.me/Klarlex">Telegram</a> <br>
➤ A9FM <a href="https://github.com/A9FM">Github</a> | <a href="https://github.com/a9_fm">Telegram</a> <br>
