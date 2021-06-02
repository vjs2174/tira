import click
from rich.table import Table

@click.command()
@click.pass_obj
def vm_create(config):
    click.echo("Creating VM")
    pass

@click.command()
@click.pass_obj
def vm_start(config):
    click.echo("Starting VM")
    pass

@click.command()
@click.pass_obj
def vm_list(config):
    virtual_machines_list_file = config.files['virtual_machines_list']
    console = config.console
    with open(virtual_machines_list_file, 'r') as f:
        vms = f.readlines()
    vms = [entry.split() for entry in vms]
    table = Table(title="TIRA Hosts")
    table.add_column("Host", justify="center", no_wrap=True)
    table.add_column("Virtual Machine", justify="center")
    table.add_column("State", justify="center")
    for vm in vms:
        if len(vm)==2:
            table.add_row(*vm)
        else:
            table.add_row(*vm[:3])
    with console.pager():
        console.print(table)