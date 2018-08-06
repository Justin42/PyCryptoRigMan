from .base_adapter import BaseJsonAdapter


class XmrStakAdapter(BaseJsonAdapter):
    def get_hashrate(self) -> int:
        return self.data_raw['hashrate']['total'][0]

    def get_extras(self) -> dict:
        return dict()