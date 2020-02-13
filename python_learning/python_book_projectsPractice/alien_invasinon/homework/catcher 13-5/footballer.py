import pygame
from pygame.sprite import Sprite


class Footballer(Sprite):
	def __init__(self, screen, c_settings):
		super(Footballer, self).__init__()
		"""Инициализирует футболиста и задаёт ему начальную позицию."""
		
		self.screen = screen
		self.c_settings = c_settings

		# Загрузка изображения футблиста и получение прямоугольника.
		self.image = pygame.image.load('footballer.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		# Каждый новый футболист появляется у нижнего края экрана.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Сохранение вещественной координаты центра футболиста.
		self.center = float(self.rect.centerx)

		# Флаг перемещения.
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Обновляет позицию футболиста с учётом флага."""
		# Обновляется атрибут center, не rect.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.c_settings.footballer_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.c_settings.footballer_speed_factor

		# Обновление атрибута rect на основании self.center.
		self.rect.centerx = self.center

	def blitme(self):
		"""Рисует футболиста в текущей позиции."""
		self.screen.blit(self.image, self.rect)