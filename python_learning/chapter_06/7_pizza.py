# Сохранение информации о заказанной пицце.
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}

# Описание заказа.
print("You order a " + pizza['crust'] + "-crust pizza " +
	"witch the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping.title())
# Пример вложения списка в словарь.
# Для того, чтобы перебрать спиок в словаре, нужно указать имя словаря и затем в квадратных скобках указать ключ (pizza['toppings']).

print(" ")

# Сохранение информации о заказанной пицце.
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	'elite toppings': ['olives', 'rosemary', 'bulgarian pepper']
	}

# Описание заказа.
print("You order a " + pizza['crust'] + "-crust pizza " + 
			"witch the following toppings:")

for name, toppings in pizza.items():
	if 'toppings' in name or 'elite toppings' in name:
		print(name.title() + ":")
		for topping in toppings:
			print("\t" + topping.title())
if 'toppings' not in name and 'elite toppings' not in name:
	print("You just ordered pizza with " + pizza['crust'] + " crust.")
# (Упражнение 6-12.).Расширенный пример предыдушей программы.
