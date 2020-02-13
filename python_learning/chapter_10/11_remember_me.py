import json

# Программа загружает имя пользователя, если оно было сохранено ранее.
# В противном случае она запрашивает имя пользователя и сохраняет его.
filename = 'username.json'
try:
	with open(filename) as file_object:
		username = json.load(file_object)
except FileNotFoundError:
	username = input("What is your name? ")
	with open(filename, 'w') as file_object:
		json.dump(username, file_object)
		print("We'll remember you when you come back, " + username + "!")
else:
	print("Welcome back, " + username + "!")

# Объединённая программа с 12_greet_user.py

# Сохранение с использованием модуля json особенно полезно при работе с данными, сгенерированными пользователем, потому что без сохранения эта информация будет потеряна при остановке программы.

# Если программа выводит трассировку о сбое, значит нужно удалить существующий файл username.json.

# "Сохранение и чтение данных, сгенерированных пользователем" стр.205-207.

import json

def greet_user():
	"""Приветствует пользователя по имени."""
	filename = 'username.json'
	try:
		with open(filename) as file_object:
			username = json.load(file_object)
	except FileNotFoundError:
		username = input("What is your name? ")
		with open(filename, 'w') as file_object:
			json.dump(username, file_object)
			print("We'll remember you when you come back, " + username + "!")
	else:
		print("Welcome back, " + username + "!")

greet_user()
# Чтобы код стал чище можно переместить его в функцию.

# Подробнее о том как работает этот кода на стр. 207-209 "Рефакторинг".


import json

def get_stored_username():
	"""Получает хранимое имя пользователя, если оно существует."""
	filename = 'username.json'
	try:
		with open(filename) as file_object:
			username = json.load(file_object)
	except FileNotFoundError:
		return None
	else:
		return username
def greet_user():
	"""Приветствует пользователя по имени."""
	username = get_stored_username()
	if username:
		print("Welcome back, " + username + "!")
	else:
		username = input("What is your name? ")
		with open(filename, 'w') as file_object:
			json.dump(username, file_object)
			print("We'll remember you when you come back, " + username + "!")

greet_user()
# Здесь код разделился на уже на две функции, потому что функция в предыдущем примере решала слишком много разных задач.

# Подробнее о том как работает этот кода на стр. 207-209 "Рефакторинг".


import json

def get_stored_username():
	"""Получает хранимое имя пользователя, если оно существует."""
	filename = 'username.json'
	try:
		with open(filename) as file_object:
			username = json.load(file_object)
	except FileNotFoundError:
		return None
	else:
		return username
def get_new_username():
	"""Запрашивает новое имя пользователя."""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as file_object:
		json.dump(username, file_object)
	return username
def greet_user():
	"""Приветствует пользователя по имени."""
	username = get_stored_username()
	if username:
		print("Welcome back, " + username + "!")
	else:
		username = get_new_username()
		print("We'll remember you when you come back, " + username + "!")

greet_user()
# В этом примере код ещё больше разделился на функции по свои задачам.

# Подробнее о том как работает этот кода на стр. 207-209 "Рефакторинг".

# Рефакторинг - усовершенствование кода, разбивая его на функции, каждая из которых решает свою конкретную задачу.
