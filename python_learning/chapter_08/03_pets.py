def describe_pet(animal_type, pet_name):
	"""Выводит информатию о животном"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
# Значения связанные с аргументами подобным образом, называются позиционными аргументами.
# При вызове describe_pet() необходимо передать тип и имя - именно в таком порядке.
# "Позизионные аргументы" стр.137-138.

def describe_pet(animal_type, pet_name):
	"""Выводит информатию о животном"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
# Функция может вызываться в программе столько раз, сколько потребуется, причём с другими аргументами.
# "Многократные вызову функций" стр.138.

def describe_pet(animal_type, pet_name):
	"""Выводит информатию о животном"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('harry', 'hamster')
# Если нарушить порядок следования аргументов в вызове при позиционных аргументов, вывод получится безсмысленным.
# "О важности порядка позиционных аргументов"стр.138-139.

def describe_pet(animal_type, pet_name):
	"""Выводит информатию о животном"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='harry',animal_type='hamster')
# Пример именнованных аргументов. Представляет собой пару "имя-занчение".
# Имя и значение связываются с аргументом напрямую, так что при передаче аргумент апутаница с порядком исключается.
# "Именованные аргументы"стр.138.

def describe_pet(pet_name, animal_type='dog'):
	"""Выводит информатию о животном"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
# Пример знвызова значений по умолчанию.
# Нужно обратить внимание: в определении функции пришлось изменить порядок параметров.
# Все параметры со значением по умолчанию должны следовать после параметров, у которых значений по умолчанию нет.
# "Значения по умолчанию" стр.140-141.
