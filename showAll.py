from clipboard import *
from config import *
from listDirectory import *

from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt 
import sys, os



class ShowAllMemes(QMainWindow):


	lista = ListDir().listDir() 
	lista = sorted(lista)
	pieces = 0
	for i in lista:
		pieces = pieces+1

	print(lista)
	print("""




		ShowAllMemes()""")
	Xcord = None
	Ycord = None

	

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

		self.Xcord = Xcord
		self.Ycord = Ycord

   
		self.widget = QWidget()   
    
		
		self.window(Xcord, Ycord)

		self.show()


	def window(self, Xcord, Ycord):

		Xcord = Xcord + 300
		Ycord = Ycord 

		self.layout()
		self.scroll()


		self.move(Xcord, Ycord)
		self.resize(300, 30)
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setStyleSheet(""" 
				background: {};		
			""".format(self.BGCOLOR))

	
		self.show()

	def scroll(self):
		self.scroll = QScrollArea()
		self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)	
		self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.scroll.setWidgetResizable(False)
		self.scroll.setWidget(self.widget)

		self.setCentralWidget(self.scroll)

	def layout(self):
		
		self.vbox = QVBoxLayout()
		
		object = QLabel("TOTAL: {}".format(self.pieces))
		object.move(0,5)
		self.vbox.addWidget(object)
		x = 0
		for meme in self.lista:
			memeBut = QPushButton(self)
			memeBut.setFixedWidth(280)
			memeBut.setText(meme)
			memeBut.clicked.connect(self.memeClicked)
			memeBut.setFlat(True)
			self.vbox.addWidget(memeBut)
		
		self.vbox.setContentsMargins(0, 0, 0, 0)
		self.widget.setLayout(self.vbox)

	


	def keyPressEvent(self, e):
		if e.key() == self.ESCAPE or e.key() == self.CTRL:
			self.close()

						
	def memeClicked(self):
		print("meme")
