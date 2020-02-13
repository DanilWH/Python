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

class ElectricCar(Car):
	"""Представляет аспекты машины, специфические для электромобилей."""
	def __init__(self, make,  model, year):
		"""
		Инициализирует атрибуты класса-родителя.
		Затем инициализирует атрибуты, специфические для электромобиля.
		"""
		super().__init__(make, model, year)
		self.battery= Battery() # Этот атрибут будет присутствовать во всех экземплярах, созданных на основе класса ElectricCar(но не во всяком экземпляре Car).

	def fill_gas_tank(self):
		"""У электромобилей нет бензобака"""
		print("This car does not need a gas tank!")
		# "Переопределение методов класса-родителя" стр. 173.

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
# my_tesla.describe_battery() # Сейчас этот код не работает, чтобы он заработал, нужно посмотреть код в "Определение атрибутов и методов класса-потомка" стр.172-173.

# Исходный класс называется родителем, а новый класс-потомком. Класс-потомок наследует атрибуты и методы родителя, но при этом также может определять собственные атрибуты и методы.

# В определении потомка, имя класса-родителя заключается в круглые скобки.

# Метод __init__ (который после def) получает информацию, необходимую для создания экземпляра Car.

# Функция super()-специальная функция, которая помогает Python связать потоммка с родителем.

# Имя super происходит зи распространённой терминологии: класс-родитель называется суперклассом, а класс-потомок - субклассом.

# "Метод __init__() класса-потомка." стр. 170-172.
