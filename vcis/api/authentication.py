################################################################################
# Modules and functions import statements
################################################################################

import json
import logging
from datetime import datetime
from helpers.app_runtime import app, app_config
from helpers.app_helper import api_response, get_model, api_authorization
from modules.api_stats import update_api_stats, get_api_stats
from flask import request, make_response

from werkzeug.exceptions import BadRequest

################################################################################
# Helper response functions 
################################################################################

def negative_json_response(method_name):
    json_data = {
        'name' : method_name,
        'result': 'NG',
        'jwt' : None
    }
    update_api_stats(method_name)
    logging.debug(get_api_stats(method_name))
    return json.dumps(json_data)

def json_response(request, json_data=None, ex=None):
    request_path = request.path

    if json_data is None:
        json_data = {
            'request.path' : request_path,
            'result': 'NG',
            'exception' : ex.description
        }

    update_api_stats(request_path)
    logging.debug(get_api_stats(request_path))
    return json.dumps(json_data)


def expect(key_name, data_dict):
    if key_name not in data_dict:
        # TODO: Add to logging
        import pdb
        import inspect
        import sys
        caller = sys._getframe(1)
        x = inspect.currentframe().f_back.f_locals.items()

        pdb.set_trace()
        raise BadRequest('Expected parameter [{0}] not found.'.format(key_name))


################################################################################
# API 
################################################################################
@app.route('/api/authenticate/user', methods=['POST'])
def api_authenticate_user_post(errorMessages=None):
    '''  
    API to authenticate user and return a JWT to user
    '''
    logging.debug("In api_authenticate_user_post()")

    try:
        user_data = request.json
        if user_data is None:
            return json_response(request)

        # Clean input
        # Normalize JSON keys to lowercase
        for k, v in user_data.items():
            if not k.islower():
                user_data[k.lower()] = v
                user_data.pop(k)

        # Validate input
        expect('message_type', user_data)
        expect('message', user_data)
        
        # Do something with input
        if user_data['message_type'].lower() == 'username:password':
            message_dict = user_data['message']
            expect('username1', message_dict)
            expect('password', message_dict)


            json_data = {
                'name' : request.path,
                'result': 'success',
                'jwt' : str(datetime.utcnow())
            }
            return json_response(request, json_data)
        
        raise BadRequest()
    # except BadRequest:
    #     return json_response(request, None, e)
    except Exception as e:
        return json_response(request, None, e)

    
    
    # jsonData = request.json
    # if 'message' not in jsonData:
    #     pass

    # update_api_stats('/api/authenticate/user')
    # logging.debug(get_api_stats('/api/authenticate/user'))
    # return json.dumps(json_data)
