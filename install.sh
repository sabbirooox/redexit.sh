#!/bin/bash
clear
echo -e "\e[1;32m[+] Installing Requirements...\e[0m"
pkg update -y && pkg upgrade -y
pkg install python -y
pip install colorama pillow

echo -e "\e[1;32m[+] Downloading RED EXIT Tool...\e[0m"
curl -sL https://raw.githubusercontent.com/sabbiroox/redexit.sh/main/red_exif.py -o red_exif.py

chmod +x red_exif.py

echo -e "\e[1;34m[✓] Installation Complete!\e[0m"
echo -e "\e[1;33mType 'python red_exif.py' to run the tool.\e[0m"
