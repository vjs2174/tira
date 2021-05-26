import click

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
    virtual_machines_list_file = config.files['virtual_machines_list']
    console = config.console
    with console.pager():
        with open(virtual_machines_list_file, 'r') as f:
            console.print(f.read())

