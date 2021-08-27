import click

from .commands import listing


@click.group(name="cluster")
def cli():
    """
    Cluster [list]
    """


cli.add_command(listing)
