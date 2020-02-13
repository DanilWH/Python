class GameStats():
	def __init__(self, g_settings):
		self.g_settings = g_settings
		self.reset_stats()

		self.game_active = False

	def reset_stats(self):
		self.number_of_misses = self.g_settings.misses_limit