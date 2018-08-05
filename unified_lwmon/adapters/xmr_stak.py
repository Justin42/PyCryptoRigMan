from .base_adapter import BaseJsonAdapter, AdapterType


class XmrStakAdapter(BaseJsonAdapter):
    def __init__(self, config):
        self.type = AdapterType.XMR_STAK
        super().__init__(config)

    def parse(self):
        return super().parse()
