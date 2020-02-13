from collections import OrderedDict
golossariy = OrderedDict()

golossariy['concatenation'] = 'line break'
golossariy['variable'] = 'place of memory'
golossariy['list'] = 'itemset'
golossariy['if'] = 'condition'
golossariy['tuples'] = 'an immutable list'
golossariy['dictionary'] = 'the creation of real objects'
golossariy['"keys()"'] = 'if you are only interested in the keys pars'
golossariy['"value()"'] = 'if you are only interested in the values pars'
golossariy['"items()"'] = 'display vocabularies in a list'
golossariy['"sorted()"'] = 'sort lists, tuples, dictionaries, and more'

for word, definition in golossariy.items():
	print(word.title() +
		":\n\t" + definition + ".")
# Упражнение 9-13(переделанное 6-4).


from random import randint

class Die():
	def __init__(self, sides=6):
		"""Инициализирует атрибуты для сторон куба"""
		self.sides = sides

	def roll_die(self):
		"""Выводит наугад любое число от 1 до сторон куба"""
		number = randint(1, self.sides)
		return number

sides = Die()
cube_6 = []
for roll in range(10):
	cube_6.append(sides.roll_die())
print("\n10 rolls:")
print(cube_6)
# 
cube_10 = Die(10)
cube_witch_10 = []
for roll in range(10):
	cube_witch_10.append(cube_10.roll_die())
print("\n10 rolls:")
print(cube_witch_10)
# Моделирования 10-гранного куба с 10 бросками.

cube_20 = Die(20)
cube_witch_20 = []
for roll in range(10):
	cube_witch_20.append(cube_20.roll_die())
print("\n10 rolls:")
print(cube_witch_20)
# Моделирование 20-гранного куба с 10 бросками.

# Упражнение 9-14.
