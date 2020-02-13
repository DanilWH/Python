def greet_users(names):
	"""Вывод простого приветствия для каждого пользователя в списке"""
	for name in names:
		message = "Hello, " + name.title() + "!"
		print(message)

usernames = ['danil', 'galya', 'dasha']
greet_users(usernames)
# Пример передачи списка.
# Подробнее на стр.147-148. "Передача списка".
