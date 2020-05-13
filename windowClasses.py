from clipboard import *
from config import *

from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt 
import sys, os

from PyQt5.QtGui import QIcon, QPixmap



class InputBox(QWidget):
	widthWindow = windowWidth
	heightWindow = windowHeight
	textboxContent = ""
	lista = [" ", " ", " ",]
	lista2 = ["", "", ""]
	str1 = ""
	str2 = ""
	str3 = ""
	keyEvent = 1

	Ycord = None
	Xcord = None

	hightlight = None
	osType = None

	KEY = higlightKey
	ESCAPE = escapeKey
	ENTER = enterKey
	BGCOLOR = backgroundColor
	HIGLIGHTED = higlighted
	LABELCOLOR = labelColor
	INPUTCOLOR = inputFieldColor


	def __init__(self, Xcord, Ycord):
		super().__init__()

		self.osType = platform.system()
		if "linux" in self.osType.lower():
			self.osType = "linux"
		elif "windows" in self.osType.lower():
			self.osType = "windows"

		self.Xcord = Xcord
		self.Ycord = Ycord
		print(Xcord)
		print(Ycord)
		self.window(Xcord, Ycord)
		self.grid()
		#self.label()
		self.setLayout(self.grid)
		#listClass = ListDir()
		self.lista = ListDir().listDir()

		self.show()
			
	def grid(self):
		self.grid = QGridLayout()
		self.grid.addWidget(self.label(), 1, 1)
		self.grid.addWidget(self.labelLeft(), 1,1)
		self.grid.addWidget(self.inputField(), 2, 1)
		self.grid.addWidget(self.label2(), 3, 1)
		self.grid.addWidget(self.label3(), 4, 1)
		self.grid.addWidget(self.label4(), 5, 1)
		self.grid.addWidget(self.button(), 6, 1)

	def window(self, Xcord, Ycord):
		self.move(Xcord, Ycord)
		self.resize(300, 30)
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setStyleSheet(""" 
				background: {};		
			""".format(self.BGCOLOR))

	def label(self):
		label = QLabel(self)
		label.move(0,0)
		label.resize(self.widthWindow, 5)
		label.setStyleSheet("QLabel{background-color: "+ self.LABELCOLOR+";}")
	def labelLeft(self):
		label = QLabel(self)
		label.move(0,5)
		label.resize(5, 100)
		#label.setText(content)
		label.setStyleSheet("QLabel{background-color: "+ self.LABELCOLOR+";}")

	def inputField(self):
		self.inputBox = QLineEdit(self)
		self.inputBox.move(0, 5)
		self.inputBox.resize(self.widthWindow, 25)
		self.inputBox.setStyleSheet("QLineEdit{background-color: "+self.INPUTCOLOR+";}")
		
		self.inputBox.textChanged.connect(self.changed)

	def changed(self):
		self.textboxContent = self.inputBox.text()
		self.inputBox.resize(self.widthWindow-25, 25)
		self.arrowLabel.resize(25, 30)
		self.button()
		self.list()
		
		print(self.textboxContent)

	def button(self):
		self.arrowLabel = QPushButton(self)
		self.arrowLabel.move(self.widthWindow-25 , 0)
		self.arrowLabel.resize(0, 0)
		self.arrowLabel.setText("\u2193")
		self.arrowLabel.clicked.connect(self.roll)
		
	def roll(self):
		self.resize(self.widthWindow, 90)

	def label2(self):
		self.label2 = QLabel(self)
		self.label2.move(5, 30)
		self.label2.resize(self.widthWindow, 20)
		self.label2.setText(" ")

	def label3(self):
		self.label3 = QLabel(self)
		self.label3.move(5, 50)
		self.label3.resize(self.widthWindow, 20)
		self.label3.setText(" ")

	def label4(self):
		self.label4 = QLabel(self)
		self.label4.move(5, 70)
		self.label4.resize(self.widthWindow, 20)
		self.label4.setText(" ")

	def list(self):
		i=0
		x=0
		
		for elem in self.lista:
			#self.lista[i] = self.lista[i].lower()
			self.textboxContent = self.textboxContent
			if self.osType == "windows":
				if self.textboxContent in self.lista[i] in self.lista[i]:
					print("##"+self.lista[i] + "  {}".format(i)) 
					
					try:
						self.lista2[x] = self.lista[i] 
						
					except:
						print("lol")
					x +=1
					self.str1 = self.lista2[0]
					self.str2 = self.lista2[1]
					self.str3 = self.lista2[2]
					c = 0
					for character in self.str1:
						if character in self.textboxContent:
							self.str1first = self.str1[:c]
						else:
							c = c+1
					self.str1last = self.str1[c+len(self.textboxContent):]
					#self.str1xD = self.str1first + termcolor.colored(self.textboxContent, "green") + self.str1last
					#print(self.str1xD)
					self.label2.setText(self.str1)
					self.label3.setText(self.str2)
					self.label4.setText(self.str3)
					print(self.lista2)
					print("%:{0}, {1}, {2}".format(self.str1, self.str2, self.str3))
				
			elif self.osType == "linux":
				if self.textboxContent in self.lista[i] and "png" in self.lista[i]:
					print("##"+self.lista[i] + "  {}".format(i)) 
					
					try:
						self.lista2[x] = self.lista[i] 
						
					except:
						print("lol")
					x +=1
					self.str1 = self.lista2[0]
					self.str2 = self.lista2[1]
					self.str3 = self.lista2[2]
					c = 0
					for character in self.str1:
						if character in self.textboxContent:
							self.str1first = self.str1[:c]
						else:
							c = c+1
					self.str1last = self.str1[c+len(self.textboxContent):]
					#self.str1xD = self.str1first + termcolor.colored(self.textboxContent, "green") + self.str1last
					#print(self.str1xD)
					self.label2.setText(self.str1)
					self.label3.setText(self.str2)
					self.label4.setText(self.str3)
					print(self.lista2)
					print("%:{0}, {1}, {2}".format(self.str1, self.str2, self.str3))
			i = i+1

			


	def keyPressEvent(self, e):
		if e.key() == self.ESCAPE:
			self.close()
		elif e.key() == Qt.Key_Down:		
			self.keyEvent =self.keyEvent+1
			if self.keyEvent >=4:
				self.keyEvent = 4
			self.keyDown()

		elif e.key() == Qt.Key_Up:
			self.keyEvent =self.keyEvent-1
			if self.keyEvent <=1:
				self.keyEvent = 1
			self.keyUp()

		elif e.key() == self.ENTER:
			print("ENTER")
			self.keyEnter()

		elif e.key() == self.KEY:
			print("HighlightWin")
			self.hightlight = HighlightWin(self.Xcord+self.widthWindow, self.Ycord,
				self.keyEvent, self.textboxContent, self.str1, self.str2, self.str3, self.osType)

			print(self.hightlight.closing())

			

		
		
		print("self.keyEvent: {}".format(self.keyEvent))

	def keyDown(self):
		
		if self.keyEvent == 1:
			
			self.label2.setStyleSheet("QLabel{background-color: "+ self.BGCOLOR+";}")
			self.label3.setStyleSheet("QLabel{background-color: "+ self.BGCOLOR+";}")
			self.label4.setStyleSheet("QLabel{background-color: "+ self.BGCOLOR+";}")

		elif self.keyEvent == 2:
			self.resize(300 , 50)
			self.label2.setStyleSheet("QLabel{background-color: "+ self.HIGLIGHTED+";}")
			self.label3.setStyleSheet("QLabel{background-color: "+ self.BGCOLOR+";}")
			self.label4.setStyleSheet("QLabel{background-color: "+ self.BGCOLOR+";}")

		elif self.keyEvent == 3:
			self.resize(300 , 70)
			self.label2.setStyleSheet("QLabel{background-color: "+ self.BGCOLOR+";}")
			self.label3.setStyleSheet("QLabel{background-color: "+ self.HIGLIGHTED+";}")
			self.label4.setStyleSheet("QLabel{background-color: "+ self.BGCOLOR+";}")

		elif self.keyEvent == 4:
			self.resize(300 , 90)
			self.label2.setStyleSheet("QLabel{background-color: "+ self.BGCOLOR+";}")
			self.label3.setStyleSheet("QLabel{background-color: "+ self.BGCOLOR+";}")
			self.label4.setStyleSheet("QLabel{background-color: "+ self.HIGLIGHTED+";}")
			if self.keyEvent >=4:
				self.keyEvent = 4
		
	def keyUp(self):
		
		if self.keyEvent == 1:
			self.resize(300 , 30)
			self.label2.setStyleSheet("QLabel{background-color: "+ self.BGCOLOR+";}")
			self.label3.setStyleSheet("QLabel{background-color: "+ self.BGCOLOR+";}")
			self.label4.setStyleSheet("QLabel{background-color: "+ self.BGCOLOR+";}")
			if self.keyEvent < 1:
				self.keyEvent = 1

		elif self.keyEvent == 2:
		
			self.label2.setStyleSheet("QLabel{background-color: "+ self.HIGLIGHTED+";}")
			self.label3.setStyleSheet("QLabel{background-color: "+ self.BGCOLOR+";}")
			self.label4.setStyleSheet("QLabel{background-color: "+ self.BGCOLOR+";}")
			
		elif self.keyEvent == 3:
		
			self.label2.setStyleSheet("QLabel{background-color: "+ self.BGCOLOR+";}")
			self.label3.setStyleSheet("QLabel{background-color: "+ self.HIGLIGHTED+";}")
			self.label4.setStyleSheet("QLabel{background-color: "+ self.BGCOLOR+";}")

		elif self.keyEvent == 4:
			self.label2.setStyleSheet("QLabel{background-color: "+ self.BGCOLOR+";}")
			self.label3.setStyleSheet("QLabel{background-color: "+ self.BGCOLOR+";}")
			self.label4.setStyleSheet("QLabel{background-color: "+ self.HIGLIGHTED+";}")
			
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
			os.popen("notify-send -t 9000 -i {0}/MemeZfinder/icon.png  'zamontuj nośnik z memami' '{0}' ".format(self.pwd))
		x = 0
		for elem in files:
			i = 0
			for char in elem:
				if char == ".":
					form = elem[i+1:]
					if form.upper() not in imageFormats or form == "txt":
						print("DEL: {}".format(files[x]))
						del files[x]

					print("^^: x({0})  {1} format: {2}".format(x, elem, form))
				i = i+1
			x = x+1
		print(files)
		return files


class HighlightWin(QWidget):

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

	KEY = higlightKey
	ESCAPE = escapeKey
	ENTER = enterKey



	def __init__(self, X, Y, keyEvent, textboxContent, str1, str2, str3, osType):
		super().__init__()
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

		elif e.key() == Qt.Key_Left or e.key() == self.KEY or e.key() == self.ESCAPE:
			self.close()

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
