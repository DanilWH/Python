class Restaurant():
	"""Выводит информацию о ресторане"""
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""Выводит два атрибута"""
		print(self.restaurant_name.title() + " will treat you " + self.cuisine_type.title() + ".")

	def open_restaurant(self):
		"""Выводит сообщение о том, что ресторан открыт."""
		print("Restaurant " + self.restaurant_name.title() + " is open.")

restaurant = Restaurant('queen', 'pizza')
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())

print(" ")

restaurant.describe_restaurant()
restaurant.open_restaurant()
# Упражнение 9-1.
print(" ")

restaurant_0 = Restaurant('malahit', 'georgian')
restaurant_0.describe_restaurant()

restaurant_1 = Restaurant('chayka', 'russia')
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant('chayhana', 'japanese')
restaurant_2.describe_restaurant()
# Упражнение 9-2.
print(" ")

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

	def describe_user(self):
		"""Выводит информацию о пользователе."""
		print("User: " + self.first_name.title())
		print("Last name: " + self.last_name.title())
		print("Age: " + str(self.age))
		print("Alias: " + self.alias.title())
		print("Password: " + str(self.password))

	def greet_user(self):
		"""Выводит простое приветствие для пользователя."""
		print("Hello " + self.first_name.title() + " " +
			self.last_name.title() + ".\n")

user_0 = User('danil', 'lomakin', 15, 'dan programmer', '341021946235102002')
user_0.describe_user()
user_0.greet_user()

user_1 = User('natasha', 'lomakina', 46, 'natella', '19712808natalinatali')
user_1.describe_user()
user_1.greet_user()

user_2 = User('oleg', 'lomakin', 44, 'oracular', '271072')
user_2.describe_user()
user_2.greet_user()
# Упражнение 9-3.
