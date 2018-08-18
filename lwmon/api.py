from .adapters.adapter_factory import AdapterFactory, AdapterType
from .exchanges.exchange import *
from abc import ABC, abstractmethod


class Rig(object):
    def __init__(self, config):
        self.data = dict()
        self.config = config
        adapter_type = AdapterType.__getattr__(str(self.config['adapter']).upper())
        self.adapter = AdapterFactory.create(adapter_type, self.config)

        # Function wrappers
        self.stats = dict()

    def update(self):
        self.adapter.refresh()
        self.stats = {
            'name': self.config['name'],
            'alias': self.config.get('alias'),
            'address': self.config['address'],
            'adapter': self.config['adapter'],
            'hashrate': self.adapter.get_hashrate(),
            'extras': self.adapter.get_extras()
        }

    def __str__(self):
        return self.stats


class Monitor(ABC):
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def load_config(self, config: dict):
        pass


class RigMonitor(Monitor):
    def __init__(self, config=None):
        if config is None:
            self.config = dict()
        else:
            self.load_config(config)
        self.rigs = []
        self.stats = dict()

    def add_rig(self, rig):
        print("Added rig '{0}'".format(rig.config['name']))
        self.rigs.append(rig)

    def update(self):
        stats = dict()
        stats['rigs'] = []
        stats['hashrate'] = 0
        for rig in self.rigs:
            rig.update()
            stats['rigs'].append(rig.stats)
            stats['hashrate'] += rig.stats['hashrate']
        self.stats = stats

    def load_config(self, config: dict):
        self.config = config
        rigs = self.config['lwmon']['rigs']
        print(config)
        for rig_conf in rigs:
            rig = Rig(rig_conf)
            self.add_rig(rig)


class PriceMonitor(Monitor):
    def __init__(self, config=None):
        self.exchanges = []
        if config is None:
            self.config = dict()
        else:
            self.config = config

    def add_exchange(self, exchange: Exchange):
        self.exchanges.append(exchange)

    def load_config(self, config: dict):
        pass

    def update(self):
        for exchange in self.exchanges:
            exchange.update()
