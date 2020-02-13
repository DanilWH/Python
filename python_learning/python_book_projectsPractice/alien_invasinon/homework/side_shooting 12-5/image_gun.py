import pygame

class Ship():
	def __init__(self, screen, settings):
		self.screen = screen
		self.settings = settings
		# Загружает изображение корабля.
		self.image = pygame.image.load('ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		# Устанавливает корабль в текущей позиции.
		self.rect.centery = self.screen_rect.centery
		self.rect.left = self.screen_rect.left
		# Сохранение в вещественную коодинату.
		self.center = float(self.rect.centery)
		# Флаги для перемещения.
		self.moving_up = False
		self.moving_down = False

	def update(self):
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.center -= self.settings.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.center += self.settings.ship_speed_factor

		self.rect.centery = self.center

	def blitme(self):
		"""Рисует изображение корабля."""
		self.screen.blit(self.image, self.rect)