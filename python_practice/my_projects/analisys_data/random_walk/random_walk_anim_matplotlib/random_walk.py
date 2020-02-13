from random import choice

class RandomWalk():
	def __init__(self, num_points=1000):
		self.num_points = num_points

		self.last_x = 0
		self.last_y = 0

	def get_step(self):
		direction = choice([-1, 1])
		distance = choice(list(range(5)))
		step = direction * distance

		return step

	def take_a_step(self):
		while True:
			x_step = self.get_step()
			y_step = self.get_step()

			if x_step == 0 and y_step == 0:
				continue
			else:
				self.last_x += x_step
				self.last_y += y_step

				break