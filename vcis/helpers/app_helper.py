################################################################################
# Modules and functions import statements
################################################################################

import json
import logging
import sys

from flask import url_for, get_flashed_messages, make_response, request
from helpers.app_runtime import jinja2_env, app_config
from helpers.jwt_helper import decrypt_jwt

################################################################################
# Functions
################################################################################

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
    return response


def api_response(json_data):
    logging.debug("IN api_response")
    response = make_response(json.dumps(json_data))
    response.headers['Server'] = app_config['application']['version']
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
        
        jwt = auth_tokens[1]

        r = decrypt_jwt(jwt)
        
        import pdb
        pdb.set_trace()
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
