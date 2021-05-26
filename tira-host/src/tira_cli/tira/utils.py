from configparser import ConfigParser, ExtendedInterpolation
from pkg_resources import resource_filename #access package resources
from rich.console import Console
from rich.theme import Theme
from random import choice

class TiraConfig(object):
    def __init__(self, tira_config_file='config/tira.cfg', **kwargs):
        TIRA_CONFIG_PATH = resource_filename(__name__, tira_config_file)
        tira_config_parser = ConfigParser(interpolation=ExtendedInterpolation())
        tira_config_parser.read(TIRA_CONFIG_PATH)
        self.files = dict(tira_config_parser.items('FILES'))
        self.console = Console(theme=Theme.read(TIRA_CONFIG_PATH), **kwargs)

def generate_nickname(adjectives_files='config/adjectives.txt', animals_files='config/animals.txt'):
    f_adjectives = resource_filename(__name__, adjectives_files)
    f_animals = resource_filename(__name__, animals_files)
    with open(f_adjectives, 'r') as f:
        adjectives = f.read().splitlines()
    with open(f_animals, 'r') as f:
        animals = f.read().splitlines()
    return f"{choice(adjectives)} {choice(animals)}"