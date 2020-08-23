# The web application start file
################################################################################
# Import statements
################################################################################

import json
import logging
from datetime import datetime

# from bottle import run
# from app.helpers import application
# from app.settings import hostname, appconfig
from app.settings import appsecrets, appconfig

################################################################################
# Setup logging configuration
################################################################################

# ZX standard for logging in Python 3
logging_format = logging.Formatter('%(asctime)-15s %(levelname)-8s %(name)-5s %(message)s')
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
default_console_logger = root_logger.handlers[0]
default_console_logger.setFormatter(logging_format)

file_logger = logging.FileHandler('vcis.log')
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
    if 'application' in appconfig \
        and 'print_test_log' in appconfig['application'] \
        and appconfig['application']['print_test_log'] == True:
            logging.critical("%8s test message %s" % ("CRITICAL", str(datetime.utcnow())))
            logging.error("%8s test message %s" % ("ERROR", str(datetime.utcnow())))
            logging.warning("%8s test message %s" % ("WARNING", str(datetime.utcnow())))
            logging.info("%8s test message %s" % ("INFO", str(datetime.utcnow())))
            logging.debug("%8s test message %s" % ("DEBUG", str(datetime.utcnow())))


################################################################################
# Main function
################################################################################


if __name__ == '__main__':
    logging.info("[PROGRAM START]")
    print_test_log()
    #app.run(host='127.0.0.1', port=8080, debug=True)
    logging.info("[PROGRAM END]")
