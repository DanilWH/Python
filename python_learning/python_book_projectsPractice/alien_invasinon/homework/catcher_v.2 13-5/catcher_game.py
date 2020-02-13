import pygame
import sys

import game_function as gf
from settings import Settings
from footballer import Footballer
from game_stats import GameStats
from ball import Ball
from pygame.sprite import Group

def run_game():
	pygame.init()
	c_settings = Settings()
	screen = pygame.display.set_mode(
		(c_settings.screen_width, c_settings.screen_height))
	pygame.display.set_caption("Catcher")
	# Создание экземпляра для хранения игровой статистики.
	stats = GameStats(c_settings)

	# Создание футболиста и мяча.
	footballer = Footballer(screen, c_settings)
	balls = Group()

	gf.create_ball(balls, screen, c_settings)

	while True:
		# Отслеживение событий клавиатуры.
		gf.check_event(footballer)

		if stats.game_active:
			# Передвижение футболиста.
			gf.update_footballer(footballer, balls)
			# Передвижение мяча.
			gf.update_ball(balls, footballer, screen, c_settings, stats)
			# Проверка позиции мяча.
			gf.check_position_ball(balls, screen, c_settings)
		# Обновление изображения на экране и отображение нового экрана.
		gf.update_screen(c_settings, screen, footballer, balls)

run_game()
