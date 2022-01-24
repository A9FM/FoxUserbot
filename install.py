import os
import pip

pip.main(["install", "telegraph", "pyrogram", "requests", "wget", "colorama", "--upgrade"])
print("\n\nFoxUserBot installed.\nStart FoxUserbot... (if you get error, writte 'python3 main.py' in the terminal)")
os.system("python3 main.py" if os.name == "nt" else "python main.py")
