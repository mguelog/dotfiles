from os import path
import json


def load_theme():
    with open(path.join(path.expanduser('~'), '.config', 'qtile', 'theme.json'), 'r') as file:
        data = file.read()
        theme = '{}.json'.format(json.loads(data)['theme'])

    with open(path.join(path.expanduser('~'), '.config', 'qtile', 'themes', theme), 'r') as file:
        data = file.read()

    return json.loads(data)


colors = load_theme()
