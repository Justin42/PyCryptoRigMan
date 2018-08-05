from .base_adapter import BaseJsonAdapter


class XmrStakAdapter(BaseJsonAdapter):
    def __init__(self, config):
        super().__init__(config)

    def _parse_(self):
        return
