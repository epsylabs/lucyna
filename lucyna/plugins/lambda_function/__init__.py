import click

from .commands import listing


@click.group(name="lambda")
def cli():
    """
    Lambda [listing]
    """


cli.add_command(listing)
