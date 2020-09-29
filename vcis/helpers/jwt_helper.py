
import json
import logging
from jwcrypto.jwk import JWK
from jwcrypto.jwt import JWT
from time import time

from helpers.app_runtime import app_config, app_secrets

def get_jwk():
    jwk_config = None
    # Get JWK (if exists)
    if 'jwk' in app_secrets and 'kty' in app_secrets['jwk']:
        key_type = app_secrets['jwk']['kty'].lower()
        if key_type == "oct" and 'k' in app_secrets['jwk']:
            jwk_config = { 
                'kty' : key_type, 
                'k': app_secrets['jwk']['k'] 
            }
        # Add support for other key types here;
        # For now, we only support octat sequence ("oct")

    if jwk_config is not None:
        return JWK.from_json(json.dumps(jwk_config))
    return None

def create_signed_jwt():
    jwk = get_jwk()

    if jwk is None:
        return None

    nbf = round(time())
    exp = nbf + (60 * 20) # 20 minutes TODO: read from config

    token = JWT(
        header = {
            "alg": "HS256"
        },
        claims = {
            "iss" : "plato.emptool.com",
            "aud" : "plato.emptool.com",
            "nbf" : nbf,
            "exp" : exp,
            "info": "I'm a signed token"
        })
    token.make_signed_token(jwk)
    return token
    
    #logging.info(token.serialize())


def create_encrypted_jwt():
    jwk = get_jwk()

    if jwk is None:
        return None

    nbf = round(time())
    exp = nbf + (60 * 20) # 20 minutes TODO: read from config

    token = JWT(
        header = {
            "alg": "HS256"
        },
        claims = {
            "iss" : "plato.emptool.com",
            "aud" : "plato.emptool.com",
            "nbf" : nbf,
            "exp" : exp,
            "info": "I'm a signed token"
        })
    token.make_signed_token(jwk)
    logging.info(token.serialize())

    encrypted_token = JWT(
        header = {
            "alg": "A256KW", 
            "enc": "A256CBC-HS512"
        },
        claims = token.serialize()
        )
    encrypted_token.make_encrypted_token(jwk)
    return encrypted_token.serialize()
