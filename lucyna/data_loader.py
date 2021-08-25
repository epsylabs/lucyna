from dataclasses import dataclass

from .context import ContextObject


@dataclass
class Data:
    click_params: dict
    fetcher: dict


class DataLoader:
    def __init__(self, context: ContextObject, data_fetcher, click_params=None):
        self.context = context
        self.data_fetcher = data_fetcher
        self.click_params = click_params

    def fetch_data(self):
        return Data(self.click_params, self.data_fetcher(self.context, self.click_params))
