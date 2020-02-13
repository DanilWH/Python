from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Finds a code of country."""
    for code, name in COUNTRIES.items():
        if country_name == name:
            return code
    if country_name == 'Egypt, Arab Rep.':
        return 'eg'
    elif country_name == 'Tanzania':
        return 'tz'
    elif country_name == 'Bolivia':
        return 'bo'
    elif country_name == 'Iran, Islamic Rep.':
        return 'ir'
    elif country_name == 'Vietnam':
        return 'vn'
    # if name of country is not found, return None.
    return None