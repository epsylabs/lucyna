import click

from .cluster import cli as cluster_cli
from .service import cli as service_cli
from .task import cli as task_cli


@click.group(name="ecs")
def cli():
    """
    ECS [cluster, service, task]
    """


cli.add_command(cluster_cli)
cli.add_command(service_cli)
cli.add_command(task_cli)
