import pygal

from die import Die

dice = []

num_dies = int(input("How many dice do you have?: "))

for curr_die in range(num_dies):
	num_sides = int(input("How many sides your " +
		str(curr_die+1) + " cube?: "))
	die = Die(num_sides)
	dice.append(die)

how_many_rolls = int(input("How many rolls do you want to do?: "))

while True:
	results = [sum([die.roll() for die in dice])
		for num_roll in range(how_many_rolls)]

	max_val = sum([die.num_sides for die in dice])
	min_val = num_dies
	frequencies = [results.count(val) for val in range(min_val, max_val+1)]

	gal = pygal.Bar()
	gal.x_labels = [str(val) for val in range(min_val, max_val+1)]
	gal.add('Your ' + str(len(dice)) + ' cubes', frequencies)
	gal.render_to_file('inter_roll.svg')
	print("Your file is ready!")

	answer = input("Repeat?(y/n): ").lower()
	if answer == 'n':
		break