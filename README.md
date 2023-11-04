# Discord plus

Discord on linux does not update its self, we do.

## About the problem

**Note:** We are not referring to snap or flatpak versions of the app since they are not officially supported by Discord.

When updates are available, Discord on Linux will not apply them automatically.\
Instead it will pop up a message box informing you for the update, and give you two options:
 - Install/update from a **.tar.gz** file
 - Install/update from a **.deb** file

This means that each time there is an update, the user must manually download and install the newer version of Discord

## About Discord_plus

Discord_plus is, essentiatlly, a python script that runs before the main Discord binary does.\
Specifically it will:
  - Check for a newer Discord version on the official website.
  - If there is a newer version, it will download and install the latest one
  - And finally, it will launch the main Discord binary

If there's not a newer version, the script will just launch Discord normally.

Discord_plus has been tested on:
  - Ubuntu
  - Kali Linux
  - Fedora
  - *Other Debian based distribuitions should work fine.

## Installation

The following one-liner will install Discord_plus along with required packages, as well as create a symlink and a **.desktop** file.

**Note:** The ```install.sh``` script will try to uninstall existing Discord installations, if any, but **it is a good idea to uninstall Discord manually** just in case.

```
git clone https://github.com/n0ns0n/Discord_plus $HOME/.local/share/Discord_plus && \
cd $HOME/.local/share/Discord_plus && \
bash install.sh
```

If you don't want to use the one-liner, make sure to clone the repo inside .loca/share on your home directory. Also make sure to run the script using Bash.
