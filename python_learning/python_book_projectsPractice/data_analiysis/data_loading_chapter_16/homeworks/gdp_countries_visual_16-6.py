import json
import pygal

from get_code import get_country_code
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

filename = 'data/gdp_countries_data.json'
with open(filename) as f:
    data_obj = json.load(f)

gdp_countries = {}
for gdp_dict in data_obj:
    if gdp_dict['Year'] == 2015:
        # getting of country name, GDP values and code of current country.
        country_name = gdp_dict['Country Name']
        gdp_value = int(gdp_dict['Value'])
        code = get_country_code(country_name)
        if code:
            gdp_countries[code] = gdp_value

gdp_group1, gdp_group2, gdp_group3, gdp_group4, gdp_group5 = {}, {}, {}, {}, {}
for code, value in gdp_countries.items():
    if value < 50_000_000_000:
        gdp_group1[code] = value
    elif value < 200_000_000_000:
        gdp_group2[code] = value
    elif value < 800_000_000_000:
        gdp_group3[code] = value
    elif value < 1.6 * 10**12:   # 1_600_000_000_000 trillion
        gdp_group4[code] = value
    else:
        gdp_group5[code] = value

wm_style = RS('#336699', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)

wm.title = 'GDP of World'
wm.add('GDP < 50 bn', gdp_group1)
wm.add('GDP < 200 bn', gdp_group2)
wm.add('GDP < 800 bn', gdp_group3)
wm.add('GDP < 1,6 tn', gdp_group4)
wm.add('GDP > 1,6 tn', gdp_group5)

wm.render_to_file('gdp_countries.svg')