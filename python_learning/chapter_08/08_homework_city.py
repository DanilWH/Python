def city_country(city, country):
	full = city + ", " + country + "."
	return full

ready = city_country(city='Los-Angeles', country='USE')
print(ready)

my_def = city_country(city='Moskow', country='Russia')
print(my_def)

my_def = city_country(city='Piter', country='Russia')
print(my_def)

my_def = city_country(city='San-Francisko', country='USE')
print(my_def)
# Упражнение 8-6.

print(' ')

def make_album(name, album_name, tracks=''):
	album = {'name': name, 'album': album_name}
	if tracks:
		album['tracks'] = tracks
	return album

end = make_album(name='kizaru', album_name='yad')
print(end)

end = make_album(name='smokepurpp', album_name='bleesyotrap')
print(end)

end = make_album(name='$uicideboys', album_name='radical $uicide')
print(end)

end = make_album(name='playboi', album_name='playboy carti', tracks=22)
print(end)
# Упражнение 8-7

def make_album(name, album_name):
	album = {'name': name, 'album': album_name}
	return album

while True:
	print("\n(enter 'q' if want to quit):")
	artist = input("Enter an artist: ")
	if artist == 'q':
		break
	album = input("Enter an album: ")
	if album == 'q':
		break
	full = make_album(artist, album)
	print(full)
# Упражнение 8-8.
