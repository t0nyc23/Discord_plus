#!/bin/bash
CRESET="\e[0m"
RED="\e[1;31m"
CYAN="\e[1;36m"
echo -e "${CYAN}[+] Installing python3 requirements${CRESET}"
sudo apt install python3-{requests,tk,bs4,tarfile,json}
Check_Discord () {
	#Wanna do it yourself or we can do it for ya?
	app_name="discord"
	dpkg -l | grep $app_name &>/dev/null
	if [ $? -eq 0 ]; then
        echo -e "\n\n${RED}[+] Discord is installed${CRESET}"
        echo -e "${RED}[+] Trying to uninstall first${CRESET}\n\n"
	    sudo apt-get remove $app_name
	else
	    snap list | grep $app_name &> /dev/null
	    if [ $? -eq 0 ]; then
	        echo -e "\n\n${RED}[+] Discord is installed as a snap${CRESET}"
	        echo -e "${RED}[+] Trying to uninstall first${CRESET}\n\n"
	        sudo snap remove $app_name
	    fi
	fi
}
echo -e "${CYAN}[+] Checking if Discord is installed${CRESET}"
Check_Discord       
echo -e "${CYAN}[+] Creating symlink to /usr/local/bin/discord${CRESET}"       
sudo ln -sf $(pwd)/discord.py /usr/local/bin/discord
echo -e "${CYAN}[+] Creating .desktop file${CRESET}"
desktop_file="[Desktop Entry]
Name=Discord
StartupWMClass=discord
Comment=All-in-one voice and text chat for gamers that's free, secure, and works on both your desktop and phone.
GenericName=Internet Messenger
Exec=/usr/local/bin/discord
Icon=$HOME/.local/share/Discord/discord.png
Type=Application
Categories=Network;InstantMessaging;"
echo "$desktop_file" | sudo tee /usr/share/applications/discord.desktop
