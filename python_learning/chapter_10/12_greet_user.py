import json

filename = 'username.json'
with open(filename) as file_object:
	username = json.load(file_object)
	print("Welcome back, " + username + "!")
# Программа, которая приветствуе пользователя по ранее созранённому имени.
# Пример обьеденённой программы с 11_remember_me.py в файле 11_remember_me.py.
# "Сохранение и чтение данных, сгенерированных пользователем" стр.205-207.
