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

# ZX standard for logging in Python 3
logging_format = logging.Formatter('%(asctime)-15s %(levelname)-8s %(name)-5s %(message)s')
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
default_console_logger = root_logger.handlers[0]
default_console_logger.setFormatter(logging_format)

file_logger = logging.FileHandler('logs/vcis.log')
file_logger.setFormatter(logging_format)
root_logger.addHandler(file_logger)

################################################################################
# Import api/modules
################################################################################

from api import *
from modules import *

################################################################################
# Some ad-hoc helper function
################################################################################

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
