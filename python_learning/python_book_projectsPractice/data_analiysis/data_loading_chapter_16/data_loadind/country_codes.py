from pygal.maps.world import COUNTRIES
def get_country_code(country_name):
    """Возвращает для заданной страны её код Pygal, состоящий из 2 букв."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    if country_name == 'American Samoa':
        return 'as'
    elif country_name == 'Antigua and Barbuda':
        return 'ag'
    elif country_name == 'Aruba':
        return 'aw'
    elif country_name == 'Barbados':
        return 'bb'
    elif country_name == 'Bermuda':
        return 'bm'
    elif country_name == 'Bolivia':
        return 'bo'
    elif country_name == 'Cayman Islands':
        return 'ky'
    elif country_name == 'Comoros':
        return 'km'
    elif country_name == 'Curacao':
        return 'cw'
    elif country_name == 'Dominica':
        return 'dm'
    elif country_name == 'Egypt, Arab Rep.':
        return 'eg'
    elif country_name == 'Faeroe Islands':
        return 'fo'
    elif country_name == 'Fiji':
        return 'fg'
    elif country_name == 'French Polynesia':
        return 'pf'
    elif country_name == 'Gambia, The':
        return 'gm'
    elif country_name == 'Gibraltar':
        return 'gi'
    elif country_name == 'Grenada':
        return 'gd'
    elif country_name == 'Hong Kong SAR, China':
        return 'hk'
    elif country_name == 'Iran, Islamic Rep.':
        return 'ir'
    elif country_name == 'Isle of Man':
        return 'im'
    # Если страна не найдена, вернуть None.
    return None

# Всё что ниже убрать после отладки!!!!!!
if __name__ == '__main__':
    for code, name in sorted(COUNTRIES.items()):
        print(f'{code}: {name}')