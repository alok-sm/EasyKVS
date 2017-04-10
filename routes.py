import json
from flask import jsonify
from flask import request
from helpers import write_log
from flask_cors import CORS
from function_defs import Functions
from flask_with_defaults import FlaskWithDefaults


config = json.load(open('config.json'))

functions = Functions(config['storage_file'])
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
            response = functions.get_key(key)
        if request.method == 'POST':
            response = functions.set_key(key, request.data)
        if request.method == 'PUT':
            response = functions.mod_key(key, request.data, config['strict_modify'])
        if request.method == 'DELETE':
            response = functions.del_key(key, config['strict_delete'])

    write_log(key, request, response)

    return response


if __name__ == '__main__':
    app.run(host=config['host'], port=config['port'], threaded=config['threaded'], debug=config['debug'])