import os
from modules.plugins_1system.settings.main_settings import version
from prefix import my_prefix

from pystyle import  Write, Colors
os.system("cls" if os.name == "nt" else "clear")

Write.Print(f"""
╔═╗┌─┐─┐ ┬           
╠╣ │ │┌┴┬┘           
╚  └─┘┴ └─           
╦ ╦┌─┐┌─┐┬─┐┌┐ ┌─┐┌┬┐
║ ║└─┐├┤ ├┬┘├┴┐│ │ │ 
╚═╝└─┘└─┘┴└─└─┘└─┘ ┴ 
Github: https://github.com/FoxUserbot/FoxUserbot
Version: {version}
Prefix: {my_prefix()}

Client Started
Type {my_prefix()}ping to check Userbot works
""", Colors.red_to_yellow, interval=0.0)
