from enum import Enum
import requests

# Adapter imports
from .xmr_stak import XmrStakAdapter
from .base_adapter import BaseAdapter


class AdapterType(Enum):
    AUTO = 0
    SRB_MINER = 1
    XMR_STAK = 2
    XMR_RIG = 3
    CAST_XMR = 4
    LWMON_API = 5


class AdapterFactory(object):
    typeClasses = {
        AdapterType.SRB_MINER:      None,
        AdapterType.XMR_STAK:       XmrStakAdapter,
        AdapterType.XMR_RIG:        None,
        AdapterType.CAST_XMR:       None,
        AdapterType.RIGMAN_PROXY:   None,
        AdapterType.AUTO:           None,
    }

    @staticmethod
    def detect_type(url) -> AdapterType:
        # TODO implement auto detection
        #data = requests.get(url)
        adapter_type = AdapterType.XMR_STAK
        return adapter_type

    @staticmethod
    def create(adapter_type: AdapterType, config) -> BaseAdapter:
        if adapter_type is AdapterType.AUTO:
            adapter_type = AdapterFactory.detect_type(config['address'])
        # noinspection PyArgumentList
        return BaseAdapter.__new__(AdapterFactory.typeClasses[adapter_type], config)
