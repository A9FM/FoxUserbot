apt update -y
apt install python3 -y
apt install python3-pip -y
apt install git -y
apt install wget -y
pip3 install -U pyrogram
wget https://github.com/FoxUserbot/FoxUserbot/archive/refs/heads/main.zip
unzip main.zip
rm main.zip
cd FoxUserbot-main
python3 install.py
