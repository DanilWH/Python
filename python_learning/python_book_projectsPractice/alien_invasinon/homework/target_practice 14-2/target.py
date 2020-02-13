import pygame

class Target():
	def __init__(self, screen, g_settings):
		self.screen = screen
		self.g_settings = g_settings

		# Загрузка изображения.
		self.image = pygame.image.load('image/mishen.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		# Назначение координаты.
		self.rect.centery = self.screen_rect.centery
		self.rect.left = self.screen_rect.left

		self.y = float(self.rect.centery) # Назначение вещественной координаты.

	def check_edges(self):
		if self.rect.top <= self.screen_rect.top:
			self.g_settings.fleet_direction = 1
		if self.rect.bottom >= self.screen_rect.bottom:
			self.g_settings.fleet_direction = -1
	def update_target(self):
		"""Обновляет позицию мишени."""
		self.y += (self.g_settings.speed_factor_target * 
			self.g_settings.fleet_direction)
		self.rect.centery = self.y

	def blitme_target(self):
		self.screen.blit(self.image, self.rect)

	def center_target(self):
		"""Выравнивает мишень по центру справой стороны экрана."""
		self.y = self.screen_rect.centery