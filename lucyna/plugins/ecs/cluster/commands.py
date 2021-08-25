import click

from ....data_loader import DataLoader
from ....runner import Runner
from ....ui import Ui, make_listing_layout
from .data import fetch_listing
from .layouts import ListingLayout


@click.command(help="List available clusters", name="list")
@click.pass_context
def listing(ctx):
    Runner(Ui(make_listing_layout, ListingLayout, DataLoader(ctx.obj, fetch_listing))).run()
