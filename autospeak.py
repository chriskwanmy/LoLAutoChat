import pyautogui
import pygetwindow as gw
import time

def speak():
	gwt = gw.getWindowsWithTitle('League of Legends (TM) Client')[0]
	# gwt = gw.getWindowsWithTitle('WhatsApp')[0]
	gwt.activate()

	time.sleep(1)
	pyautogui.moveTo.click(x=500, y=600)
	pyautogui.keyDown('shift')
	pyautogui.press('enter')
	pyautogui.keyUp('shift')
	pyautogui.write('Hello world!')
speak()