def get_formatted_name(first_name, last_name):
	"""Возвращает аккуратно отформатированное полное имя."""
	full_name = first_name + " " + last_name
	return full_name.title()
musician = get_formatted_name('danil', 'lomakin')
print(musician)
# Команда return передаёт значение из функции в строку, в которой эта функция была вызвана.
# Значение, возвращаемое функцией, называется возвращаемым значением.

def get_formatted_name(first_name, last_name, middle_name=''):
	"""Возвращает аккуратно отформатированное полное имя."""
	if middle_name:
		full_name = first_name + ' ' + middle_name + " " + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
# Пример необязательных аргументов (в данном примере, необязательным аргументом является middle_name).
# Необязательные значения позволяют функциям рабоать в максимально широком спекторе сценариев использования без усложнения вызовов.
# Подробнее на стр.143-145 "Необязательные аргументы".
