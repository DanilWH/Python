class User():
	"""Выводит информацию о человеке."""
	def __init__(self, first_name, last_name, age, alias, password):
		"""Инициализирует атрибуты:
		first_name, last_name, age, alias, password."""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.alias = alias
		self.password = password
		self.login_attempts = 0

	def describe_user(self):
		"""Выводит информацию о пользователе."""
		print("\nUser: " + self.first_name.title())
		print("Last name: " + self.last_name.title())
		print("Age: " + str(self.age))
		print("Alias: " + self.alias.title())
		print("Password: " + str(self.password) + "\n")

	def greet_user(self):
		"""Выводит простое приветствие для пользователя."""
		print("Hello " + self.first_name.title() + " " +
			self.last_name.title() + ".\n")

	def increment_iogin_attempts(self):
		"""Увиличивает значение login_attempts на 1."""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Обнуляет значение login_attempts."""
		self.login_attempts = 0
