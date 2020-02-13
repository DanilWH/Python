import pygal
import numpy as np

XLIM = 0.2

def f(x):
    return 1 / x

scatter = pygal.XY()
for row in range(-1, 2, 2):
    pointsx = []
    pointsy = []
    for x in np.arange(XLIM, f(XLIM), 0.01):
        x = x * row
        y = f(x)
        pointsx.append((x, y))
        pointsy.append((y * -1, x))

    scatter.add('f(x)', pointsx)
    scatter.add('x(f)', pointsy)

scatter.render_to_file('f(x).svg')