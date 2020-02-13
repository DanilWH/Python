import pygame
import sys

import game_function as gf
from settings import Settings
from footballer import Footballer
from ball import Ball
from pygame.sprite import Group

def run_game():
	pygame.init()
	c_settings = Settings()
	screen = pygame.display.set_mode(
		(c_settings.screen_width, c_settings.screen_height))
	pygame.display.set_caption("Catcher")

	# Создание футболиста и мяча.
	footballer = Footballer(screen, c_settings)
	footballers = Group()
	balls = Group()

	gf.create_ball(balls, screen, c_settings)
	gf.create_footboller(footballers, screen, c_settings)

	while True:
		# Отслеживение событий клавиатуры.
		gf.check_event(footballers)
		# Передвижение футболиста.
		gf.update_footballer(footballers, balls)
		gf.update_ball(balls, footballers, screen, c_settings)
		gf.check_position_ball(balls, screen, c_settings)
		# Обновление изображения на экране и отображение нового экрана.
		gf.update_screen(c_settings, screen, footballers, balls)

run_game()