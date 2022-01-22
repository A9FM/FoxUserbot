import os
from colorama import Fore
import time
import configparser

os.system("pip3 install -U colorama")

requirements = ["pyrogram", "requests", "wget", "telegraph"]
for rq in requirements:
    os.system(f"pip3 install -U {rq}")
    
os.system("cls" if os.name == "nt" else "clear")


def createConfig(path):
    print(Fore.GREEN + "Добро пожаловать в установщик FoxUserBot.")
    print(Fore.GREEN + "Сейчас вам предложат ввести номер телефона и код входа от вашего аккаунта в Telegram, сделайте это для установки FoxUserBot.\nПри последующем запуске, пишите в терминал python3 main.py")
    try:
        os.system("python3 main.py")
    except:
        os.system("python main.py")

if __name__ == "__main__":
    path = "config.ini"
    createConfig(path)

