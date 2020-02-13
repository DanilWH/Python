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

