import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk()

discret_color = 1 / (rw.num_points / 2)
R, G, B = 1, 1, 1

plt.title("Random Walk Animation", fontsize=24)
plt.axis([-150, 150, -150, 150])
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

current_point = 0
while current_point <= rw.num_points:

	plt.scatter(rw.last_x, rw.last_y, color=(R, G, B), edgecolor='none', s=25)
	rw.take_a_step()

	plt.pause(0.000001)
	current_point += 1

	R -= discret_color
	G -= discret_color
	R, G = round(R, len(str(discret_color % 1))), round(G, len(str(discret_color % 1)))

	if R <= 0 and G <= 0:
		R = 0
		G = 0
		B -= discret_color
		B = round(B, len(str(discret_color % 1)))
		if B < 0:
			B = 0

plt.show()