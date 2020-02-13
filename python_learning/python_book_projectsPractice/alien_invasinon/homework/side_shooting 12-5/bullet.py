import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""Класс для управлениями пулями, выпущеным кораблём."""
	def __init__(self, settings, ship, screen):
		"""Создаёт объект пули в текужей позиции пистолета."""
		super(Bullet, self).__init__()
		self.screen = screen

		# Создание пули и назначение правильной позиции.
		self.rect = pygame.Rect(0,0, settings.bullet_width, settings.bullet_heidth)
		self.rect.centery = ship.rect.centery
		self.rect.right = ship.rect.right
		# Хранение позиции пули в вещественном формате.
		self.x = float(self.rect.x)

		self.color = settings.bullet_color
		self.bullet_speed = settings.bullet_speed_factor

	def update(self):
		"""Перемещение пули вправо по экрану."""
		# Обновление позиции пули в вещественном формате.
		self.x += self.bullet_speed
		# Обновление позиции прямоугольника.
		self.rect.x = self.x
	def draw_bullet(self):
		"""Вывод пули на экран."""
		pygame.draw.rect(self.screen, self.color, self.rect)
		