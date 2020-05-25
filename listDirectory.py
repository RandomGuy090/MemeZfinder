from clipboard import *
from config import *

from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt 
import sys, os




class ListDir():
	pwd = memeFolderPath

	def __init__(self):
		self.listDir()

	def listDir(self):
		imageFormats = ['JPEG', 'JPG', 'PNG', 'GIF', 'TIFF',
			    'PSD', 'PDF', 'EPS', 'AI', 'INDD', 'RAW']
		
		try:
			files = os.listdir(self.pwd+"/")
		except:
			print("nośnik z memami nie został zamonotwany")
			os.popen("notify-send -t 9000   'zamontuj nośnik z memami' '{0}' ".format(self.pwd))
		x = 0
		for elem in files:
			i = 0
			for char in elem:
				if char == ".":
					form = elem[i+1:]
					if form.upper() not in imageFormats or form == "txt" :
						print("DEL: {}".format(files[x]))
						del files[x]

					print("^^: x({0})  {1} format: {2}".format(x, elem, form))
				i = i+1
			x = x+1
		print(files)
		return files
