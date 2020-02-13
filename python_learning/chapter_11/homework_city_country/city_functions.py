def get_city_country(city, country, population=''):
	"""Выводит отформатированное название города и страны."""
	if population:
		full_name = city.title() + " " + country.title() + "-population " + str(population) + "."
	else:
		full_name = city.title() + " " + country.title() + "."
	return full_name
# Упражнение 11-1 и 11-2.
