from flask import Flask, current_app
from .views import RigsView
from .api import Rig, RigMonitor
import yaml

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/')
def home():
    return 'Universal Lightweight Monitor'


with app.app_context():
    current_app.lwmon = dict()
    monitor = RigMonitor()
    with open('lwmon/config.yml') as file:
        config = yaml.safe_load(file)
    monitor.load_config(config)
    current_app.lwmon['monitor'] = monitor
RigsView.register(app)

if __name__ == '__main__':
    app.run()
