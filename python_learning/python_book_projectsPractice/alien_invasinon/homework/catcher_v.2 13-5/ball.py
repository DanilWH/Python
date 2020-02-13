import pygame
import random
from pygame.sprite import Sprite

class Ball(Sprite):
	def __init__(self, screen, c_settings):
		super(Ball, self).__init__()
		self.screen = screen
		self.c_settings = c_settings

		# Загрузка избражения мяча.
		self.image = pygame.image.load('ball.bmp')
		self.rect = self.image.get_rect()

		# Каждый новый мяч появляется в рандомной позиции верхнего края экрана.
		self.rect.x = random.randint(0, c_settings.screen_width)
		self.rect.bottom = self.rect.top

		# Хранение точной позиции мяча.
		self.y = float(self.rect.bottom)

	def update(self):
		"""Перемещает мяч вниз."""
		self.y += self.c_settings.ball_speed_factor
		self.rect.bottom = self.y

	def blitme(self):
		"""Выводит мяч в текущем положении."""
		self.screen.blit(self.image, self.rect)