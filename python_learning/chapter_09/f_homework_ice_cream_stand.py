class Restaurant():
	"""Выводит информацию о ресторане"""
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Выводит два атрибута"""
		print(self.restaurant_name.title() + " will treat you " + self.cuisine_type.title() + ".")

	def open_restaurant(self):
		"""Выводит сообщение о том, что ресторан открыт."""
		print("Restaurant " + self.restaurant_name.title() + " is open.")

	def set_number_served(self, served):
		self.number_served = served

	def increment_number_served(self, increment_served):
		self.number_served += increment_served

class IceCreamStand(Restaurant):
	"""
	Представляет аспекты ресторана, специфические для киосков с мороженным.
	"""
	def __init__(self, restaurant_name, cuisine_type):
		"""Инициализирует атрибуты киоска с мороженным"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = []

	def message_for_cream(self):
		for self.flavor in self.flavors:
			print(self.flavor.title())

cream = IceCreamStand('Frost', 'Cream')
cream.flavors = ['magnate', 'plombir', 'eskimo', 'horn']

cream.message_for_cream()
# Упражнение 9-6.


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
		print("Password: " + str(self.password))

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

class Admin(User):
	"""
	Представляет аспекты пользователей, специфические для администраторов.
	"""
	def __init__(self, first_name, last_name, age, alias, password):
		"""Инициализирует атрибуты администратора."""
		super().__init__(first_name, last_name, age, alias, password)
		self.privileges = []

	def show_privileges(self):
		for self.privilege in self.privileges:
			print(self.privilege)

admin = Admin('danil', 'lomakin', 15, 'dan_programmer', 341021946235102002)
admin.describe_user()

admin.privileges = [
	'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    	]
admin.show_privileges()
# Упражнение 9-7.


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

new_admin = Admin('natasha', 'lomakina', 46, 'natella', '19712808natalinatali')
new_admin.describe_user()

new_admin.privileges.show_privileges()

admin_privileges = [
	'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
new_admin.privileges.privileges = admin_privileges

new_admin.privileges.show_privileges()
# Упражнение 9-8.

class Car():
	"""Простая модель автомобиля"""
	def __init__(self, make, model, year):
		"""Инициализирует атрибуты для описания автомобиля."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0 

	def get_descriptive_name(self):
		"""Возвращаес аккуратно отформатированное описание."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()


	def read_odometer(self):
		"""Выводит пробег машины в милях"""
		print("This car has " + str(self.odometer_reading) + " miles on it.")


	def update_odometer(self, miliage):
		"""
		Устанавливает заданное значение на одометре.
		При попытке обратной подкрутки изменеие отклоняется.
		"""
		if miliage >= self.odometer_reading:
			self.odometer_reading = miliage
		else:
			print("You can not roll back an odometer!")

	def increment_odometer(self, miles):
		"""
		Увеличивает показания одометра с заданным приращением.
		При попытке обратной подкрутки изменеие отклоняется.
		"""
		if miles < 0:
			print("You can not roll back an odometer!")
		else:
			self.odometer_reading += miles

class Battery():
	"""Простая модель аккумулятора электромобиля."""
	def __init__(self, battery_size=70):
		"""Инициализирует атрибуты аккумулятора."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Выводит информацию о мощности аккумулятора."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

	def get_range(self):
		"""Выводит приблизительный запас хода для аккумулятора"""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)

	def upgrade_battary(self):
		if self.battery_size == 85:
			print("The battery pack is already updated!")
		else:
			print("Battery upgrade to 85 kWh...")
			self.battery_size = 85

class ElectricCar(Car):
	"""Представляет аспекты машины, специфические для электромобилей."""
	def __init__(self, make,  model, year):
		"""
		Инициализирует атрибуты класса-родителя.
		Затем инициализирует атрибуты, специфические для электромобиля.
		"""
		super().__init__(make, model, year)
		self.battery= Battery()

	def fill_gas_tank(self):
		"""У электромобилей нет бензобака"""
		print("This car does not need a gas tank!")

auto = ElectricCar('Japan', 'huaga', 2018)
print(auto.get_descriptive_name())
auto.battery.get_range()

auto.battery.upgrade_battary()

auto.battery.get_range()
# Упражнение 9-9.
