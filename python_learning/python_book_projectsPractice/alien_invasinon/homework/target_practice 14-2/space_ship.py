import pygame

class SpaceShip():
	"""Класс космического корабля."""
	def __init__(self, screen, g_settings):
		self.screen = screen
		self.g_settings = g_settings

		self.image = pygame.image.load('image/spaceship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		self.rect.right = self.screen_rect.right
		self.rect.centery = self.screen_rect.centery

		self.center = float(self.rect.centery)

		self.move_up = False
		self.move_down = False

	def update_ship(self):
		if self.move_up and self.rect.top > self.screen_rect.top:
			self.center -= self.g_settings.speed_factor_spaceship
		if self.move_down and self.rect.bottom < self.screen_rect.bottom:
			self.center += self.g_settings.speed_factor_spaceship
		self.rect.centery = self.center

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def center_spaceship(self):
		"""Выравнивает корабль по центру слевой стороны экрана."""
		self.center = self.screen_rect.centery