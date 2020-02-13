def make_pizza(size, *toppings):
	"""Выводит информацию о дополнениях к пицце"""
	print("\nMaking a " + str(size) + "-inch pizza wich the following toppings:")
	for topping in toppings:
		print("- " + topping)
