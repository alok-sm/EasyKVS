import sys
import json

# Write prettier logs for easy debugging
def write_log(key, request, response):
    print('http_method  : ' +  str(request.method))
    print('req_key      : ' +  str(key))
    if request.method in ['POST', 'PUT']:
        print('req_val      : ' +  str(request.form['value']))
    print('res_code     : ' +  str(response[1]))
    print('res_str      : ' +  str(response[0]))
