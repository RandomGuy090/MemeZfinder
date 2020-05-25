from clipboard import *
from config import *
from highlightWindow import *
from listDirectory import *
from showAll import *


from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt 
import sys, os





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
	showAll = None
	osType = None

	CTRL = showAllKey
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

		elif e.key() == self.CTRL:

			self.showAll = ShowAllMemes(self.Xcord, self.Ycord)


			

		
		
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