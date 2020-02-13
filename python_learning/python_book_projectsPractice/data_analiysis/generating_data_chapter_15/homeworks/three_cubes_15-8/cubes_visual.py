import pygal

from die_cube import Die

cube_1 = Die()
cube_2 = Die()
cube_3 = Die()

results = [cube_1.roll() + cube_2.roll() + cube_3.roll()
	for num_roll in range(1000000)]

max_val = cube_1.num_sides + cube_2.num_sides + cube_3.num_sides
min_val = 3

frequencies = [results.count(val) for val in range(min_val, max_val+1)]

gal = pygal.Bar()

gal.title = "Three cubes"
gal.x_labels = [str(x) for x in range(min_val, max_val+1)]
gal.x_title = "Values of cubes"
gal.y_title = "Frequence of Values"

gal.add('D' + str(cube_1.num_sides) +
	' + D' + str(cube_2.num_sides) +
	' + D' + str(cube_3.num_sides),
	frequencies)
gal.render_to_file('visual.svg')