import click

from ...data_loader import DataLoader
from ...runner import Runner
from ...ui import Ui, make_listing_layout
from .data import fetch_listing
from .layouts import ListingLayout


@click.command(help="List available functions", name="list")
@click.option("--region", type=str, help="Region e.g. us-east-2")
@click.pass_context
def listing(ctx, **kwargs):
    Runner(Ui(make_listing_layout, ListingLayout, DataLoader(ctx.obj, fetch_listing, kwargs))).run()
