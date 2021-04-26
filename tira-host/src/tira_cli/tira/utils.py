from configparser import ConfigParser, ExtendedInterpolation
from pkg_resources import resource_filename #access package resources

class TiraConfig(object):
    def __init__(self, tira_config_file='tira.cfg'):
        TIRA_CONFIG_PATH = resource_filename(__name__, tira_config_file)
        tira_config_parser = ConfigParser(interpolation=ExtendedInterpolation())
        tira_config_parser.read(TIRA_CONFIG_PATH)
        self.files = dict(tira_config_parser.items('FILES'))

# print(tira_config.get('ROOT', 'mountpoint'))
# print(tira_config.items('FILES'))