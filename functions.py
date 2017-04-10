import shelve
data = shelve.open("data")

def get_key(key):
    value = data.get(key, None)
    if value == None:
        return 'Key not found. Send a POST request to set the key', 500
    return value, 200

def set_key(key, value):
    if key in data:
        return 'Key exists. Send a PUT request to overwrite key', 500
    data[key] = value
    return '', 204

def mod_key(key, value, strict_modify):
    if strict_modify and key not in data:
        return 'Key not found. Send a POST request to set the key', 500
    data[key] = value
    return '', 204

def del_key(key, strict_delete):
    if strict_delete and key not in data:
        return 'Key to delete not found', 500
    try: del data[key]
    except Exception as e: pass
    return '', 204