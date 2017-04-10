import json
from flask import jsonify
from flask import request
from helpers import write_log
from flask_cors import CORS
from functions import get_key
from functions import set_key
from functions import mod_key
from functions import del_key
from flask_with_defaults import FlaskWithDefaults


config = json.load(open('config.json'))

app = FlaskWithDefaults(__name__)
CORS(app)


@app.route('/kvs', defaults={'key': None})
@app.route('/kvs/<key>')
def add_key(key):
    response = 'Unsupported HTTP method', 501

    if key is None or key == '':
        response = 'You need to send a key', 500

    if request.method in ['POST', 'PUT'] and (request.data is None or request.data == ''):
        response = 'You need to send a value', 500

    if response[1] != 500:
        if request.method == 'GET':
            response = get_key(key)
        if request.method == 'POST':
            response = set_key(key, request.data)
        if request.method == 'PUT':
            response = mod_key(key, request.data, config['strict_modify'])
        if request.method == 'DELETE':
            response = del_key(key, config['strict_delete'])

    write_log(key, request, response)

    return response


if __name__ == '__main__':
    app.run(host=config['host'], port=config['port'], threaded=config['threaded'], debug=config['debug'])