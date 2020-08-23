################################################################################
# Modules and functions import statements
################################################################################

import logging
import json

########################################
# Define core functions
########################################

def get_config_json():
    logging.debug("Opening appconfig.json")
    appconfig_file = open( 'appconfig.json' )
    logging.debug("Loading appconfig.json")
    appconfig = json.load( appconfig_file )
    logging.debug("app_config loaded")
    return appconfig

def get_secrets_json():
    logging.debug("Opening secrets.json")
    secrets_file = open( 'secrets.json' )
    logging.debug("Loading secrets.json")
    appsecrets = json.load( secrets_file )
    logging.debug("secrets loaded")
    return appsecrets

################################################################################
# Variables dependent on Application basic functions
################################################################################

appconfig = get_config_json()
appsecrets = get_secrets_json()

################################################################################
# Main function
################################################################################

if __name__ == '__main__':
    pass
