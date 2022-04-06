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
<a href="https://github.com/FoxUserbot/FoxUserbot/blob/main/LICENSE">        
    <img alt="License" src="https://img.shields.io/github/license/FoxUserbot/FoxUserbot?style=for-the-badge">
</a>

<a href="https://github.com/FoxUserbot/FoxUserbot/commits/main">
    <img alt="last-commit" src="https://img.shields.io/github/last-commit/FoxUserbot/FoxUserbot?style=for-the-badge">
</a>

<a href="https://github.com/FoxUserbot/FoxUserbot/issues">        
    <img alt="Issues" src="https://img.shields.io/github/issues/FoxUserbot/FoxUserbot?style=for-the-badge">
</a>

<a href="https://github.com/FoxUserbot/FoxUserbot">
    <img alt="CodeFactor" src="https://www.codefactor.io/repository/github/FoxUserbot/FoxUserbot/badge?style=for-the-badge">
    <img alt="Stars" src="https://img.shields.io/github/stars/FoxUserbot/FoxUserbot?style=for-the-badge">
    <img alt="Size" src="https://img.shields.io/github/repo-size/FoxUserbot/FoxUserbot?style=for-the-badge">
    <img alt="Language" src="https://img.shields.io/github/languages/top/FoxUserbot/FoxUserbot?style=for-the-badge">
    <img alt="Python" src="https://img.shields.io/badge/python-%3E%203.6-blue?style=for-the-badge">
</a>



</p>



<h1>Custom modules</h1>

<p>To add your module to the bot, create a pull request in the <a href='https://github.com/FoxUserbot/Modules/'>custom_modules</a> repository</p>

```
python3
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
<h2>How to install?</h3>


- Termux

```
pkg update -y && pkg install python3 wget -y && wget -O foxub.$$ https://github.com/FoxUserbot/FoxUserbot/archive/refs/heads/main.zip && (unzip foxub.$$ && rm -rf foxub.$$ && cd FoxUserbot-main && python3 install.py)
```

- APT (Debian based)


```
apt update -y && apt install python3 python3-pip wget -y && wget -O foxub.$$ https://github.com/FoxUserbot/FoxUserbot/archive/refs/heads/main.zip && (unzip foxub.$$ && rm -rf foxub.$$ && cd FoxUserbot-main && python3 install.py)
```

- Astra Linux (if python < 3.7, else go to "Debian based")

```
apt update -y && apt install curl wget -y && sh <(curl -sSL https://gist.githubusercontent.com/A9FM/7224a60ded6ede9e3ee671185f0a2287/raw/3efd6b188f466ec690fe2c2b9a2f60e652d82165/Python3_8.sh) && wget -O foxub.$$ https://github.com/FoxUserbot/FoxUserbot/archive/refs/heads/main.zip && (unzip foxub.$$ && rm -rf foxub.$$ && cd FoxUserbot-main && python3 install.py)
```

- YUM (RHEL based)

```
yum -y update && yum install wget python3 curl -y && python3 <(curl -sSL https://bootstrap.pypa.io/get-pip.py) && wget -O foxub.$$ https://github.com/FoxUserbot/FoxUserbot/archive/refs/heads/main.zip && (unzip foxub.$$ && rm -rf foxub.$$ && cd FoxUserbot-main && python3 install.py)
```

- PACMAN (Arch based)

```
pacman -S python3 wget curl && python3 <(curl -sSL https://bootstrap.pypa.io/get-pip.py) && wget -O foxub.$$ https://github.com/FoxUserbot/FoxUserbot/archive/refs/heads/main.zip && (unzip foxub.$$ && rm -rf foxub.$$ && cd FoxUserbot-main && python3 install.py)
```

- MacOS

```
xcode-select --install ; /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)" && brew install python3 && pip3 install --upgrade pip && pip3 install wheel && brew install wget && wget -O foxub.$$ https://github.com/FoxUserbot/FoxUserbot/archive/refs/heads/main.zip && (unzip foxub.$$ && rm foxub.$$ && cd FoxUserbot-main && python3 install.py)
```


<h4>How to start?</h3>

```
cd FoxUserbot-main && python3 main.py
```

<h3>Windows</h2>
<h4>Install</h3>

- Install <a href="https://www.python.org/downloads/">python3</a>

- Download and Unzip <a href="https://github.com/FoxUserbot/FoxUserbot/archive/refs/heads/main.zip">This file (!don't rename the directory!)</a>

- Open install.py

<h4>How to start</h3>

- Open windows.bat

<h1>Groups and support</h1>
<a href="https://t.me/foxteam0">
<img alt="Telegram" src="https://img.shields.io/badge/Telegram_Channel-0a0a0a?style=for-the-badge&logo=telegram">
</a>

<a href="https://t.me/foxteamdiscuss">
<img alt="Telegram group" src="https://img.shields.io/badge/Telegram_Group-0a0a0a?style=for-the-badge&logo=telegram">
</a>
    
<h1>Credits</h1>
➤ A9FM <a href="https://github.com/A9FM">Github</a> | <a href="https://github.com/a9_fm">Telegram</a> <br>
