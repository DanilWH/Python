def sandwich_shop(*sandwichs):
	"""Выводит информацию о сендвичах"""
	print("\nOrdered sandwich: ")
	for sandwich in sandwichs:
		print("- " + sandwich)

sandwich_shop('russia')
sandwich_shop('bread', 'butter', 'fish')
sandwich_shop('arepa', 'bocadilo', 'crok-madam', 'ban-me', 'vada-pav')
# Упражнение 8-12.

def build_profile(
		first_name, last_name,
		**any_values_in_the_dictionary):
	user_info = {}
	user_info['first'] = first_name
	user_info['last'] = last_name
	for key, values in any_values_in_the_dictionary.items():
		user_info[key] = values
	return user_info
user_profile = build_profile('natasha', 'lomakina',
							location='Los-Angeles',
							age=46,
							year_of_birth=1971,
							education='profile average')
print(user_profile)
# Упражнение 8-13.

def made_car(manufacturer, name_car, **cars_features):
	car_info = {}
	car_info['manufacturer'] = manufacturer
	car_info['name_car'] = name_car
	for key, values in cars_features.items():
		car_info[key] = values
	return car_info

ready_car = made_car('USE', 'chevrolet',
					color='black',
					picking='everything')
print(ready_car)
# Упражнение 8-14.
