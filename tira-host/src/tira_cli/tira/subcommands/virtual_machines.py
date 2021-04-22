import click
from rich.__main__ import make_test_card
from rich.console import Console


@click.command()
def create():
    click.echo("Creating VM")
    import socket
    click.echo(socket.getfqdn())

@click.command()
def start():
    click.echo("Starting VM")


@click.command(name='list')
def list_vms():
    console = Console()
    with console.pager():
        vms = [f"betaweb{i}\t\tvm_{i%66}\n" for i in range(1000)]
        console.print(''.join(vms))
