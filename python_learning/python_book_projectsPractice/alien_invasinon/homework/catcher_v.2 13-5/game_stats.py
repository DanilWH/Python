class GameStats():
	"""Отслеживание статистики игры catcher."""

	def __init__(self, c_settings):
		"""Инициалицирует статистику."""
		self.c_settings = c_settings
		self.reset_stats()
		# Игра запускается в активном состоянии.
		self.game_active = True

	def reset_stats(self):
		"""Инициализирует статистику, изменяющуюся в ходе игры."""
		self.footballers_left = self.c_settings.footballer_limit