from flask import Flask, jsonify
from flask_classy import FlaskView
import yaml

from .adapters.adapter_factory import AdapterFactory, AdapterType


class Rig(object):
    def __init__(self, config):
        self.data = dict()
        self.config = config
        adapter_type = AdapterType.__getattr__(self.config['adapter'])
        self.adapter = AdapterFactory.create(adapter_type, self.config)

    def refresh(self):

        return


class RigMonitor(object):
    def __init__(self):
        self.rigs = []

    def add_rig(self, rig):
        self.rigs.append(rig)

    def refresh(self):
        for rig in self.rigs:
            rig.refresh()
