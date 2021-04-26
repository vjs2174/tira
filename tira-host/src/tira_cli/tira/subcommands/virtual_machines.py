import click
from rich.__main__ import make_test_card
from rich.console import Console


@click.command()
@click.pass_obj
def vm_create(config):
    click.echo("Creating VM")
    click.echo(type(config))

@click.command()
@click.pass_obj
def vm_start(config):
    click.echo("Starting VM")


@click.command()
@click.pass_obj
def vm_list(config):
    virtual_machines_list = config.files
    console = Console()
    console.print(virtual_machines_list)
    # with console.pager():
        # vms = [f"betaweb{i}\t\tvm_{i%66}\n" for i in range(1000)]
        # console.print(''.join(vms))
