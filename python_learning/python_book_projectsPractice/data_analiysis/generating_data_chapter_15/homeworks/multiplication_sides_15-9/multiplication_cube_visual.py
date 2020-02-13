import pygal

from cube import Cube

cube_1 = Cube()
cube_2 = Cube()

# get result of roll.
side_values = [cube_1.roll() * cube_2.roll() for i in range(1000000)]

min_side_val = 1
max_side_val = cube_1.num_sides * cube_2.num_sides

# count frequencies of result of roll.
frequencies = [side_values.count(val)
	for val in range(min_side_val, max_side_val+1)]

gl = pygal.Bar()

gl.title = "Multiplication of result sides cubes"
gl.x_labels = [str(x) for x in range(min_side_val, max_side_val+1)]
gl.x_title = "Values of sides a cube"
gl.y_title = "Frequencies of rolls values"

gl.add('D6 * D6', frequencies)
gl.render_to_file('multiplication_visualisation.svg')