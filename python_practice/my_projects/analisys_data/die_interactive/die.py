from random import randint

class Die():
	def __init__(self, num_sides):
		self.num_sides = num_sides

	def roll(self):
		"""Returns a side of cube."""
		return randint(1, self.num_sides)