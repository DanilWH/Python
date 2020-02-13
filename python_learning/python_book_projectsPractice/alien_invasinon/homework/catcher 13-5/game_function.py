import pygame
import sys
import random

from ball import Ball
from footballer import Footballer

def check_keydown_events(event, footballers):
	for footballer in footballers.sprites():
		"""Реагирует на нажатия клавиш."""
		if event.key == pygame.K_RIGHT:
			footballer.moving_right = True
		elif event.key == pygame.K_LEFT:
			footballer.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()

def check_keyup_event(event, footballers):
	for footballer in footballers.sprites():
		"""Реагирует на отпускание клавиш."""
		if event.key == pygame.K_RIGHT:
			footballer.moving_right = False
		elif event.key == pygame.K_LEFT:
			footballer.moving_left = False

def check_event(footballers):
	"""Отслеживает события клавиатуры."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, footballers)
		elif event.type == pygame.KEYUP:
			check_keyup_event(event, footballers)

def update_screen(c_settings, screen, footballers, balls):
	"""Обновляет изображение на экране и отображает новый экран."""
	# При каждом проходе цикла перерисовывается экран.
	screen.fill(c_settings.rgb_color)
	# Рисует футболиста и мяч в текущей позиции.
	footballers.draw(screen)
	balls.draw(screen)
	# Отображение послежнего прорисованного экрана.
	pygame.display.flip()

def create_footboller(footballers, screen, c_settings):
	# Создаёт экзепляр футболиста.
	footballer = Footballer(screen, c_settings)
	# Добавляет его в группу.
	footballers.add(footballer)

def create_ball(balls, screen, c_settings):
	"""Создаёт мяч."""
	ball = Ball(screen, c_settings)
	balls.add(ball)

def check_position_ball(balls, screen, c_settings):
	ball = Ball(screen, c_settings)

	for ball in balls.copy():
		if ball.rect.right > c_settings.screen_width or ball.rect.left < 0:
			balls.remove(ball)
			create_ball(balls, screen, c_settings)
		elif ball.rect.top > c_settings.screen_height:
			balls.remove(ball)
			create_ball(balls, screen, c_settings)

def update_ball(balls, footballers, screen, c_settings):
	"""Обновляет позицию мяча."""
	balls.update()

	collisions = pygame.sprite.groupcollide(footballers, balls, False, True,)

	if len(balls) == 0:
		# Уничтожение мяча и создание нового мяча.
		balls.empty()
		create_ball(balls, screen, c_settings)

def update_footballer(footballers, balls):
	"""Обновляет позицию футболиста."""
	footballers.update()