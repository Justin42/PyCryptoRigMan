from flask import Flask, jsonify
from flask_classy import FlaskView
import yaml

class RigsView(FlaskView):
    def list(self):
        response = [{'rigs': {'name': 'local'}}]
        return jsonify(response)