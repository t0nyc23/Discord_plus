# Discord plus

## About the problem

**Note:** We do not refer to the Snap or Flatpak versions of the app as they are not officially supported by Discord.

When updates become available, Discord on Linux will not apply them automatically.  
Instead, it will display a message box, informing you of the update and providing you with two options:
- Install/update from a **.tar.gz** file.
- Install/update from a **.deb** file.

This means that each time there is an update, users must manually download and install the newer version of Discord.

## About Discord_plus

**Discord_plus** is essentially a Python script that runs before the main Discord binary. It serves the following purposes:

- Check for a newer Discord version on the official website.
- If a newer version is available, it will download and install the latest one.
- Finally, it will launch the main Discord binary.

If there is no newer version, the script will launch Discord normally.

**Discord_plus** has been tested on the following Linux distributions:
- Ubuntu
- Kali Linux
- Fedora

*Other Debian-based distributions should work fine.

## Installation

The following one-liner will install Discord_plus along with the required packages and create a symlink and a **.desktop** file.

**Note:** The `install.sh` script will attempt to uninstall existing Discord installations, if any, but **it is a good idea to uninstall Discord manually** just in case.

```
git clone https://github.com/n0ns0n/Discord_plus $HOME/.local/share/Discord_plus && \
cd $HOME/.local/share/Discord_plus && \
bash install.sh
```

If you prefer not to use the one-liner, be sure to clone the repository inside .local/share in your home directory. Also, make sure to run the script using Bash.
