import pygame
from pygame.sprite import Sprite

class Star(Sprite):
	def __init__(self, settings, screen):
		super(Star, self).__init__()
		self.screen = screen
		self.settings = settings

		# Загрузка фото звезды и назначение атрибута rect.
		self.image = pygame.image.load('star.bmp')
		self.rect = self.image.get_rect()

		# Каждая звезда появляется в левом верхнем углу экрана.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Сохранение точной позиции звезды.
		self.x = float(self.rect.x)

	def blitme(self):
		"""Выводит звезду в текущем положении."""
		self.screen.blit(self.image, self.rect)
