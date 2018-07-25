from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time

sense = SenseHat()
sense.clear()

class stack():
	def __init__(self):
		pygame.init()
		pygame.display.set_mode((640, 480))
		self.gaming = True

	def startGame(self):
		pygame.time.set_timer(USEREVENT +1, 800)
		column = 0
		row = 7
		while self.gaming:
			for event in pygame.event.get():

				if event.type == KEYDOWN:

					sense.set_pixel(column-1, row, (0, 0, 255))
					row -= 1
					column = 0
					if (row == 8):
						row = 0
					if (column == 8):
						column = 0

				else:
					sense.set_pixel(column,row, (0, 255, 0))
					time.sleep(.3)
					sense.set_pixel(column, row, (0, 0, 0))
					time.sleep(.3)
					column += 1
					if (column == 8):
						column = 0

if __name__ == "__main__":
	try:
		game = stack()
		game.startGame()
	except KeyboardInterrupt:
		sense.clear()
