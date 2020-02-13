while True:
	toppings = input("Введи твои дополнения к пицце: ")

	if toppings == 'quit':
		break
	else:
		print(toppings.title() + " included in your order.")
# Упражнение 7-4.

while True:
	age = input("Какой ваш возраст? ")
	age = int(age)
	
	if age < 3:
		print("Ваш билет бесплатный.")
	elif age < 12:
		print("Ваш билет стоит $10")
	else:
		print("Ваш билет стоит $15")
# Упражнение 7-5.

message = ""
while message != 'quit':
	message = input("Какой ваш возраст? ")
	if message != 'quit':
		message = int(message)
		if message < 3:
			print("Ваш билет бесплатный.")
		elif message < 12:
			print("Ваш билет стоит $10")
		else:
			print("Ваш билет стоит $15")
# Задание 1 упражнения 7-6.

active = True
while active:
	message = input("Какой ваш возраст? ")
	if message == 'quit':
		active = False
	else:
		message = int(message)
		if message < 3:
			print("Ваш билет бесплатный.")
		elif message < 12:
			print("Ваш билет стоит $10")
		else:
			print("Ваш билет стоит $15")
# Задание 2 упражнения 7-6.

while True:
	message = input("Какой ваш возраст? ")
	if message == 'quit':
		break
	else:
		message = int(message)
		if message < 3:
			print("Ваш билет бесплатный.")
		elif message < 12:
			print("Ваш билет стоит $10")
		else:
			print("Ваш билет стоит $15")
# Задание 3 упражнения 7-6.
