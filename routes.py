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

    # Validate the key 
    if key is None or key == '':
        response = 'You need to send a key', 500

    print(request.form)

    # validate the value
    if request.method in ['POST', 'PUT']:
        if request.form is None or request.form['value'] is None:
            response = 'You need to send a value1', 500
        if (not config['allow_empty_values'] and request.form['value'] == ''):
            response = 'You need to send a value2', 500

    # Function dispatcher. Choose function from the functions class based on request type
    if response[1] != 500:
        if request.method == 'GET':
            response = functions.get_key(key)
        if request.method == 'POST':
            response = functions.set_key(key, request.form['value'])
        if request.method == 'PUT':
            response = functions.mod_key(key, request.form['value'], config['strict_modify'])
        if request.method == 'DELETE':
            response = functions.del_key(key, config['strict_delete'])

    # write the log
    write_log(key, request, response)

    # return the response
    return response

# start the server
if __name__ == '__main__':
    app.run(host=config['host'], port=config['port'], threaded=config['threaded'], debug=config['debug'])