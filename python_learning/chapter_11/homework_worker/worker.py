class Employee():
	"""Класс представляющий работника."""
	def __init__(self, first_name, last_name, salary):
		self.first_name = first_name
		self.last_name = last_name
		self.salary = salary

	def give_raise(self, amount=5000):
		"""Увиличивает ежегодный оклад на $5000"""
		self.salary += amount
# Упражнение 11-3.
