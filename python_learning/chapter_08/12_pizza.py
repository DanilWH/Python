def make_pizza(*toppings):
	"""Вывод списка заказанных дополнений"""
	print(toppings)

make_pizza('pepperoni')
make_pizza('mushroms', 'green peppers', 'extra cheese')
# Звёздочка в имени параметра *toppings приказывает Python создать пустой кортеж с именем toppings и упаковать в него все полусенные значения.
# Python упаковывает аргументы в кортеж даже в том случае, если функция получает всего одно значение.

def make_pizza(*toppings):
	"""Выводит описание пиццы."""
	print("\nMaking a pizza wich the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushroms', 'green peppers', 'extra cheese')
# Теперь команду print можно заменить циклом, который перебирает список дополнений и выводит описание заказанной пиццы.
# Этот синтаксис работает независимо от количества аргументов, переданных фкнуции.
# "Передача произвольных набора аргументов" стр. 151-152.

def make_pizza(size, *toppings):
	"""Выводит описание пиццы."""
	print("\nMaking a " + str(size) + "-inch pizza wich the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroms', 'green peppers', 'extra cheese')
# Если нужно, чтобы функция могла вызываться с разными количествами аргументов, параметр для получения произвольного количества аргументов должен стоять на последнем месте в определении функции.
# Python сначала подбирает соответствия для позиционных и именнованных аргументов, а потом объединяет все остальные аргументы в последнем параметре.
# "Позиционные аргументы с произвольными наборами аргументов" стр. 152-153.
