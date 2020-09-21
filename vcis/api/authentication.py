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
            'exception' : "Unknown error." if ex is None else  ex.description
        }

    update_api_stats(request_path)
    logging.debug(get_api_stats(request_path))
    return json.dumps(json_data)


# TODO: Commmon validation funciton
def expect(key_name, data_dict):
    if key_name not in data_dict:
        # TODO: Add to logging
        raise BadRequest('Expected parameter [{0}] not found.'.format(key_name))
    return data_dict[key_name]


def validate_user_credentials(username, password):
    # Check is username is in credential store
    # If username is in credential store, check if password is correct
    from modules.credential_store import is_registered
    from modules.DataStorage import SqliteDataStore

    import pdb
    pdb.set_trace()
    credential_store = SqliteDataStore("./data/cred_store.sqlite3")

    if is_registered(username):
        return True
    if username.lower() == "zhixian":
        return True
    return False

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
        # Normalize JSON keys to lowercase (TODO: common function)
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
            username = expect('username', message_dict)
            password = expect('password', message_dict)

            # Validate credentials
            is_valid_credentials =  validate_user_credentials(username, password)
            if is_valid_credentials:
                # Get roles
                # Make JWT
                json_data = {
                    'name' : request.path,
                    'result': 'OK',
                    'jwt' : str(datetime.utcnow())
                }
            else:
                json_data = {
                    'name' : request.path,
                    'result': 'NG',
                    'jwt' : None
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
