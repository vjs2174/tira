import click

from .subcommands.virtual_machines import vm_create, vm_start, vm_list
from .utils import TiraConfig


@click.group(invoke_without_command=True, no_args_is_help=True)
@click.pass_context
@click.option('--debug/--no-debug', default=False)
def cli(context, debug):
    context.obj = TiraConfig()

cli.add_command(vm_create, name='create')
cli.add_command(vm_start, name='start')
cli.add_command(vm_list, name='list')