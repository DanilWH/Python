import matplotlib.pyplot as plt

x_values = list(range(-1000, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
	edgecolor='none', s=40)

# Назначение заголовка диаграммы и меток осей.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Назначение размера шрифта и делений на осях.
#plt.tick_params(axis='both', which='major', labelsize=5)

# Назначение диапазона для каждой оси.
plt.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot.png', bbox_inches='tight') # Автоматически сохраняет фото диаграммы с именем, которое указано в первом аргументе и с расширением. Второй аргумент отсекает от диаграммы лишние пропуски. Сохраняется в каталоге с scatter_squares.
plt.show() # отображает график в окне.