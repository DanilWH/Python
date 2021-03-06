alen_0 = {'color': 'green', 'points': 5}
# Словарь представляет собой совокупность пар "ключ-значение".
# Значением может быть любой объект, создаваемый в программе Python(число, строка, список и даже ругой словарь).
# Подробнее на стр. 102 "Работа со словарями"
print(alen_0['color'])
print(alen_0['points'])
# Чтобы получить значение, связанное с ключом, укажите имя словаря, а затем ключ в квадратных скобках.

alen_0 = {'color': 'green', 'points': 5}
new_alen = alen_0['points']
print("You just earned " + str(new_alen) + " points.")# Вы только что заработали 5 очков.
# Если, допустим, игрок сбивает корабль пришельца, для получения заработанных им очков может использоваться код в примере выше.
# Если этот код будет выполняться каждый раз, когда игрок сбивает очередного пришельца, программа будет полусать правильное количество очков.
# "Обращение к значениям в словаре" стр. 102-103.

alen_0 = {'color': 'green', 'points': 5}
print(alen_0)
alen_0['x_position'] = 0
alen_0['y_position'] = 25
print(alen_0)
# Чтобы добавить новоые пары в список, нужно указать имя словаря, за которым в квадратных скобках следует новых ключ с новым значением.
# "Добавление новых пар ключ-значение" стр.103.

alen_0 = {}

alen_0['color'] = 'green'
alen_0['points'] = 5

print(alen_0)
# Чтобы начать заполнение пустого словаря, нужно определить словарь с пустой парой фигурных скобок, а затем добавить новые пары "ключ-значение"(каждая пара в отдельной стоке).
# "Создание пустого словаря" стр.103-104.

alen_0 = alen_0 = {'color': 'green'}
print("The alen is " + alen_0['color'] + ".")

alen_0['color'] = 'yellow'
print("The alen is now " + alen_0['color'] + ".")
# Чтобы изменить значение в словаре, нужно указать имя словаря с ключом в квадратных скобках, а затем новое значение, которое должно быть связанно с этим ключом.
# "Изменение значений в словаре" стр.104.

alen_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("\nOriginal x_position: " + str(alen_0['x_position']))
# alen_0['speed'] = 'fast'
# Пришелец перемещается вправо.
# Вычисляем велечину смещения на основании текущей скорости.

if alen_0['speed'] == 'slow':
	x_increment = 1
elif alen_0['speed'] == 'medium':
	x_increment = 2
else:
	# Пришелец двигается быстро.
	x_increment = 3
# Новая позиция равна сумме старой позиции и приращения.
alen_0['x_position'] = alen_0['x_position'] + x_increment
print("New x_position: " + str(alen_0['x_position']))
# Подробнее на стр.104-105 "Изменение значений в словаре".

alen_0 = {'color': 'green', 'points': 5}
print(alen_0)

del alen_0['points']
print(alen_0)
# Чтобы удалить пар "ключ-значение", можно удалить при помощи команды del. При вызове достаточно передать имя словаря и удаляемый ключ. Отменить удаление уже нельзя.
# "Удаление пар ключ-значение"стр.105.

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
# Словарь также может использоваться для хранения одного вида информации о многих объектах.
# Допустим, нужно провется опрос у коллег и узнать их любимый язык программирования.
# Пары в словаре в этой записи разбиты по строкам.
# Подробно на стр.106-107.
