##pobieranie i przetwarzanie koordynatów myszy 
##TYLKO LINUX
import sys, os
import pyautogui


def coordsX():
	x, y = pyautogui.position()

	
	print("X: {}".format(x))
	return int(x)
def coordsY():
	x, y = pyautogui.position()
	print("Y: {}".format(y))
	return int(y)







