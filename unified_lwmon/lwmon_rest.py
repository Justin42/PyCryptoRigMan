from flask import Flask
from .api import Rig, RigMonitor
from .views import RigsView

app = Flask(__name__)


@app.route('/')
def home():
    return 'Unified Lightweight Monitor'


@app.route('/refresh')
def refresh():
    return ''


if __name__ == '__main__':
    rigMon = RigMonitor()

    RigsView.register(app, route_prefix='/api/')
    app.run()
