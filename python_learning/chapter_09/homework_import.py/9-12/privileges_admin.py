from user import User

class Admin(User):
	"""
	Представляет аспекты пользователей, специфические для администраторов.
	"""
	def __init__(self, first_name, last_name, age, alias, password):
		"""Инициализирует атрибуты администратора."""
		super().__init__(first_name, last_name, age, alias, password)
		self.privileges = Privileges()

class Privileges():
	def __init__(self, privileges=[]):
		self.privileges = privileges

	def show_privileges(self):
		for self.privilege in self.privileges:
			print(self.privilege)