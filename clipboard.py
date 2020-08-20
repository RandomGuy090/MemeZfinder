import os, platform
from config import *
try:
	import win32clipboard
except:
	print("lol")
class Clipboard():


	vidFormats =""" WEBM MPG, . MP2, . MPEG,
				. MPE, . MPV.OGG MP4, . M4P,
				. M4V.AVI, . WMV.MOV, . QT.FLV,
				. SWF.AVCHD."""
	imageFormats = """
			    JPEG JPG PNG GIF TIFF
			     PSD PDF EPS AI INDD RAW

					"""
	def __init__(self, filename, osType):
		self.getPath()

		if "linux" in osType.lower():
			self.getImageLinux(filename)
		elif "windows" in osType.lower():
			
			self.getImageWin(filename)



	def getPath(self):
		self.path = os.getcwd()
		
	
	def getImageLinux(self, filename):
		#self.path = self.path+"/MEMES/"
		#self.path = "/media/randomguy90/cheny/"
		self.path = memeFolderPath+"/"
		print("CurrentPath: {}".format(self.path))

		self.path = self.path+filename
		self.i = 0
		for elem in self.path:
			if elem ==".":
				self.format = self.path[self.i+1:]
			else:
				self.i = self.i+1
		
		print("PATH TO FILE: {}".format(self.path))
		print("IMAGE format: {}".format(self.format))
		print("image TAKEN")

		if self.format.upper() in self.imageFormats:
			print("IMAGE TYPE")
			os.popen("xclip -selection clipboard -t image/png -i '{}'".format(self.path))
		elif self.format.upper() in self.vidFormats:
			print("VIDEO TYPE")
			os.popen("xclip -selection clipboard -t video/mp4 -i '{}'".format(self.path))	
		
		
	
	def getImageWin(self, filename):
		import io
		from PIL import Image

		self.path = memeFolderPath+"\\"
		print("CurrentPath: {}".format(self.path))

		self.path = self.path + filename
		image = Image.open(self.path)
		output = io.BytesIO()
		image.convert("RGB").save(output, "BMP")
		data = output.getvalue()[14:]
		output.close()
		self.sendToClipboard(8, data)

	def sendToClipboard(self, clip_type, data):
	    win32clipboard.OpenClipboard()
	    win32clipboard.EmptyClipboard()
	    win32clipboard.SetClipboardData(clip_type, data)
	    win32clipboard.CloseClipboard()		

	