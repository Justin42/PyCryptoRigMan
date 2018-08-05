from flask import Flask, jsonify
from flask_classy import FlaskView
import yaml

from .adapters.base_adapter import AdapterType


class Rig(object):
    def __init__(self, config):
        self.data = dict()
        self.config = config
        self._init_adapter_(self.config['type'])

    def _init_adapter_(self, type):
        type = AdapterType[type]

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