import shelve
import json
import sys

# dumps the contents of the db as a json string
config = json.load(open('config.json'))
storage_file = config['storage_file']
if len(sys.argv) > 1:
    storage_file = sys.argv[1]
data = shelve.open(storage_file)
print json.dumps(dict(data), indent=4, sort_keys=True)