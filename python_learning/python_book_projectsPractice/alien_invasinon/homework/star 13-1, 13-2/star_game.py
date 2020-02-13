import sys
import pygame

from settings import Settings
from image_star import Star
from pygame.sprite import Group
import game_functions as gf

def run_game():
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	pygame.display.set_caption("Falling stars")

	stars = Group()

	# Создание экземпляра звезды.
	star = Star(settings, screen)

	# Создание флота пришельца.
	gf.create_fleet(settings, screen, stars)

	while True:
		gf.check_events()
		gf.update_screen(screen, settings, stars)
run_game()
# Задание 13-2 не доделано.