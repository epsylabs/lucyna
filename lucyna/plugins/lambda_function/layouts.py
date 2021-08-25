import arrow
from rich.table import Table

from ... import DATE_FORMAT
from ...ui import BaseListingLayout, LucynaPanel


class ListingLayout(BaseListingLayout):
    def header(self):
        grid = Table.grid(expand=True)
        grid.add_column(justify="left", ratio=1)
        region = "All regions" if not self.data.click_params["region"] else self.data.click_params["region"]
        grid.add_row(f"Lambdas > {region}")

        return LucynaPanel(grid)

    def main(self):
        table = Table()
        table.add_column("Name")
        table.add_column("Runtime")
        table.add_column("Timeout")
        table.add_column("Memory size")
        table.add_column("Last modified")
        table.add_column("Description")

        for functions in self.data.fetcher:
            for lambda_function in functions:
                table.add_row(
                    lambda_function["FunctionName"],
                    lambda_function["Runtime"],
                    str(lambda_function["Timeout"]),
                    str(lambda_function["MemorySize"]),
                    arrow.get(lambda_function["LastModified"]).format(DATE_FORMAT),
                    lambda_function["Description"],
                )

        return table
