import csv
import pygal

from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS
from get_code_surface import get_code_country

# reading of data from file.
filename = 'data/surface_sqr_countries.csv'
with open(filename) as f:
    reader_obj = csv.reader(f)
    for i in range(4):
        next(reader_obj)
    headers = next(reader_obj)
    print(headers)

    #saving of data in dict/
    c_squares = {}
    for row in reader_obj:
        c_name = row[0]
        code = get_code_country(c_name)
        try:
            area = int(float(row[-3]))
        except:
            print(f'{c_name}: no data')
        else:
            if code:
                c_squares[code] = area
            else:
                print(f'{c_name}: not found.')    # } remove after debug!!!

# distribution of countries by the groups.
country_group1, country_group2, country_group3 = {}, {}, {}
for code, area in c_squares.items():
    if area < 500_000:
        country_group1[code] = area
    elif area < 2_000_000:
        country_group2[code] = area
    else:
        country_group3[code] = area

# application of a style to the graph.
wm_style = RS('#228B22', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'Square countries of the world\nSurface area (sq. km)'
# the construction of the graph.
wm.add('Area < 500,000', country_group1)
wm.add('Area < 2 ml', country_group2)
wm.add('Area > 2 ml', country_group3)

wm.render_to_file('area_counrties.svg')
