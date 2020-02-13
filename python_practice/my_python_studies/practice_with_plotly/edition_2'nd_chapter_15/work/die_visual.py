from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

die_1 = Die()
die_2 = Die()

results = [die_1.get_side() + die_2.get_side() for val in range(1000)]

sum_sides = die_1.num_sides + die_2.num_sides
frequensies = [results.count(side) for side in range(2, sum_sides+1)]

# Visualize the results.
x_values = list(range(2, sum_sides+1))
data = [Bar(x=x_values, y=frequensies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling D6 1000 times',
    xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')