import os
from pystyle import  Write, Colors
from plugins.settings.main_settings import version

from prefix import my_prefix
prefix = my_prefix()

os.system("cls" if os.name == "nt" else "clear")

Write.Print(f"""
╔═╗┌─┐─┐ ┬           
╠╣ │ │┌┴┬┘           
╚  └─┘┴ └─           
╦ ╦┌─┐┌─┐┬─┐┌┐ ┌─┐┌┬┐
║ ║└─┐├┤ ├┬┘├┴┐│ │ │ 
╚═╝└─┘└─┘┴└─└─┘└─┘ ┴ 
Channel: @foxteam0
Version: {version}
Prefix: {prefix}

Client Started
Type {prefix}ping to check Userbot works
""", Colors.red_to_yellow, interval=0.0)
