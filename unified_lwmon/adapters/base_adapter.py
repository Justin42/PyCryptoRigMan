from enum import Enum

class AdapterType(Enum):
    SRB_MINER = 0
    XMR_STAK = 1

class BaseAdapter(object):
    def __init__(self, type):
        self.type = type



