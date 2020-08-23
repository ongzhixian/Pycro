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
from app.settings import appsecrets

from modules.oanda import Oanda

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

# Redundant;
# console_logger = logging.StreamHandler() # Log to console as well
# console_logger.setFormatter(logging_format)
# root_logger.addHandler(console_logger)

################################################################################
# Import api/modules
################################################################################

from api import *
from modules import *

################################################################################
# Main function
################################################################################

if __name__ == '__main__':
    logging.info("[PROGRAM START]")
    # logging.info("Running on [{0}]".format(app_helpers.hostname))
    logging.critical("%8s test message %s" % ("CRITICAL", str(datetime.utcnow())))
    logging.error("%8s test message %s" % ("ERROR", str(datetime.utcnow())))
    logging.warning("%8s test message %s" % ("WARNING", str(datetime.utcnow())))
    logging.info("%8s test message %s" % ("INFO", str(datetime.utcnow())))
    logging.debug("%8s test message %s" % ("DEBUG", str(datetime.utcnow())))

    # api = Oanda(Oanda.PRACTICE_ENVIRONMENT)
    # api.get_instrument_list();
    # json = api.get_price("EUR_USD") 
    # print(json)

    # import pdb
    # pdb.set_trace()

    logging.info("[PROGRAM END]")

