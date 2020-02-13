import pygame

from pygame.sprite import Group

from settings import Settings
import function_game as fg
from space_ship import SpaceShip
from target import Target
from game_stats import GameStats
from button import Button

def run_game():
	pygame.init()
	g_settings = Settings()
	screen = pygame.display.set_mode((
		g_settings.screen_width, g_settings.screen_height))
	pygame.display.set_caption("Target practice")

	# Создание экземпляра корабля.
	spaceship = SpaceShip(screen, g_settings)

	# Создание экземпляра мишени.
	target = Target(screen, g_settings)

	# Экземпляр статистики игры.
	stats = GameStats(g_settings)

	# Создание группы для пуль
	bullets = Group()

	# Создание экземпляра кнопки.
	play_button = Button(g_settings, screen, 'В бой!')

	while True:
		fg.event_tracking(spaceship, g_settings, screen, bullets, play_button,stats, target) # Отслеживание событий клавиатуры.
		if stats.game_active:
			spaceship.update_ship() # Обновление позиции корабля.
			fg.update_bullets(g_settings, bullets, target, spaceship, stats)
			fg.update_target(target)

		fg.update_screen(screen, g_settings, spaceship, target, bullets,play_button, stats) # Обновление и перерисовка экрана
run_game()
