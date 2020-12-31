# The web application start file
################################################################################
# Import statements
################################################################################

import json
import logging
from datetime import datetime

from helpers.app_runtime import app, app_config, app_secrets

from modules import *
from api import *
from pages import *
from os import environ



################################################################################
# Setup logging configuration
################################################################################
# import sys
# import os
# if sys.platform.lower() == "win32": 
#     os.system('color')

# TODO: Move this elsewhere (runtime?)
# from flask import g
# ZX standard for logging in Python 3
class CorrelationIdFilter(logging.Filter):

    # This is a logging filter that makes the request ID available for use in
    # the logging format. Note that we're checking if we're in a request
    # context, as we may want to log things before Flask is fully loaded.
    def filter(self, record):
        #record.request_id = request_id() if flask.has_request_context() else ''
        record.request_id = 'some.g.correlationId'
        return True
    # def filter(self, rec):
    #     return rec.levelno == logging.INFO

# TODO: Move this elsewhere (runtime?)
# TODO: Consider using dictconfig() format instead
#logging_format = logging.Formatter('%(asctime)-15s %(levelname)-8s %(name)-5s %(module)s.%(funcName)s %(message)s')
logging_format = logging.Formatter('%(asctime)-15s %(levelname)-8s %(name)-5s [%(module)s.%(funcName)s -- %(lineno)d] %(message)s (correlation_id=%(request_id)s)')

correlationIDFilter = CorrelationIdFilter()
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
root_logger.addFilter(correlationIDFilter)

default_console_logger = root_logger.handlers[0]
default_console_logger.setFormatter(logging_format)
default_console_logger.addFilter(correlationIDFilter)

file_logger = logging.FileHandler('logs/vcis.log')
file_logger.setFormatter(logging_format)
file_logger.addFilter(correlationIDFilter)

root_logger.addHandler(file_logger)


################################################################################
# Import api/modules
################################################################################

from api import *
from modules import *

################################################################################
# Some ad-hoc helper function
################################################################################

# TODO: Move this elsewhere (runtime?)
def print_test_log():
    if 'application' in app_config \
        and 'print_test_log' in app_config['application'] \
        and app_config['application']['print_test_log'] == True:
            logging.critical("%8s test message %s" % ("CRITICAL", str(datetime.utcnow())))
            logging.error("%8s test message %s" % ("ERROR", str(datetime.utcnow())))
            logging.warning("%8s test message %s" % ("WARNING", str(datetime.utcnow())))
            logging.info("%8s test message %s" % ("INFO", str(datetime.utcnow())))
            logging.debug("%8s test message %s" % ("DEBUG", str(datetime.utcnow())))


################################################################################
# Main function
################################################################################
import os

if __name__ == '__main__':
    logging.info("[PROGRAM START]")
    print_test_log()
    # TODO: Move this elsewhere (runtime?)
    # TODO: Make the host, port and debug from the below to be configurable
    # Use SSL if conditions are right
    if 'use_ssl' in app_config['runtime']               \
        and app_config['runtime']['use_ssl'] == True    \
        and 'ssl' in app_config                             \
        and 'crt_file' in app_config['ssl']                 \
        and app_config['ssl']['crt_file'] != None           \
        and os.path.exists(app_config['ssl']['crt_file'])   \
        and 'pvk_file' in app_config['ssl']                 \
        and app_config['ssl']['pvk_file'] != None           \
        and os.path.exists(app_config['ssl']['pvk_file']):
        crt_file = app_config['ssl']['crt_file']
        pvk_file = app_config['ssl']['pvk_file']
        app.run(host='127.0.0.1', port=8080, debug=True, ssl_context=(crt_file, pvk_file))
    app.run(host='127.0.0.1', port=8080, debug=True, ssl_context=None)
    logging.info("[PROGRAM END]")
