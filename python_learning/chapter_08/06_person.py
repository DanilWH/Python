def build_person(first_name, last_name):
	"""Возвращает словарь с информацией о человеке"""
	person = {'first': first_name, 'last': last_name}
	return person

musician = build_person('danil', 'lomakin')
print(musician)
# Возвращает словарь с информацией о человеке.

def build_person(first_name, last_name, age=''):
	"""Возвращает словарь с информацией о человеке"""
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person

musician = build_person('danil', 'lomakin', age=27)
print(musician)
# Пример сохранения возраста человека.
# Параметр age в определении функции является "необязательным".
