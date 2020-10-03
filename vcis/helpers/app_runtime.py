################################################################################
# Modules and functions import statements
################################################################################

import logging
import json

from os import path
from socket import gethostname, getfqdn
from uuid import uuid4
from flask import Flask, g, request

from jinja2 import Template, Environment, FileSystemLoader

########################################
# Define core functions
########################################

def get_host_name():
    return gethostname()

def get_domain_name():
    return getfqdn()

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
    app_config['DOMAIN_NAME'] = get_domain_name()
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
# Request decorators
################################################################################

# @app.before_first_request
# def before_app_first_request():

#     """ 
#     This function will run once before the first request to this instance of the application.
#     You may want to use this function to create any databases/tables required for your app.
#     """
#     print("This function will run once ")

@app.before_request
def before_each_request():
    # g is an object provided by Flask. 
    # It is a global namespace for holding any data you want during a single app context.
    # An app context lasts for one request / response cycle, 
    # Hence, g is not appropriate for storing data across requests
    logging.warning("before_request is running!")
    correlation_id = request.headers.get("X-Correlation-Id")
    if correlation_id is None:
        correlation_id = uuid4()
    g.correlation_id = correlation_id
    g.user = "alibaba"
    # ZX:   Unfortunate, we cannot make changes to request.headers 
    #       (its 'EnvironHeaders' and they are immutable)
    # import pdb
    # pdb.set_trace()
    
# @app.after_request
# def after_request_func(response):
#     """ 
#     This function will run after a request, as long as no exceptions occur.
#     It must take and return the same parameter - an instance of response_class.
#     This is a good place to do some application cleanup.
#     """
#     # username = g.username
#     # foo = session.get("foo")
#     # print("after_request is running!", username, foo)
#     return response

# @app.teardown_request
# def teardown_request_func(error=None):
#     """ 
#     This function will run after a request, regardless if an exception occurs or not.
#     It's a good place to do some cleanup, such as closing any database connections.
#     If an exception is raised, it will be passed to the function.
#     You should so everything in your power to ensure this function does not fail, so
#     liberal use of try/except blocks is recommended.
#     """
#     print("teardown_request is running!")
#     if error:
#         # Log the error
#         print(str(error))


################################################################################
# Main function
################################################################################

if __name__ == '__main__':
    pass
