################################################################################
# Modules and functions import statements
################################################################################

import json
import logging
import sys

from flask import url_for, get_flashed_messages, make_response, request, g
from helpers.app_runtime import jinja2_env, app_config
from helpers.jwt_helper import decrypt_jwt

################################################################################
# Functions
################################################################################

def get_app_config(name="", config=app_config):
    # Let's return a empty string on not found for now.
    # It maybe better to raise an exception
    # TODO: Change all the app_config['application']['session_id'] to use this function instead
    if name is None:
        return ""

    tokens = name.split(".")

    if len(tokens) <= 0:
        return "" 

    token_1 = tokens[0]

    if len(tokens[1:]) > 0 and token_1 in config:
        return get_app_config(".".join(tokens[1:]), config[token_1])

    if len(tokens[1:]) == 0 and token_1 in config:
        return config[token_1]
    else:
        return ""

def get_model(cookie_json=None):
    caller = sys._getframe(1)                       # '_getframe(1)' gets previous stack; 
                                                    # '_getframe()' gets current stack
    caller_name = caller.f_code.co_name             # returns 'view_home'
    module_name = caller.f_globals['__name__']      # returns 'modules.default_routes'
    package_name = caller.f_globals['__package__']  # returns 'modules'

    context = cookie_json if cookie_json is not None else {}
    context['url_for'] = url_for                            # function for Flask
    context['get_flashed_messages'] = get_flashed_messages  # function for Flask
    context['app_settings'] = app_config                  # make application settings available
    context['view_name'] = caller_name
    context['view_module'] = module_name
    context['view_package'] = package_name
    context['view_id'] = "{0}.{1}".format(module_name, caller_name)

    # context['auth_cookie'] = request.cookies.get(appconfig["application"]["auth_cookie_name"])
    # context['current_datetime'] = datetime.now()
    # context = {
    #     'auth_cookie'       : request.cookies.get(appconfig["application"]["auth_cookie_name"]),
    #     'current_datetime'  : datetime.now()
    # }
    return context

def view(model=None, view_path=None):
    if view_path is None:
        caller = sys._getframe(1)                       # '_getframe(1)' gets previous stack; 
                                                        # '_getframe()' gets current stack
        caller_name = caller.f_code.co_name             # returns 'view_home'
        module_name = caller.f_globals['__name__']      # returns 'modules.default_routes'
        package_name = caller.f_globals['__package__']  # returns 'modules'

        view_path = module_name.split('.')
        view_path.remove(package_name)
        view_path.append("{0}.html".format(caller_name))
        view_path = '/'.join(view_path)                 # returns 'default_routes/view_home.html

    logging.info("fetching view [{0}]".format(view_path))

    if model is None:
        model = get_model()

    #Return an string of rendered template
    #return jinja2_env.get_template(view_path).render(model)

    #Change to return a response object instead
    response = make_response(jinja2_env.get_template(view_path).render(model))
    response.headers['Server'] = app_config['application']['version']
    #a = get_app_config("application.test_nested.test_username")
    response.set_cookie(app_config['application']['session_id'], g.session_id)
    return response


def api_response(json_data):
    logging.debug("IN api_response")
    response = make_response(json.dumps(json_data))
    response.headers['Server'] = app_config['application']['version']
    response.set_cookie(app_config['application']['session_id'], g.session_id)
    return response
    

################################################################################
# Decorators
################################################################################


def api_authorization(fn):
    def wrapper(*args, **kwargs):
        logging.info("api_authorization=[{0}.{1}]".format(fn.__module__, fn.__name__))
        # Check for cookie
        # id_token = request.cookies.get("id_token")
        # if not id_token:
        #     return "invalid - api auth Failed "
        
        
        # Check for header
        if "authorization" not in request.headers:
            return "invalid - api auth Failed "

        auth_tokens = request.headers["Authorization"].split()
        if len(auth_tokens) < 2:
            return "invalid len - api auth Failed "
        
        # decode JWT
        jwt = auth_tokens[1]
        claims = decrypt_jwt(jwt)
        # {
        #   'aud': 'plato.emptool.com'
        # , 'exp': 1601691436
        # , 'info': "I'm a signed token"
        # , 'iss': 'plato.emptool.com'
        # , 'nbf': 1601690236} (correlation_id=some.g.correlationId)

        # TODO: We only accept claims intend for us (audience)

        # TODO: We only accept claims from issuers/audience

        # if claims contains username, set username
        if 'username' in claims and len(claims['username'].strip()) > 0:
            g.username = claims['username']

        logging.info(claims)
        # if 'id-token' not in request.headers:
        #     return "invalid - api auth Failed "

        return fn(*args, **kwargs)

    # Renaming the function name
    # Otherwise it gives a very odd error as follows:
    # AssertionError: View function mapping is overwriting an existing endpoint function: wrapper
    # wrapper.__name__ = fn.__name__
    return wrapper


def jwt_authorization(fn):
    def wrapper(*args, **kwargs):
        logging.info("jwt_authorization=[{0}.{1}]".format(fn.__module__, fn.__name__))
        # Check for cookie
        # id_token = request.cookies.get("id_token")
        # if not id_token:
        #     return "invalid - api auth Failed "
            
        # Check for header
        if 'id-token' not in request.headers:
            return "invalid - api auth Failed "    

        return fn(*args, **kwargs)
    # Renaming the function name
    # Otherwise it gives a very odd error as follows:
    # AssertionError: View function mapping is overwriting an existing endpoint function: wrapper
    # wrapper.__name__ = fn.__name__
    return wrapper

################################################################################
# Export module variables
################################################################################
 
 # N/A

################################################################################
# Main function
################################################################################

if __name__ == '__main__':
    pass
