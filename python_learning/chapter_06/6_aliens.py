alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)
# Чтобы создать флот пришельцев нужно, сначала создать нужное количество словарей(то есть пришельцев) и потов все словари закинуть в список.


# Создание пустого списка для хранения пришельцев.
aliens = []
# Создание 30 зелёных пришельцев.
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
# Превращение первых трёх пришельцов в жёлтый цвет с другими характиристиками.
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	# Превращение жёлтых пришельцев в крассный цвет с др. хар-ми.
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

# Вывод первых 5 пришельцев.
for alien in aliens[:5]:
	print(alien)
print("...")

# Вывод количеста созданных пришельцев.
print("Total number of aliens: " + str(len(aliens)))
# Пример генерирования 30 пришельцев на стр.114-115.
