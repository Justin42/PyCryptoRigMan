from enum import Enum
import urllib, json


class AdapterType(Enum):
    SRB_MINER = 0
    XMR_STAK = 1
    XMR_RIG = 2
    CAST_XMR = 3
    RIGMAN_PROXY = 4


class BaseAdapter(object):
    def __init__(self, config):
        self.config = config
        self.data_raw = dict()
        self.data_parsed = dict()

    def get_raw(self):
        return self.data_raw

    def get_parsed(self):
        return self.data_parsed

    def parse(self):
        return NotImplementedError("API adapter seems invalid. BaseAdapter.parse not implemented.")

    def refresh(self):
        return NotImplementedError("API adapter seems invalid. BaseAdapter.refresh not implemented.")


class BaseJsonAdapter(BaseAdapter):
    def __init__(self, config):
        super().__init__(config)

    def refresh(self):
        return