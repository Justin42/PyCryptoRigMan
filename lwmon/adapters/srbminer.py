from .base_adapter import BaseJsonAdapter


class SrbMinerAdapter(BaseJsonAdapter):
    def get_hashrate(self) -> int:
        total_hashrate = 0
        for device in self.data_raw['devices']:
            total_hashrate += device['hashrate']
        return total_hashrate
