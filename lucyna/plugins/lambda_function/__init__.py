import click

from .commands import listing


@click.group(name="lambda")
def cli():
    """
    Lambda [list]
    """


cli.add_command(listing)
