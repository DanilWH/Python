alen_color = 'green'

if alen_color == 'green':
	print('You have earned 5 points!')
# Работающая версия программы.
# Первое задание упражнения 5-3.
alen_color = 'yellow'

if alen_color == 'red':
	print('You have earned 5 points')
# Не работающая программа.
# Второе задание упражнения 5-3.

alen_color = 'red'

if alen_color == 'green':
	points = 5
elif alen_color == 'yellow':
	points = 10
else:
	points = 15
print('You have earned ' + str(points) + ' points!')
# Первое задание упражнения 5-4.
# elif-дополнение из 1,2 и 3 задания из кпражнения 5-5.

alen_color = 'red'

if alen_color == 'red':
	message = '\nYou red alen! Hoho!'
elif alen_color == 'green':
	message = '\nWow, you green alen! Heh.'
elif alen_color == 'yellow':
	message = '\nOh, are you the yellow newcomer?'
print(message)
# Первая версия четвёртого задания упражнения 5-5.

alen_color = 'green'

if alen_color == 'red':
	message = 'You the red alen! Hoho!'
elif alen_color == 'green':
	message = 'Wow, you are the green alen! Heh.'
else:
	message = 'Oh, are you the yellow newcomer?'
print(message)
# Вторая версия четвёртого задания упражнения 5-5.

alen_color = 'yellow'

if alen_color == 'red':
	message = 'You red alen! Hoho!'
elif alen_color == 'green':
	message = 'Wow, you green alen! Heh.'
else:
	message = 'Oh, are you the yellow newcomer?'
print(message)
# Третья версия четвёртого задания упражнения 5-5.

age = 20

if age < 2:
	print('\nBaby')# Младенец.
elif age < 4:
	print('\nKid')# Малыш.
elif age < 13:
	print('\nChild')# Ребёнок.
elif age < 20:
	print('\nTennager')# Подросток.
elif age < 65:
	print('\nAduld')# Взрослый.
else:
	print('\nOlder person')# Пожилой человек.
# Упражнение 5-6.

favorite_fruits = ['peach', 'apricat', 'banana']

if 'lemon' in favorite_fruits:
	print('You really like lemon!')
if 'peach' in favorite_fruits:
	print('You really like peach!')
if 'banana' in favorite_fruits:
	print('You really like banana!')
if 'apple' in favorite_fruits:
	print('You really like apple!')
if 'apricat' in favorite_fruits:
	print('You really like apricat!')
# Упражнение 5-7

print(' ')

favorite_fruits = ['peach', 'banana', 'apricat']

if 'lemon' in favorite_fruits:
	fruits = 'lemon'
if 'peach' in favorite_fruits:
	fruits = 'peach'
if 'banana' in favorite_fruits:
	fruits = 'banana'
if 'apple' in favorite_fruits:
	fruits = 'apple'
if 'apricat' in favorite_fruits:
	fruits = 'apricat'

for fruit in favorite_fruits:
	print('You really like ' + fruit + '!')
# Та-же программа(5-7),только с использованием цикла for(собственной разработкой).
