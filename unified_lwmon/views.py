from flask import Flask, jsonify
from flask_classy import FlaskView


class RigsView(FlaskView):
    def list(self):
        response = [{'rigs': {'name': 'local'}}]
        return jsonify(response)


class WebInterface(FlaskView):
    def __init__(self):
        return
