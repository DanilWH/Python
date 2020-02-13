"""Класс для представления автомобиля"""
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
		self.battery= Battery() 
		
	def fill_gas_tank(self):
		"""У электромобилей нет бензобака"""
		print("This car does not need a gas tank!")

"""
По идее классы ElectricCar и Battery можно удалить, для более правильного примера импорта в файле i_my_cars.py, но не стираю чтобы другие примеры в i_my_cars.py работали.
"""