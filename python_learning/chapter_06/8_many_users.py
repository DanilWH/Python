users = {
	'aeinshtein': {
		'first': 'albert',
		'last': 'einshtein',
		'location': 'prisenton',
	},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris'
	},
}

for username, user_info in users.items():
	print("Username: " + username.title())
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
# Словарь также можно вложить в другой словарь, но в таких случаях код быстро усложняется.
# "Словарь в словаре" стр.118-119.
