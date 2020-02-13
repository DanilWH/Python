import matplotlib.pyplot as plt

from random_walk import RandomWalk
# Новые блуждания строятся до тех пор, пока программа остаётся активной.
while True:
	# Построение случайного блуждания и нанесение точек на диаграмму.
	rw = RandomWalk(50000)
	rw.fill_walk()

	# Назначение размера области просмотра.
	plt.figure(dpi=126, figsize=(16, 9)) # (Адаптированно под мой экран.)

	#plt.plot(rw.x_values, rw.y_values, c='blue', linewidth=1, zorder=1)

	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
		edgecolor='none', s=1, zorder=1)

	# Выделение первой и последней точек.
	plt.scatter(0, 0, c='green', edgecolors='none', s=100, zorder=2)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
		s=100, zorder=2)

	# Удаление осей.
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break