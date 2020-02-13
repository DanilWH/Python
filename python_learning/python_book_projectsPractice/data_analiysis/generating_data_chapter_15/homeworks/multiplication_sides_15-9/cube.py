import random

class Cube():
	def __init__(self, num_sides=6):
		self.num_sides = num_sides

	def roll(self):
		"""Returns a value of side cube."""
		return random.randint(1, self.num_sides)
