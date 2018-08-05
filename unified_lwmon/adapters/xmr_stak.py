from json import json
from .base_adapter import BaseJsonAdapter


class XmrStakAdapter(BaseJsonAdapter):
    def __init__(self, config):
        super().__init__(config)

    def get_hashrate(self) -> int:
        return self.data_raw['hashrate']['total'][0]
