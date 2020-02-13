import pygame

class Rocket():
	def __init__(self, settings, screen):
		"""Инициализирует ракету и задаёт её начальную позицию."""
		self.screen = screen
		self.settings = settings
		# Загрузка изображения ракеты и получение прямоугольника.
		self.image = pygame.image.load('image/rocket.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		# Каждая новая ракет появляется в середине окна.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		# Сохранение вещественной координаты ракеты.
		self.center_x = float(self.rect.centerx)
		self.center_y = float(self.rect.centery)
		# Флаги перемещения
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Обновляет позицию ракеты с учётом флага."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center_x += self.settings.rocket_speed_factor
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.center_x -= self.settings.rocket_speed_factor
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.center_y -= self.settings.rocket_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.center_y += self.settings.rocket_speed_factor

		# Обновление атрибута rect на основании center_x и center_y.
		self.rect.centerx = self.center_x
		self.rect.centery = self.center_y

	def blitme(self):
		"""Рисует ракету в текущей позиции."""
		self.screen.blit(self.image, self.rect)
