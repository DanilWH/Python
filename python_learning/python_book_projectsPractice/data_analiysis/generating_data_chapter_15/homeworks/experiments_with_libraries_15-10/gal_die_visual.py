import pygal

from gal_die import Step

gal = pygal.XY(stroke=False)
step = Step(10000)

step.make_steps()
gal.add('Points', step.coor_points)
gal.render_to_file('rw_gal_visual.svg')