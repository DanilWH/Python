def show_magicans(name_magicans_list):
	for name_magicans in name_magicans_list:
		print(name_magicans.title())


def make_great(name_magicans_list):
	while name_magicans_list:
		great_magican = name_magicans_list.pop()
		
		print("Great " + great_magican.title())
		name_magicans_great.append(great_magican)

name_magicans_list = ['danil', 'galya', 'dasha', 'anya', 'zarina']
name_magicans_great = []

print("1")
show_magicans(name_magicans_list)

print("2")
make_great(name_magicans_list[:])

print("3")
show_magicans(name_magicans_list)
# Упражнения 8-9, 8-10, 8-11.
