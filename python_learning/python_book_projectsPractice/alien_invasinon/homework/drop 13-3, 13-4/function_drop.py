import pygame
import sys

from drop import Drop

def check_events():
	"""Проверяет события клавиш."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				sys.exit()

def update_screen(screen, d_settings, drops):
	"""Обновления окна."""

	# Заполнение цветом
	screen.fill(d_settings.rgb_color)
	# Отрисовка капли
	drops.draw(screen)
	# Обновление экрана
	pygame.display.flip()

def get_number_drops_x(d_settings, drop_width):
	"""Вычисляет количество капель в ряду."""
	available_spase_x = d_settings.screen_width - 2 * drop_width
	number_drops_x = int(available_spase_x / (2 * drop_width))
	return number_drops_x

def get_number_rows(d_settings, drop_height):
	"""Определяет количество рядов, помещяущихся на эране."""
	available_spase_y = (d_settings.screen_height - (1 * drop_height))
	number_rows = int(available_spase_y / (2 * drop_height))
	return number_rows

def create_drop(d_settings, screen, drops, drop_number, row_number):
	"""Создаёт каплю и размещает её в ряду."""
	drop = Drop(d_settings, screen)
	drop_width = drop.rect.width
	drop.x = drop_width + 2 * drop_width * drop_number
	drop.rect.x = drop.x
	drop.rect.y = drop.rect.height + 2 * drop.rect.height * row_number
	drops.add(drop)

def create_fleet(d_settings, screen, drops):
	"""Создаёт ряд капель."""
	# Создание каплю и вычисление количества капель в ряду.
	drop = Drop(d_settings, screen)
	number_drops_x = get_number_drops_x(d_settings, drop.rect.width)
	number_rows = get_number_rows(d_settings, drop.rect.height)

	# Создание первого ряда капель.
	for row_number in range(number_rows):
		for drop_number in range(number_drops_x):
			# Создание капли и размещение ёё в ряду.
			create_drop(d_settings, screen, drops, drop_number, row_number)

def update_drops(drops):
	"""Обновляет позиции всех капель."""
	drops.update()

def update_edge_drops(d_settings, screen, drops, deleted_storage_drops):
	for drop in drops:
		if drop.rect.top >= 800:
			deleted_storage_drops.append(drop)
			drops.remove(drop)

			number_drops_x = get_number_drops_x(d_settings,
			drop.rect.width)

			if len(deleted_storage_drops) == number_drops_x:
				for drop_number in range(number_drops_x):
					# Создание капли и размещение ёё в ряду.
					drop = Drop(d_settings, screen)
					drop_width = drop.rect.width
					drop.x = drop_width + 2 * drop_width * drop_number
					drop.rect.x = drop.x
					drops.add(drop)
				del deleted_storage_drops[:]
	print(len(drops))