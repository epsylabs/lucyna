import click
from rich.console import Console

from .context import ContextObject
from .plugins import cluster, dashboard, service, task


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = ContextObject()


def safe_cli():
    """
    Used as an entry point in pyproject.toml::tool.poetry.scripts
    To handle global exceptions.
    """
    try:
        cli()
    except Exception as e:
        console = Console()

        if type(e).__qualname__ == "ClusterNotFoundException":
            # Handle botocore.errorfactory.ClusterNotFoundException exception
            console.print(
                "Cluster not found. To list available clusters run: ecs cluster list",
                style="bold red",
            )
            return

        raise


cli.add_command(cluster.cli)
cli.add_command(dashboard.cli)
cli.add_command(service.cli)
cli.add_command(task.cli)


if __name__ == "__main__":
    cli()
