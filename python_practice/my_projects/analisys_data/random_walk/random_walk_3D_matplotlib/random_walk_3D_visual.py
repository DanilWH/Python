from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from get_step import RandomWalk

fig = plt.figure(dpi=128, figsize=(10, 8))
ax = fig.gca(projection='3d')
rm = RandomWalk()
rm.get_steps_walk()

cm_list = [val for val in range(rm.num_steps)]
ax.scatter(rm.x_steps, rm.y_steps, rm.z_steps, c=cm_list, cmap=plt.cm.Blues,
    alpha=1)

plt.show()