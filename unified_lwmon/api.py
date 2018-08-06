from flask import Flask, jsonify
from flask_classy import FlaskView
import yaml

from .adapters.adapter_factory import AdapterFactory, AdapterType


class Rig(object):
    def __init__(self, config):
        self.data = dict()
        self.config = config
        adapter_type = AdapterType.__getattr__(str(self.config['adapter']).upper())
        self.adapter = AdapterFactory.create(adapter_type, self.config)

        # Function wrappers
        self.hashrate = self.adapter.get_hashrate
        self.refresh = self.adapter.refresh


class RigMonitor(object):
    def __init__(self):
        self.rigs = []

    def add_rig(self, rig):
        self.rigs.append(rig)

    def refresh(self):
        for rig in self.rigs:
            rig.refresh()

    def hashrate(self) -> int:
        hashrate = 0
        for rig in self.rigs:
            hashrate += rig.hashrate()
        return hashrate
