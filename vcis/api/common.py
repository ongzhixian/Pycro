################################################################################
# Modules and functions import statements
################################################################################

import logging
from datetime import datetime
from helpers.app_runtime import app, app_config
from helpers.app_helper import api_response, get_model, api_authorization
from modules.api_stats import update_api_stats, get_api_stats
from flask import request, make_response


################################################################################
# API 
################################################################################
@app.route('/api/common/utc', methods=['GET', 'POST'])
def api_common_utc_get(errorMessages=None):
    '''  
    API to return server time in UTC
    '''
    logging.debug("In api_common_utc_get()")

    json_data = {
        'name' : '/api/common/utc',
        'result': 'success',
        'datetime' : str(datetime.utcnow())
    }

    update_api_stats('/api/common/utc')
    logging.debug(get_api_stats('/api/common/utc'))
    return json.dumps(json_data)


@app.route('/api/common/name', methods=['GET', 'POST'])
@api_authorization
def api_common_name_get(errorMessages=None):
    '''  
    API to return device name
    '''
    logging.debug("In api_common_name_get()")

    json_data = {
        'name' : '/api/common/name',
        'result': 'success',
        'device_name' : app_config['DEVICE_NAME']
    }

    update_api_stats('/api/common/name')
    return api_response(json_data)
    #return json.dumps(json_data)


@app.route('/api/common/version', methods=['GET', 'POST'])
def api_common_version_get(errorMessages=None):
    '''  
    API to return version
    '''
    logging.debug("In api_common_version_get()")

    json_data = {
        'name' : '/api/common/version',
        'result': 'success',
        'version' : app_config['application']['version']
    }

    update_api_stats('/api/common/version')
    return json.dumps(json_data)


@app.route('/api/common/echo', methods=['GET', 'POST'])
def api_common_echo_get(errorMessages=None):
    '''  
    API to echo messages
    '''
    logging.debug("In api_common_echo_get()")

    # if using GET method, we expect message query string parameter
    # Otherwise, is error
    if request.method == 'GET':
        args_count = len(request.args)
        if args_count < 0:
            json_data = {
                'name' : '/api/common/echo',
                'result': 'NG',
                'result_message': 'Invalid json request.',
                'method': request.method
            }
            update_api_stats('/api/common/echo')
            return json.dumps(json_data)

        # if there are args, we expect an arg call 'message'
        # Otherwise, is error
        if 'message' not in request.args:
            json_data = {
                'name' : '/api/common/echo',
                'result': 'NG',
                'result_message': 'Invalid json request.',
                'method': request.method
            }
            update_api_stats('/api/common/echo')
            return json.dumps(json_data)

        # Orthodox answer
        json_data = {
            'name' : '/api/common/echo',
            'result': 'OK',
            'result_message': "{0} (echo) {1}".format(datetime.utcnow(), request.args['message']),
            'method': request.method
        }
        update_api_stats('/api/common/echo')
        return json.dumps(json_data)

    if request.method == 'POST':
        try:
            jsonData = request.json

            if 'message' not in jsonData:
                json_data = {
                    'name' : '/api/common/echo',
                    'result': 'NG',
                    'result_message': 'Invalid json request.',
                    'method': request.method
                }
                update_api_stats('/api/common/echo')
                return json.dumps(json_data)

            json_data = {
                'name' : '/api/common/echo',
                'result': 'success',
                'result_message': "{0} (echo) {1}".format(datetime.utcnow(), jsonData['message']),
                'method': request.method
            }
            update_api_stats('/api/common/version')
            return json.dumps(json_data)

        except:
            json_data = {
                'name' : '/api/common/echo',
                'result': 'NG',
                'result_message': 'Invalid json request.',
                'method': request.method
            }
            update_api_stats('/api/common/version')
            return json.dumps(json_data)
    

    
    #if request.method == 'POST':
    json_data = {
        'name' : '/api/common/echo',
        'result': 'NG',
        'result_message': 'Invalid json request.',
        'method': request.method
    }
    update_api_stats('/api/common/echo')
    return json.dumps(json_data)
    






# @app.route('/api/echo', methods=['GET', 'POST'])
# def api_echo_get(errorMessages=None):
#     '''  
#     Test API
#     '''
#     logging.debug("In api_echo_get()")

#     req_json = None
#     try:
#         logging.info("in req_json")
#         req_json = request.json
#     except:
#         req_json = None
    
#     if req_json is None:
#         json_data = {
#             'name' : 'api_check_student_id',
#             'result': 'NG',
#             'result_message': 'Invalid json request.',
#         }
#         return json.dumps(json_data)

#     json_data = {
#         'name' : 'test',
#         'result': 'success',
#         'datetime' : req_json['message']
#     }

#     return json.dumps(json_data)