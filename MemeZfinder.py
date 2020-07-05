#!/usr/bin/python3
# -*- coding: utf-8 -*-
#MemeZfinder by RandomGuy90
import os
import platform


osType = platform.system()
if "linux" in osType.lower():
	osType = "linux"
elif "windows" in osType.lower():
	osType = "windows"


try:
	print("import PyQt5")
	from PyQt5.Qt import Qt 
	from PyQt5.QtWidgets import *
	import pyautogui
except:
	print("installing PyQt5")
	print(os.popen("pip3 install PyQt5").read())
	print(os.popen("pip3 install pyautogui").read())

	

if osType == "windows":
	try:
		print("import win32clipboard")
		import pkg_resources
		print("pkg_resources")
		pkg_resources.require("pywin32==227")
		print("win32clipboard") 
	except:
		print("installing win32clipboard")
		print(os.popen("pip3 install pywin32").read())

from coordFunc import *
from mainWindow import *





if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = InputBox(coordsX(), coordsY())
	sys.exit(app.exec_())
		

