#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, Tk
from bs4 import BeautifulSoup
import multiprocessing as mp
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

class Dialog:
	def __init__(self):
		self.root = Tk()
		self.root.title("Updating")
		self.root.resizable(False, False)
		self.DX, self.DY = 400, 400
		self.root.geometry(f"{self.DX}x{self.DY}")
		self.dots_number = 0
		self.canvas = tk.Canvas(self.root, width=self.DX, height=self.DY, bg='#10141C', highlightthickness=0)
		self.canvas.pack(anchor=tk.CENTER, expand=True)
	
	def start(self):
		self.create_canvas()
		self.root.mainloop()

	def refresh_canvas(self):
		self.canvas.delete("all")
		self.create_canvas()

	def create_canvas(self):
		max_len = 3
		self.MESSAGE = f"Checking for updates{'.' * self.dots_number}{' ' * (max_len - self.dots_number)}"
		self.dots_number += 1
		self.canvas.create_text((200, 200), text=self.MESSAGE, fill="orange", font='Arial 19')
		if self.dots_number > max_len:
			self.dots_number = 0
		self.root.after(500, self.refresh_canvas)

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

def update_discord(download_link, tar_file_name):
	dialog = Dialog()
	installer = mp.Process(target=install_discord_tar, args=(download_link, tar_file_name,))
	dialog_box = mp.Process(target=dialog.start)
	installer.start()
	dialog_box.start()
	installer.join()
	while True:
		if not(installer.is_alive()):
			dialog_box.kill()
			break

download_link, tar_file_name, discord_version = get_download_info()
has_update = check_for_update(discord_version)
if has_update:	
	update_discord(download_link, tar_file_name)
cmd = f"{DISCORD_BINARY}&>/dev/null"
os.system(cmd)
#os.system(DISCORD_BINARY)
sys.exit()