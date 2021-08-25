from enum import Enum

from rich.table import Table

from ....ui import BaseListingLayout, LucynaPanel, StatusEnum


class ClusterStatusEnum(Enum):
    ACTIVE = StatusEnum.ACTIVE.value
    PROVISIONING = StatusEnum.IN_PROGRESS.value
    DEPROVISIONING = StatusEnum.IN_PROGRESS.value
    FAILED = StatusEnum.STOPPED.value
    INACTIVE = StatusEnum.STOPPED.value


class ListingLayout(BaseListingLayout):
    def header(self):
        grid = Table.grid(expand=True)
        grid.add_column(justify="left", ratio=1)
        grid.add_row(f"Clusters")

        return LucynaPanel(grid)

    def main(self):
        table = Table()

        table.add_column("Cluster name")
        table.add_column("Status")
        table.add_column("Running tasks")
        table.add_column("Pending tasks")
        table.add_column("Active services")

        for cluster in self.data.fetcher:
            status = ClusterStatusEnum[cluster["status"]].value

            table.add_row(
                cluster["clusterName"],
                f"[{status.colour}]{status.icon}[/{status.colour}]  ({cluster['status'].lower()})",
                str(cluster["runningTasksCount"]),
                str(cluster["pendingTasksCount"]),
                str(cluster["activeServicesCount"]),
            )

        return table
