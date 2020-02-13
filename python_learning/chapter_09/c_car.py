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

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
# "Назначение атрибуту значения по умолчанию."стр. 166-167.

my_new_car.odometer_reading = 26
my_new_car.read_odometer()
# Первый способ изменения значения. Чтобы изменить значение атрибута, проще всего обратиться к нему прямо через экземпляр.
# Чаще разработчик пишет вспомогательный метод, который изменяет значение за него.
# "Прямое изменение значения атрибута"стр. 167.

my_new_car.update_odometer(30)
my_new_car.read_odometer()
# Второй способ изменения значения.
# "Изменение значения атрибута с использованием метода"стр.167-168.

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
# Третий способ изменения значения, только уже с приращением.
# "Изменеие атрибута с приращением"стр. 168-169.
