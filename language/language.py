# DICTIONARY


def get_language_id(language_var):
    if language_var == 'en':
        return 0
    elif language_var == 'pl':
        return 1


ui_strings = {'table': ('table', 'stolik'),
              'discount': ('discount', 'zniżka'),
              'bulk?': ('bulk?', 'na wagę?'),
              'code': ('code', 'kod'),
              'name': ('name', 'nazwa'),
              'type': ('type', 'typ'),
              'count': ('count', 'ilość'),
              'price per piece': ('for piece', 'cena/szt.'),
              'price': ('price', 'cena'),
              'discounted': ('discounted', 'po zniżce'),
              'comments': ('comments', 'uwagi'),
              'sum': ('sum', 'suma')}

type_list = ['', 'sztuka', 'czajnik', 'gaiwan', 'gram', 'opakowanie']
