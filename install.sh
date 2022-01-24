apt update -y
apt install python3 python3-pip wget -y
pip3 install -U pyrogram

wget -O foxub.$$ https://github.com/FoxUserbot/FoxUserbot/archive/refs/heads/main.zip && (unzip foxub.$$ && rm foxub.$$ && cd FoxUserbot-main)
python3 install.py
