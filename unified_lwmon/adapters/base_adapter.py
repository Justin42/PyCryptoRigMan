import requests


class BaseAdapter(object):
    def __init__(self, config):
        self.config = config
        self.data_raw = dict()
        self.data_parsed = dict()

    def get_raw(self):
        return self.data_raw

    def get_parsed(self):
        return self.data_parsed

    def _parse_(self):
        return NotImplementedError("API adapter seems invalid. BaseAdapter.parse not implemented.")

    def refresh(self):
        return NotImplementedError("API adapter seems invalid. BaseAdapter.refresh not implemented.")


class BaseJsonAdapter(BaseAdapter):
    def __init__(self, config):
        super().__init__(config)

    def refresh(self):
        self.data_raw = requests.get(self.config['address'])
        self._parse_()