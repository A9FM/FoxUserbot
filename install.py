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
    print(Fore.GREEN + "FoxUserBot installed.")
    print(Fore.GREEN + "Start FoxUserbot... (if you get error, writte 'python3 main.py' in the terminal)")
    try:
        os.system("python3 main.py")
    except:
        os.system("python main.py")

if __name__ == "__main__":
    path = "config.ini"
    createConfig(path)

