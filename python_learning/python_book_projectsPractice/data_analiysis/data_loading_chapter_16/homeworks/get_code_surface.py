from pygal.maps.world import COUNTRIES

def get_code_country(c_name):
    """Gets a code of current country."""
    for code, name in COUNTRIES.items():
        if name == c_name:
            return code
    if c_name == 'Egypt, Arab Rep.':
        return 'eg'
    elif c_name == 'Yemen, Rep.':
        return 'ye'
    elif c_name == 'Bolivia':
        return 'bo'
    elif c_name == 'Vietnam':
        return 'vn'
    elif c_name == 'Libya':
        return 'ly'
    elif c_name == 'Venezuela, RB':
        return 've'
    elif c_name == 'Tanzania':
        return 'tz'
    elif c_name == 'Congo, Dem. Rep.':
        return 'cd'
    elif c_name == 'Korea, Rep.':
        return 'kr'
    elif c_name == 'Iran, Islamic Rep.':
        return 'ir'
    elif c_name == 'Kyrgyz Republic':
        return 'kg'
    # if country name was not found.
    return None