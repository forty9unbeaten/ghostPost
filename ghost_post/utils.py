from string import ascii_lowercase
from random import choice

post_filters = [
    {
        'value': 'all',
        'display': 'All'
    },
    {
        'value': 'boasts',
        'display': 'Boasts'
    },
    {
        'value': 'roasts',
        'display': 'Roasts'
    }
]

post_sorters = [
    {
        'value': 'created',
        'display': 'Creation Date'
    },
    {
        'value': 'score',
        'display': 'Vote Score/Total'
    }
]


def generate_secret_id():
    return ''.join(choice(ascii_lowercase) for i in range(6))
