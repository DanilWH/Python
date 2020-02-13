main_menu = ['pasta', 'buckwheat porridge', 'rice', 'cabbage', 'tea', 'coffee', 'compote', 'salad', 'sandwich', 'meat']
available_toppings = ['meat', 'salad', 'tea', 'rice', 'cabbage', 'pasta']
requested_toppings = {}
admin_password = '3410'

def cancel_actions():
	while True:
		cancel = input('Cencel all entered actions(y/n)? ')

		if cancel == 'y':
			break
		elif cancel == 'n':
			continue
		else:
			print('"' + cancel + '" is not a comand!')
			continue

"""Функции админки."""
def add_topping():
	new_toppings = []

	while True:
		new_topping = input('Enter new topping: ').strip().lower()

		if new_topping == 'q':
			break
		elif new_topping in available_toppings:
			print(new_topping.title() + ' already in available menu!')
			continue # работает и без этого, но так читабельнее!
		elif new_topping == 'cancel':
			# ВНИМЕНИЕ! говнокод:
			while True:
				cancel = input('Cencel all entered actions(y/n)? ')

				if cancel == 'y':
					new_toppings.clear()
					break
				elif cancel == 'n':
					break
				else:
					print('"' + cancel + '" is not a comand!')
					continue
			if cancel == 'y':
				break
			# конец говнокода!

		elif new_topping:
				new_toppings.append(new_topping) # добавление во временный список.
				print(new_topping.title() + ' was added!')

	if new_toppings:
		# добавление всех новых блюд в доступное меню и в главное.
		for current_topping in new_toppings:
			main_menu.append(current_topping) # добавление в главное меню.
			available_toppings.append(current_topping) # добавление в доступное меню.
		print(', '.join(new_toppings).title() + ' was suttiful added!')

def remove_topping():
	# словарь для хранения удаляемых блюд (для вывода результата)
	removing_toppings = []

	while True:
		removing_topping = input('Enter topping that you want to remove: ')
		removing_topping = removing_topping.strip().lower()

		if removing_topping == 'q':
			break
		elif removing_topping == '':
			continue
		elif removing_topping not in available_toppings:
			print('This dish is not available in the menu!\nTry again!')
			continue
		elif removing_topping:
			# добавление удаляемого блюда в временный словарь
			removing_toppings.append(removing_topping)
			# удаление блюда из главного меню.
			available_toppings.remove(removing_topping)
			print(removing_topping.title() + ' was removed!')

	if removing_toppings:
		print(', '.join(removing_toppings).title() + ' was suttiful removed!')

def replace_topping():
	# временный словарь для хранения заменённых блюд (для вывода результата).
	replaced_toppings = {}

	while True:
		old_topping = input('Enter old topping: ').strip().lower()

		if old_topping == 'q':
			break
		elif old_topping == '':
			continue
		elif old_topping not in available_toppings:
			print('This dish is not available in the menu!\nTry again!')
			continue
		else:
			new_topping = input('Enter new topping: ').strip().lower()
			if new_topping == 'q':
				break
			elif new_topping == '':
				continue
			elif new_topping not in main_menu:
				print('This dish is not in the main menu!')
			else:
				print(available_toppings)
				# добавление заменённых блюд во временный словарь для последующего вывода результата.
				replaced_toppings[old_topping] = new_topping
				# возвращает индекс старого блюда в главном меню.
				old_inx = available_toppings.index(old_topping)
				# замена старого блюда на новое в глвном меню.
				available_toppings[old_inx] = new_topping
				print(old_topping.title() + ' was replaced by ' + new_topping +
					'.')
				print(available_toppings)

	# вывод результата:
	for old, new in replaced_toppings.items():
		print(old.title() + ' was replaced by ' + new + '!')


"""Функции пользователя."""
def user_actions():
	while True:
		# список для хранения заказов пользователя, который потом хранится как значению ключа в словаре requested_toppings.
		orders = []

		table_user = input('Enter your number of table(q): ').strip()

		if table_user in requested_toppings:
			print('Sory, but the table is busy. Please choise other table.')
			continue
		elif table_user == 'q':
			break
		else:
			while True:
				# запрос заказа
				order = input('Enter topping that you want to order: ')
				order = order.strip().lower()

				if order == 'q':
					break
				elif order == '':
					print('Do not enter empty value!')
					continue # работает и без этого, но так читабельнее.
				elif order in main_menu:
					if order in available_toppings:
						# добавление блюда в список заказа конкретного пользователя.
						orders.append(order)
						print('Adding ' + order + '!')
					else:
						print('Sory, but ' + order + ' have not now!')
						continue # работает и без этого, но так читабельнее!
				else:
					print(order.title() + ' is not on the menu!\nTry again!')
					continue # работает и без этого, но так читабельнее!
					print(orders)
		break

	# добавление в словарь столик пользователя (ключ) и его список заказа (значение).
	if table_user:
		if orders:
			requested_toppings[table_user] = orders

			print(', '.join(orders).title() + ' was suttiful added in your order for a table number ' + table_user + '!')
			print('Please, wait while your order will ready!')
		else:
			print('You have an empty order')
			answer = input('Continue or exit?').lower()
			if answer == 'continue':
				# стол хоть и с пустым заказом, но всё равно будет занят и имеет пустой список заказов.
				requested_toppings[table_user] = order
				print('Сome to table number ' + table_user + '.')

def admin_login():
	while True:
		login = False
		password = input('Enter password: ')

		if password.lower() == 'q':
			pass
		if password != admin_password:
			print('Enter password is wrong!\nTry again!')
			login = False
			continue # работает и без этого, но так читабельнее!
		elif password == admin_password:
			print('Successful login!')
			login = True
			break

	return login

def admin_change():

	login = admin_login()

	if login:
		while True:
			question = input('What do you want to do?(add/remove/replace): ')
			question = question.strip().lower()

			if question == 'q':
				break
			elif question == 'add':
				add_topping()
			elif question == 'remove':
				remove_topping()
			elif question == 'replace':
				replace_topping()
			else:
				print('"' + question + '" is not comand!')
				continue # работает и без этого, но так читабельнее.

while True:
	user_admin = input('Are you admin or user? ').strip().lower()
	
	if user_admin == 'admin':
		admin_change()
	elif user_admin == 'user':
		user_actions()
