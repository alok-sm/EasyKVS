import shelve
import json
data = shelve.open("data.shelve")
print json.dumps(dict(data))