class Settings():
	def __init__(self):
		"""Инициализирует статические настройки игры."""
		# Размеры и цвет экрана.
		self.screen_width = 1200
		self.screen_height = 800
		self.rgb_color = 230, 230, 230

		# Размеры пули и цвет.
		self.bullet_width = 15
		self.bullet_height = 3
		self.color_bullet = (60, 60, 60)
		self.number_bullets = 3

		# Лимит сделанных промахов.
		self.misses_limit = 2

		# Коофицент увеличение сложности игры.
		self.speedup_scale = 1.5

		self.initialize_game_settings()

	def initialize_game_settings(self):
		"""Инициализирует настройки, изменяющиеся в ходе игры."""
		self.speed_factor_spaceship = 1.5
		self.speed_factor_bullet = 3
		self.speed_factor_target = 1
		# Направление мишени.
		self.fleet_direction = 1

	def increase_speed(self):
		"""Увеличивает скорость игры."""
		self.speed_factor_spaceship *= self.speedup_scale
		self.speed_factor_bullet *= self.speedup_scale
		self.speed_factor_target *= self.speedup_scale
