from flask import Flask, jsonify
from flask_classy import FlaskView

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


class ProxiesView(FlaskView):
    def list(self):
        response = [{'proxy': {'name': 'test_proxy'}}]
        return jsonify(response)


ProxiesView.register(app, route_prefix='/api/')
if __name__ == '__main__':
    app.run()
