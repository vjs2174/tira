from configparser import ConfigParser, ExtendedInterpolation
from pkg_resources import resource_filename

import click

from .subcommands.virtual_machines import create, start, list_vms

TIRA_CONFIG = resource_filename(__name__,'tira.cfg')
tira_config = ConfigParser(interpolation=ExtendedInterpolation())
tira_config.read(TIRA_CONFIG)


@click.group(invoke_without_command=True)
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    pass
cli.add_command(create)
cli.add_command(start)
cli.add_command(list_vms)