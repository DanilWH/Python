import matplotlib.pyplot as plt

x_val = list(range(1, 5001))
y_cubes = [x**3 for x in x_val]

plt.scatter(x_val, y_cubes, c=y_cubes, cmap=plt.cm.viridis, s=5)

plt.title("Cubes", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Cubes of value", fontsize=14)

plt.tick_params(axis='both', labelsize=14)

plt.show()