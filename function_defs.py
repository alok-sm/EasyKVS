import shelve
from flask import jsonify
data = shelve.open("data.shelve")

# All the main Key Value Store functions go here
class Functions:

    # Constructor takes the storage file as param
    # and saves it to the object
    def __init__(self, storage_file):
        self.data = shelve.open(storage_file)

    # Lists all the keys on the db
    def list_keys(self):
        return jsonify(list(self.data.keys()))

    # Gets the value of the key
    def get_key(self, key):
        value = self.data.get(key, None)
        if value == None:
            return 'Key not found. Send a POST request to set the key', 500
        return value, 200

    # Sets the value of the key
    def set_key(self, key, value):
        if key in self.data:
            return 'Key exists. Send a PUT request to overwrite key', 500
        self.data[key] = value
        return '', 204

    # Modifies the value of the key
    def mod_key(self, key, value, strict_modify):
        if strict_modify and key not in self.data:
            return 'Key not found. Send a POST request to set the key', 500
        self.data[key] = value
        return '', 204

    # Deletes the key
    def del_key(self, key, strict_delete):
        try: del self.data[key]
        except Exception as e:
            if strict_delete: return 'Key to delete not found', 500
        return '', 204