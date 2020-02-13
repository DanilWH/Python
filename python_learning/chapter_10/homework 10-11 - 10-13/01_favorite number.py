import json

filename = 'favorite_numbers.json'
try:
	with open(filename) as file_object:
		favorite_numbers = json.load(file_object)
except FileNotFoundError:
	favorite_numbers = input("What's your favorite number? ")
	with open(filename, 'w') as file_object:
		json.dump(favorite_numbers, file_object)
		print("Okay, I will remember that.")
else:
	print("I know your favorite numbers! It is " + favorite_numbers + "!")
# Упражнение 10-11 и 10-12


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
		check = input("Are you " + username + "? (yes/no): ")
		if check == 'yes':
			print("Welcome back, " + username + "!")
		else:
			username = get_new_username()
			print("We'll remember you when you come back, " + username + "!")
	else:
		username = get_new_username()
		print("We'll remember you when you come back, " + username + "!")

greet_user()
# Упражнение 10-13.
