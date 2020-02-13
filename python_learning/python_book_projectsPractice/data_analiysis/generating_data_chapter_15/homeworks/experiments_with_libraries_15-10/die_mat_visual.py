import matplotlib as mat
import matplotlib.pyplot as plt

from die_mat import Die

die_1 = Die()
die_2 = Die(10)

# calculation of data.
sides = [die_1.roll() + die_2.roll() for num in range(100000)]

max_val_side = die_1.num_sides + die_2.num_sides
min_val = 2
values = list(range(min_val, max_val_side+1)) # data 'x'.
frequencies = [sides.count(current_val) for current_val in values] # data 'y'.

for val in values:
	plt.plot([val, val], [0, frequencies[values.index(val)]], linewidth=15,
		color=(0.9, 0.1, 0.1, 0.5))

# giving the graphics a good look.
plt.title("Roll of cube 100,000 item.", fontsize=24)
plt.xlabel("Values of sides cube", fontsize=14)
plt.ylabel("Frequencies of valume cube after roll", fontsize=14)

#plt.xticks([2, 3, 4, 5, 6, 7, 8 ,9, 10, 11, 12, 13, 14, 15, 16])
#plt.yticks([yval for yval in range(0, max(frequencies) + 200, 300)])
plt.axis([0, max_val_side+1,  0, max(frequencies) + max(frequencies) / 10])
plt.show()