################################################################################
# Modules and functions import statements
################################################################################

import json
import logging
from datetime import datetime
from helpers.app_runtime import app, app_config, app_secrets
from helpers.app_helper import api_response, get_model, api_authorization
from helpers.jwt_helper import create_claims, create_signed_jwt, create_encrypted_jwt
from modules.api_stats import update_api_stats, get_api_stats
from flask import request, make_response

from werkzeug.exceptions import BadRequest

log = logging.getLogger(__name__)

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
            'exception' : "Unknown error." if ex is None else ex.description
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

def get_sha256_salt_and_hash(password):
    from Crypto.Random import get_random_bytes
    from binascii import hexlify as hex, unhexlify as unhex
    from Crypto.Hash import SHA256

    new_salt = hex(get_random_bytes(8)).decode("utf8")

    h = SHA256.new()
    h.update('soma)password'.encode('utf8'))

    new_hash = new_salt + h.hexdigest()
    return (new_salt, new_hash)

def validate_user_credentials(username, password):
    # Check is username is in credential store
    # If username is in credential store, check if password is correct
    from modules.credential_store import is_registered
    from modules.DataStorage import DataStore, SqliteDataStore, UserModel
    
    (pwd_salt, pwd_hash) = get_sha256_salt_and_hash(password)    

    data_store = DataStore('sqlite')

    # TODO: Add a add_user api
    # data_store.add_user('asd2', pwd_hash, pwd_salt, 'asd@localhost')

    user = data_store.get_user(username)
    if user is not None and user.is_valid_credential(password):
        return True

    return False

    #h.update(password.encode("utf8"))
    
    # pwd_salt = hex(get_random_bytes(8))
    # pwd_hash = pwd_salt + h.hexdigest()

    # credential_store = SqliteDataStore("./data/cred_store.sqlite3")
    # results = credential_store.query('SELECT * FROM user WHERE username=?', username)

    # if len(results) <= 0:
    #     logging.info("Username (%s) not found.", username)
    #     return False
    
    # logging.info("Username (%s) found. %s", username, results[0])
    # # logging.info(results[0])
    # userData = UserModel(results[0])
    # if userData.IsValidCredential(password):
    #     return True

    #args = ('zhixian',)
    #q = credential_store.query('SELECT * FROM user')
    # import pdb
    # pdb.set_trace()

    # if is_registered(username):
    #     return True
    # if username.lower() == "zhixian":
    #     return True
    
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
        log.warning('SPECIAL log')

        user_data = request.json
        if user_data is None:
            logging.debug("user_data is None")
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
                    'jwt' : create_signed   _jwt(create_claims({
                        "info": "I'm a signed token"
                    }))
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
