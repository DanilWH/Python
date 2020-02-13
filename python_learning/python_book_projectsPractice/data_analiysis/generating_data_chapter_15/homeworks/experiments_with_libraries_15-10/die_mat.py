from random import randint

class Die():
	def __init__(self, num_sides=6):
		self.num_sides = num_sides

	def roll(self):
		"""Returns side of cube."""
		return randint(1, self.num_sides)