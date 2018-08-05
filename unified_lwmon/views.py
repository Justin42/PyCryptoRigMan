from flask import Flask, jsonify
from flask_classy import FlaskView
from .api import RigMonitor


class RigsView(FlaskView):
    def __init__(self, monitor: RigMonitor):
        super().__init__()
        self.monitor = monitor

    def list(self):
        response = [{'rigs': {'name': 'local'}}]
        return jsonify(response)


class WebInterface(FlaskView):
    def __init__(self):
        return
