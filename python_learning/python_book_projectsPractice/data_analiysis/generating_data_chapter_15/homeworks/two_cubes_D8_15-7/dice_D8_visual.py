import pygal

from die import Die

# create of cubes.
die_1 = Die()
die_2 = Die()

sum_side_random = [die_1.roll_cube() + die_2.roll_cube()
	for num_roll in range(1000000)]

max_val_cubes = die_1.num_sides + die_2.num_sides
frequencies = [sum_side_random.count(value)
	for value in range(2, max_val_cubes+1)]

gal = pygal.Bar()

# the design of appearance.
gal.title = "Analysis of two cubes."
gal.x_labels = [str(label) for label in range(2, max_val_cubes+1)]
gal.x_title = "Values of sides cube."
gal.y_title = "Frequencies of occurrence sides cubes."

# add analysis in graph.
gal.add('D8 + D8', frequencies)
gal.render_to_file('graph_of_frequencies.svg')