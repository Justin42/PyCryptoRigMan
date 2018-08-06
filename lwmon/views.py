from flask import Flask, jsonify, current_app
from flask_classy import FlaskView
from .api import RigMonitor


class RigsView(FlaskView):
    def index(self):
        return self.list()

    def list(self):
        monitor = current_app.lwmon['monitor']
        monitor.update_stats()
        return jsonify(monitor.stats)


class WebInterface(FlaskView):
    def __init__(self):
        return
