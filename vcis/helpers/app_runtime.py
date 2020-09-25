################################################################################
# Modules and functions import statements
################################################################################

import logging
import json

from os import path
from socket import gethostname
from flask import Flask

from jinja2 import Template, Environment, FileSystemLoader

########################################
# Define core functions
########################################

def path_exists(filepath):
    if path.exists(filepath):
        return True
    else:
        return False

def open_file(filepath):
    with open(filepath) as f:
        return f.read()

def get_host_name():
    return gethostname()

def get_config_json(filename='config.json'):
    if path.exists(filename):
        logging.debug("Opening config.json")
        with open(filename, encoding='utf-8', mode='r') as app_config_file:
            logging.debug("Loading config.json")
            app_config = json.load( app_config_file )
            logging.debug("app_config loaded")
    else:
        app_config = {}
    app_config['DEVICE_NAME'] = get_host_name()
    return app_config

def get_secrets_json(filename='secrets.json'):
    if path.exists(filename):
        logging.debug("Opening secrets.json")
        with open(filename, encoding='utf-8', mode='r') as app_secrets_file:
            logging.debug("Loading secrets.json")
            app_secrets = json.load( app_secrets_file )
            logging.debug("secrets loaded")
    else:
        app_secrets = {}
    return app_secrets

def setup_jinja2_env():
    logging.debug("In setup_jinja2_env()")
    env = Environment(loader = FileSystemLoader('./views'))
    return env

################################################################################
# Variables dependent on Application basic functions
################################################################################

app_config = get_config_json()
app_secrets = get_secrets_json()
jinja2_env = setup_jinja2_env()
api_stats = {}
app = Flask("vcis", static_url_path='/', static_folder='wwwroot',)

################################################################################
# Main function
################################################################################

if __name__ == '__main__':
    pass
