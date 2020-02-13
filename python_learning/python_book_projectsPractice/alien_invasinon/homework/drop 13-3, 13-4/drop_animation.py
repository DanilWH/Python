import pygame
import sys
import function_drop as fd

from pygame.sprite import Group
from settings import Settings

def run_drop():
	pygame.init()
	d_settings = Settings()
	screen = pygame.display.set_mode(
		(d_settings.screen_width, d_settings.screen_height))
	pygame.display.set_caption("Drops")
	# Создание капли
	drops = Group()

	deleted_storage_drops = []

	# Создание сетки капель.
	fd.create_fleet(d_settings, screen, drops)

	while True:
		# Проверка событий клавиш
		fd.check_events()
		# Анимирование капель, падения вниз.
		fd.update_drops(drops)

		fd.update_edge_drops(d_settings, screen, drops, deleted_storage_drops)
		# Отрисовка окна
		fd.update_screen(screen, d_settings, drops)

run_drop()