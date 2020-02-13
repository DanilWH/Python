import pygame
from time import sleep
import sys
import random

from ball import Ball
from footballer import Footballer

def check_keydown_events(event, footballer):
	"""Реагирует на нажатия клавиш."""
	if event.key == pygame.K_RIGHT:
		footballer.moving_right = True
	elif event.key == pygame.K_LEFT:
		footballer.moving_left = True
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_event(event, footballer):
	"""Реагирует на отпускание клавиш."""
	if event.key == pygame.K_RIGHT:
		footballer.moving_right = False
	elif event.key == pygame.K_LEFT:
		footballer.moving_left = False

def check_event(footballer):
	"""Отслеживает события клавиатуры."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, footballer)
		elif event.type == pygame.KEYUP:
			check_keyup_event(event, footballer)

def update_screen(c_settings, screen, footballer, balls):
	"""Обновляет изображение на экране и отображает новый экран."""
	# При каждом проходе цикла перерисовывается экран.
	screen.fill(c_settings.rgb_color)
	# Рисует футболиста и мяч в текущей позиции.
	footballer.blitme()
	balls.draw(screen)
	# Отображение послежнего прорисованного экрана.
	pygame.display.flip()

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

def del_ball_and_create_ball(balls, screen, c_settings):
	# Удаляет мяч и создаёт новый.
	balls.empty()
	create_ball(balls, screen, c_settings)

def footballer_hit(stats, balls, footballer, screen, c_settings):
	"""Обрабатывает сторкновение футболиста с мячом."""
	if stats.footballers_left > 0:
		# Уменьшение sleep_left.
		stats.footballers_left -= 1

		# Очистка спискоа мяча.
		balls.empty()

		# Создание нового мяча в случ. позиции и размещение футболиста в центре.
		create_ball(balls, screen, c_settings)
		footballer.center_footballer()

		# Пауза.
		sleep(0.5)
	else:
		stats.game_active = False

def check_aliens_bottom(screen, balls, stats, c_settings, footballer):
	"""Проверяет добрался ли мяч до нижнего края экрана."""
	srceen_rect = screen.get_rect()
	for ball in balls.sprites():
		if ball.rect.bottom >= srceen_rect.bottom:
			# Происходит пауза и создание нового мяча.
			footballer_hit(stats, balls, footballer, screen, c_settings)
			

def update_ball(balls, footballer, screen, c_settings, stats):
	"""Обновляет позицию мяча."""
	balls.update()
	# Выявление коллизий между футболистом и мячом.
	if pygame.sprite.spritecollideany(footballer, balls):
		del_ball_and_create_ball(balls, screen, c_settings)

	# Проверка мяча, добравшийся до нижнего края экрана.
	check_aliens_bottom(screen, balls, stats, c_settings, footballer)

def update_footballer(footballer, balls):
	"""Обновляет позицию футболиста."""
	footballer.update()