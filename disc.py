#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import tarfile
import shutil
import json
import sys
import os

API_URL         = "https://discord.com/api/download?platform=linux&format=tar.gz"
DISCORD_PATH    = os.path.join(os.path.expanduser("~"), ".local/share/Discord")
BUILD_INFO_PATH = DISCORD_PATH + "/resources/build_info.json"
DISCORD_BINARY  = DISCORD_PATH + "/Discord"
PATCH_SOURCE    = sys.argv[0]

def get_download_info():
	redirect_url    = requests.get(API_URL, allow_redirects=False).text
	redirect_html   = BeautifulSoup(redirect_url, features="lxml")
	download_link   = redirect_html.find('a', href=True).contents[0]
	tar_file_name   = download_link.split("/")[-1]
	discord_version = tar_file_name.replace("discord-", "")[:-7]
	return download_link, tar_file_name, discord_version

def install_discord_tar(download_link, tar_file_name):	
	tar_file = requests.get(download_link).content
	with open(tar_file_name, "wb") as archive:
		archive.write(tar_file)
	with tarfile.open(tar_file_name) as ex_archive:
		ex_archive.extractall(DISCORD_PATH[:-7])

def check_for_update(latest_version):
	with open(BUILD_INFO_PATH) as build_info:
		installed_version = json.load(build_info)['version']
	if not(latest_version == installed_version):
		return True
	else:
		return False

download_link, tar_file_name, discord_version = get_download_info()
has_update = check_for_update(discord_version)
if has_update:	
	install_discord_tar(download_link, tar_file_name)
os.system(DISCORD_BINARY)
