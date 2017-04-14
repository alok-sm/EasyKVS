import json
from flask import jsonify
from flask import request
from helpers import write_log
from flask_cors import CORS
from function_defs import Functions
from flask_with_defaults import FlaskWithDefaults


# load the config.json file
config = json.load(open('config.json'))

# instantiate the functions class
functions = Functions(config['storage_file'])

# Create the flask app
app = FlaskWithDefaults(__name__)
CORS(app)

# serve on /kvs route to list all keys
@app.route('/kvs')
def list_keys(methods=['GET']):
    return functions.list_keys()

# serve on the /kvs/<key> route to play with individual keys
@app.route('/kvs/<key>')
def kvs(key):
    response = 'Unsupported HTTP method', 501

    # Validate key value
    if key is None or key == '':
        response = 'You need to send a key', 500

    # Make sure the body isn't empty for PUT and POST requests
    if not config['allow_empty_values'] and request.method in ['POST', 'PUT'] and (request.data is None or request.data == ''):
        response = 'You need to send a value', 500

    # Function dispatcher. Choose function from the functions class based on request type
    if response[1] != 500:
        if request.method == 'GET':
            response = functions.get_key(key)
        if request.method == 'POST':
            response = functions.set_key(key, request.data)
        if request.method == 'PUT':
            response = functions.mod_key(key, request.data, config['strict_modify'])
        if request.method == 'DELETE':
            response = functions.del_key(key, config['strict_delete'])

    # write the log
    write_log(key, request, response)

    # return the response
    return response

# start the server
if __name__ == '__main__':
    app.run(host=config['host'], port=config['port'], threaded=config['threaded'], debug=config['debug'])