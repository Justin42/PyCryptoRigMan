from abc import ABC, abstractmethod
import requests


class BaseAdapter(ABC):
    def __init__(self, config):
        self.config = config
        self.data_raw = dict()
        self.data_parsed = dict()

    def get_raw(self):
        return self.data_raw

    @abstractmethod
    def refresh(self):
        return NotImplementedError("API adapter seems invalid. 'refresh' not implemented.")

    @abstractmethod
    def get_hashrate(self) -> int:
        NotImplementedError("API adapter seems invalid. 'get_hashrate' not implemented.")
        return 0

    @abstractmethod
    def get_extras(self) -> dict:
        return dict()


class BaseJsonAdapter(BaseAdapter, ABC):
    def refresh(self):
        print("Refreshing stats for rig '{0}'".format(self.config['name']))
        self.data_raw = requests.get(self.config['address']).json()
        print(self.data_raw)
