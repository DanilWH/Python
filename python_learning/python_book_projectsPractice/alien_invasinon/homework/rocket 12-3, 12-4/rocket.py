import sys
import pygame

from settings import Settings
from image_rocket import Rocket
import rocket_function as rf

def rocket():
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_heigth))
	pygame.display.set_caption("Rocket")

	rocket = Rocket(settings, screen)

	while True:
		rf.check_events(rocket) # События клавиш и мыши.
		rocket.update() # Обновление позиций ракеты.
		screen.fill(settings.rgb_color) # Заполняет экран определённым цветом.
		rocket.blitme() # Вызывает метод в классе, который рисует ракету.

		pygame.display.flip() # Отображение последнего прорисованного экрана.
rocket()
