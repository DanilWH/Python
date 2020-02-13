import sys
import pygame

from pygame.sprite import Group
from settings import Settings
from image_gun import Ship
import functions_game as fg

def run_game():
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_heidth))
	pygame.display.set_caption("Screen heidth")
	# Создание корабля.
	ship = Ship(screen, settings)
	# Создание группы для хранения пуль.
	bullets = Group()

	while True:
		fg.check_event(settings, ship, screen, bullets)
		ship.update()
		fg.update_bullets(bullets)
		fg.update_screen(settings, ship, screen, bullets)

run_game()