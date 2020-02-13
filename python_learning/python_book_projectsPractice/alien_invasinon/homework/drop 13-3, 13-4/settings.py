class Settings():
	"""Класс для хранения всеё настроек окна и капель."""
	def __init__(self):
		# Параметры окна
		self.screen_width = 1200
		self.screen_height = 800
		self.rgb_color = (230, 230, 230)
		self.drop_speed_factor = 1