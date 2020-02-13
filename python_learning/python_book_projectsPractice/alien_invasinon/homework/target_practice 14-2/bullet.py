import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self, g_settings, spaceship, screen):
		super().__init__()
		self.screen = screen
		# Создание пули в позици (0, 0) и назначение её правильной позиции.
		self.rect = pygame.Rect(0, 0, g_settings.bullet_width,
			g_settings.bullet_height)
		self.rect.centery = spaceship.rect.centery
		self.rect.left = spaceship.rect.left

		self.x = float(self.rect.x)

		self.color = g_settings.color_bullet
		self.speed_factor = g_settings.speed_factor_bullet

	def update(self):
		"""Перемещает пулю влево по экрану."""
		self.x -= self.speed_factor
		self.rect.x = self.x

	def draw_bullet(self):
		"""Отрисовка пули на экране."""
		pygame.draw.rect(self.screen, self.color, self.rect)