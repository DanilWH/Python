from random import choice

class Step():
	def __init__(self, num_points=10000):
		self.num_points = num_points
		# array with coordination of points.
		self.coor_points = [(0, 0)]

	def get_step(self):
		"""Gets a step."""
		direction = choice([-1, 1])
		distance = choice([0, 1, 2, 3, 4])
		step = direction * distance
		return step

	def make_steps(self):
		"""Adds steps in array 'coor_points'."""

		# while length of 'coor_points' is smaller than 'num_points' do cycle.
		while len(self.coor_points) <= self.num_points:
			x_step = self.get_step()
			y_step = self.get_step()

			if x_step == 0 and y_step == 0:
				continue

			next_x = self.coor_points[-1][0] + x_step
			next_y = self.coor_points[-1][-1] + y_step

			coor_one_point = (next_x, next_y)
			self.coor_points.append(coor_one_point)