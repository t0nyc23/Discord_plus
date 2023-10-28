#!/bin/bash
#Installing Requirements.
sudo apt install python3-{requests,tk,bs4,tarfile,json}

Check_Discord () {
#Wanna do it yourself or we can do it for ya?	
	app_name="discord"
	dpkg -l | grep $app_name &>/dev/null
	if [ $? -eq 0 ]; then
	    echo "found deb"
	    sudo apt-get remove $app_name
	else
	    snap list | grep $app_name &> /dev/null
	    if [ $? -eq 0 ]; then
	        echo "found snap"
	        sudo snap remove $app_name
	    fi
	fi
}
#Checking Discorc is Installed
Check_Discord       
#Creatig synlink.          
sudo ln -sf $(pwd)/discord.py /usr/local/bin/discord
#Creating .Desktop File.
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


