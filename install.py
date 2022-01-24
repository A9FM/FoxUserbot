import os
import time
import pip

pip.main(["install", "telegraph", "pyrogram", "requests", "wget", "colorama", "--upgrade"])
    
os.system("cls" if os.name == "nt" else "clear")

print("FoxUserBot installed.\nStart FoxUserbot... (if you get error, writte 'python3 main.py' in the terminal)")
try:
    os.system("python3 main.py")
except:
    os.system("python main.py")
