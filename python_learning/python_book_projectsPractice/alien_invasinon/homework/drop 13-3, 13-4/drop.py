import pygame
from pygame.sprite import Sprite

class Drop(Sprite):
	"""Класс капли."""
	def __init__(self, d_settings, screen):
		"""Инициализирует каплю и задаёт его начальную позицию."""
		super(Drop, self).__init__()
		self.screen = screen
		self.d_settings = d_settings

		# Загрузка изображения капли и назначение её начальной позиции
		self.image = pygame.image.load('drop_image.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Каждая новая капля появляется в левом верхнем углу экрана
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Сохранение точной позиции капли
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def blitme(self):
		"""Выводит каплю в текущем положении."""
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""Перемешает каплю вниз."""
		self.rect.y += self.d_settings.drop_speed_factor
