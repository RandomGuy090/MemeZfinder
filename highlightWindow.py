from clipboard import *
from config import *
from listDirectory import *


from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt 
import sys, os

from PyQt5.QtGui import QIcon, QPixmap



class HighlightWin(QWidget):
	print(""" 




		HighlightWin

		""")

	height = higlightHeight
	width = higlightWidth

	pwd = memeFolderPath

	Y = None
	X = None
	keyEvent = None
	textboxContent = None
	str1 = None
	str2 = None
	str3 = None
	run = True
	osType = None
	showAll = None

	KEY = higlightKey
	ESCAPE = escapeKey
	ENTER = enterKey
	CTRL = showAllKey



	def __init__(self, X, Y, keyEvent, textboxContent, str1, str2, str3, osType):
		super().__init__()
		print("HighlightWin.INIT")
		self.osType = osType
		self.str1 = str1
		self.str2 = str2
		self.str3 = str3
		self.X = X
		self.Y = Y
		self.keyEvent = keyEvent 
		self.textboxContent = textboxContent
		
		self.window(X, Y)

		run = self.setPic()
		if run == None:
			self.close()
		else:
			self.show()

	def window(self, X, Y):
		self.move(X, Y)
		self.resize(self.height, self.width)
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)
	

	def keyPressEvent(self, e):
		if e.key() == self.ENTER:
			self.keyEnter()
			self.close()
			sys.exit()

		
		elif e.key() in \
		{Qt.Key_Left, self.KEY, self.ESCAPE}:
			self.close()

		elif e.key() == self.CTRL:
			self.showAll = ShowAllMemes(self.Xcord, self,Ycord)
			self.showAll.close()
		

		print("{}".format(e))

	def keyEnter(self):
		if self.keyEvent == 1:
			print(self.textboxContent)
			Clipboard(self.textboxContent, self.osType)
		elif self.keyEvent == 2:
			print(self.str1)
			Clipboard(self.str1, self.osType)
		elif self.keyEvent == 3:
			print(self.str2)
			Clipboard(self.str2, self.osType)
		elif self.keyEvent == 4:
			print(self.str3)
			Clipboard(self.str3, self.osType)
		self.close()
	
	

	def addPic(self):
		if self.keyEvent == 1:
			path = self.pwd + "/" + self.textboxContent
		elif self.keyEvent == 2:
			path = self.pwd + "/" + self.str1
		elif self.keyEvent == 3:
			path = self.pwd + "/" +self.str2 
		elif self.keyEvent == 4:
			path = self.pwd + "/" +self.str3

		if self.textboxContent == "" and self.str1 == "":
			print("self.textboxContent: ''")
			self.close()
			return None
		return path

	def setPic(self):
		
		pic = self.addPic()
		if pic == None:
			self.close()
			print("CLOSE")
			return None
		label = QLabel(self)
		pixmap = QPixmap(pic)
		
		pixmap = pixmap.scaled(self.height, self.width, Qt.KeepAspectRatio, Qt.FastTransformation)
		h = pixmap.height()
		w = pixmap.width()
		self.resize(w, h)
		label.setPixmap(pixmap)
		return True
			
	def closing(self):
		if self.run == True:
			return False
		elif self.run == False:
			return True