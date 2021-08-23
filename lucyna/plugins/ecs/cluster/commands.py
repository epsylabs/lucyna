import click

from ....data_loader import DataLoader
from ..cluster.data import fetch_listing
from ..cluster.layouts import ListingLayout
from ....runner import Runner
from ....ui import Ui, make_layout


@click.command(help="List available clusters", name="list")
@click.pass_context
def listing(ctx):
    Runner(Ui(make_layout, ListingLayout, DataLoader(ctx.obj, fetch_listing))).run()
