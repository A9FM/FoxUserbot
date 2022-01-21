import os
from colorama import Fore
import time
import configparser

requirements = ["pyrogram", "requests", "wget", 'telegraph', "colorama"]
for rq in requirements:
    os.system(f"pip3 install -U {rq}")
    
os.system("cls" if os.name == "nt" else "clear")


def createConfig(path):
    print(Fore.GREEN + "Привет. Добро пожаловать в установщик FoxUserBot.")
    time.sleep(1)
    print(Fore.GREEN + "Для продолжения вам потребуються данные такие как api-id, и api-hash. Их можно найти на сайте my.telegram.org")
    api_id = input(Fore.GREEN + "Введите ваш api-id >>> ")
    api_hash = input(Fore.GREEN + "Введите api hash >>> ")

    config = configparser.ConfigParser()
    config.add_section("pyrogram")
    config.set("pyrogram", "api_id", api_id)
    config.set("pyrogram", "api_hash", api_hash)
    config.set("pyrogram", "device_model", "FoxUserbot")
    with open(path, "w") as config_file:
        config.write(config_file)

    print(Fore.GREEN + "Спасибо. Данные сохранены. Сейчас вам предложат ввести номер телефона и код входа от вашего аккаунта в Telegram, сделайте это для установки FoxUserBot.")
    os.system("python3 main.py")
 
if __name__ == "__main__":
    path = "config.ini"
    createConfig(path)

