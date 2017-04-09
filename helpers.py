import sys
import logging
import json

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

def write_log(key, request, response):
    log_line = {
        'http_method': request.method, 
        'req_key': key,
        'req_val': request.data,
        'res_code': response[1],
        'res_str': response[0]
    }

    print >> sys.stdout, json.dumps(log_line, sort_keys=True)
