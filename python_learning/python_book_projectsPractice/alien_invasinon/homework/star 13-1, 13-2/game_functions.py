import sys
import pygame

from image_star import Star
from random import randint

def check_events():
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

def update_screen(screen, settings, stars):
	screen.fill(settings.rgb_color)
	stars.draw(screen)

	pygame.display.flip()

def get_number_stars_x(settings, star_width):
	"""Вычисления количества звёзд в ряду."""
	available_space_x = settings.screen_width - 2 * star_width
	number_stars_x = int(available_space_x / (2 * star_width))
	return number_stars_x

def get_number_rows(settings, star_height):
	available_space_y = (settings.screen_height -
		(3 * star_height))
	number_rows = int(available_space_y / (2 * star_height))
	return number_rows

def create_star(settings, screen, stars, star_number, row_number):
	star = Star(settings, screen)
	star_width = star.rect.width
	star.x = randint(0, 1200)
	star.rect.x = star.x
	star.rect.y = randint(0, 800)
	stars.add(star)

def create_fleet(settings, screen, stars):
	star = Star(settings, screen)
	number_stars_x = get_number_stars_x(settings, star.rect.width)
	number_rows = get_number_rows(settings, star.rect.height)

	# Создание сетки звёзд.
	for row_number in range(number_stars_x):
		for star_number in range(number_rows):
			create_star(settings, screen, stars, star_number, row_number)
			