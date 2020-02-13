def build_profile(first, last, **user_info):
	"""Строит словарь с информацией о пользователе."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('danil', 'lomakin',
							location='Los-Angeles',
							field='program')
print(user_profile)
# Две звёздочки перед параметром **user_ifno заставляют Python создать пустой словарь с именем user_info и упаковать в него все полученные пары "имя-значение" из user_info точно так же, как в любом словаре.
"""Иногда программа должна получать произвольное количество аргументов, но нельзя узнаеть заранее, какая информация будет передаваться функции. В таких случаях можно написать функцию, получающую столько пар "ключь-значение", сколько указанно в команде вызова."""
