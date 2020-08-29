################################################################################
# Modules and functions import statements
################################################################################

import json
import logging
from datetime import datetime
from helpers.app_runtime import app, app_config
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

    return json.dumps(json_data)

@app.route('/api/common/name', methods=['GET', 'POST'])
def api_common_name_get(errorMessages=None):
    '''  
    API to return device name
    '''
    logging.debug("In api_common_name_get()")

    json_data = {
        'name' : '/api/common/name',
        'result': 'success',
        'datetime' : app_config['DEVICE_NAME']
    }

    return json.dumps(json_data)

@app.route('/api/common/version', methods=['GET', 'POST'])
def api_common_version_get(errorMessages=None):
    '''  
    API to return version
    '''
    logging.debug("In api_common_version_get()")

    json_data = {
        'name' : '/api/common/version',
        'result': 'success',
        'datetime' : app_config['application']['version']
    }

    return json.dumps(json_data)
