from flask import Flask, jsonify
from flask_classy import FlaskView
import yaml


class Rig(object):
    def __init__(self, config):
        self.data = dict()
        self.data['config'] = config
        return

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