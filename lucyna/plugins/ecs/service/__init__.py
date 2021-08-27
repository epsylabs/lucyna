import click

from .commands import dashboard, listing


@click.group(name="service")
def cli():
    """
    Service [list, dashboard]
    """


cli.add_command(listing)
cli.add_command(dashboard)
