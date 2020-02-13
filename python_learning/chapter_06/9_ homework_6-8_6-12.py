animal_0 = {
	'type': 'cat',
	'owner': 'danil',
}
animal_1 = {
	'type': 'dog',
	'owner': 'sasha',
}
animal_2 = {
	'type': 'cow',
	'owner': 'zoyka',
}
animal_3 = {
	'type': 'puma',
	'owner': 'tom',
}
animal_4 = {
	'type': 'chiken',
	'owner': 'katya',
}
pets = [animal_0, animal_1, animal_2, animal_3, animal_4]

for pet in pets:
	print(pet)
# Упражнение 6-8.

favorite_places = {
	'danil': ['home', 'mount'],
	'galya': ['witch me'],
	'dasha': ['street', 'city', 'clubs'],
}
for name, places in favorite_places.items():
	print("\n" + name.title() + " favorite places:")
	for place in places:
		print("\t" + place.title())
# Упражнение 6-9.

print(" ")

cities = {
	'los-angeles':{
		'country': 'usa',
		'population': 3976322,
		'fact': 'hollywood',
		},
	'moskow':{
		'country': 'russia',
		'population': 12506468,
		'fact': 'kremlin'
		},
	'barcelona':{
		'country': 'span',
		'population': 1620809,
		'fact': 'skate street',
		},
	}
for city, info in cities.items():
	if info['country'] == 'usa':
		country = info['country'].upper()
	else:
		country = info['country'].title()
	
	print("City-" + city.title() + ":")
	population = info['population']
	fact = info['fact'].title()
	print("\tCountry: " + country)
	print("\tPopulation: " + str(population))
	print("\tFact: " + fact)
# Упражнение 6-11 и 6-12(использование условий if и else).
