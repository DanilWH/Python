import matplotlib.pyplot as plt
import numpy as np

PI = 3.14
# заполнение значений x оси.
x_data = []
# заполнение y оси.
y_data = []

# Назначение заголовка диаграммы и меток осей.
plt.title("Sinus", fontsize=24)
plt.xlabel("sin", fontsize=20)
plt.ylabel("cos", fontsize=20)

#Назначение размера шрифта и делений на осях.
plt.tick_params(axis='both', labelsize=14)
# Назначение диапазона для каждой оси.
#plt.axis([-40, 40, 0, 500])

for x in np.arange(PI, PI * 5, 0.1):
	x = round(x, 4)
	x_data.append(x)
	y_data.append(round(np.sin(x), 4))

	plt.scatter(x_data, y_data, edgecolor='none', c=y_data,
		cmap=plt.cm.RdYlGn, s=40)
	plt.pause(0.01)

plt.show()