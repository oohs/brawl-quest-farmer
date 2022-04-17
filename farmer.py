import pyautogui
from pynput.keyboard import Key, Listener, Controller
import keyboard
#from pytesseract import pytesseract
import time
import random

#path_to_tesseract = r"C:\Users\annie\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def on_press(key):
	print(f"{key} pressed")
	if key == Key.esc:
		return False
	if key.char == 'b':
		# keep loopin
		i = 0
		while 1:
			# press to go to quests
			while 1:
				try:
					x, y = pyautogui.locateCenterOnScreen("pressForQuests.png", confidence = 0.8)
					pyautogui.click(x,y)
					break
				
				except TypeError:
					print('questsNotFound')
					time.sleep(0.5)
					#later add function to press random key to get out of stupid mess
		
	
			time.sleep(0.5)
			
			while 1:

				try:
					x, y = pyautogui.locateCenterOnScreen("pressForBrawlerQuest.png", confidence = 0.8)
					pyautogui.click(x,y)
					break
				
				except TypeError:
					for i in range(6):
						pyautogui.keyDown('a')
						time.sleep(0.3)
						pyautogui.keyUp('a')
					print('brawlerNotFound')
					
			time.sleep(0.5)
			#click to go to events
			pyautogui.click(x=989, y=958)
			time.sleep(0.5)

			#click to go to community maps
			while 1:

				try:
					x, y = pyautogui.locateCenterOnScreen("pressForCommunity.png", confidence = 0.8)
					pyautogui.click(x,y)
					break
				
				except TypeError:
					time.sleep(0.5)
					pyautogui.click(x=989, y=958)
					time.sleep(0.5)
					print('communityNotFound')			

			time.sleep(0.5)
			#choose a random community map
			while 1:

				try:
					x, y = pyautogui.locateCenterOnScreen("pressForMapMaker.png", confidence = 0.8)
					pyautogui.click(x,y+random.randint(175, 560))
					break
				
				except TypeError:
					pyautogui.click(x=989, y=958)
					print('mapmakerNotFound')			

			#press f to PLAY
			pyautogui.keyDown('f')
			time.sleep(0.1)
			pyautogui.keyUp('f')


			while 1: #we gamin boiz
				try:
					x, y = pyautogui.locateCenterOnScreen("pressForProceed.png", confidence = 0.8)
					time.sleep(1.5)
					pyautogui.click(x,y)
					time.sleep(0.05)
					#keep proceedin
					pyautogui.keyDown('f')
					time.sleep(0.1)
					pyautogui.keyUp('f')
					time.sleep(1)
					pyautogui.keyDown('f')
					time.sleep(0.1)
					pyautogui.keyUp('f')
					break
				except:
					directionY = random.choices(['w','s'], weights = (80,20))[0]
					directionX = random.choice(['d','a'])
					print(directionX, directionY)
					pyautogui.keyDown(directionY)
					pyautogui.keyDown(directionX)
					pyautogui.keyDown('space')
					time.sleep(0.1)
					pyautogui.keyUp('space')
					time.sleep(random.random()*2)
					pyautogui.keyDown('space')
					time.sleep(0.1)
					pyautogui.keyUp('space')
					print("boom boom")
					if random.random() > 0.69420:
						pyautogui.keyDown('shift')
						time.sleep(0.1)
						pyautogui.keyUp('shift')
						print("BANG")
					pyautogui.keyUp(directionY)
					pyautogui.keyUp(directionX)
					
			i += 1
			print('iteration:', i)

			time.sleep(1)

print("Press B to start BRAWLIN (aka run the program)")
print("Press esc to stop the program")


with Listener(
	on_press = on_press) as listener:
	listener.join()
