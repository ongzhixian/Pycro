
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

def create_claims(claims=None):
    
    if claims == None:
        claims = {}

    for k, v in claims.items():
        if not k.islower():
            claims[k.lower()] = v
            claims.pop(k)

    nbf = round(time())
    exp = nbf + (60 * 20) # 20 minutes TODO: read from config

    if 'iss' not in claims.keys():
        claims["iss"] = "plato.emptool.com"
    if 'aud' not in claims.keys():
        claims["aud"] = "plato.emptool.com"
    if 'nbf' not in claims.keys():
        claims["nbf"] = nbf
    if 'exp' not in claims.keys():
        claims["exp"] = exp

    return claims

def create_signed_token(claims, jwk = get_jwk()):
    
    if jwk is None:
        return None
    
    token = JWT(
        header = {
            "alg": "HS256"
        },
        claims = claims)

    token.make_signed_token(jwk)

    return token

def create_signed_jwt(claims, jwk = get_jwk()):
    
    signed_token = create_signed_token(claims, jwk)

    if signed_token is None:
        return None
    
    logging.debug("signed_token (serialize) [{0}]".format(signed_token.serialize()))
    return signed_token.serialize()


def create_encrypted_token(claims, jwk = get_jwk()):

    signed_jwt = create_signed_jwt(claims, jwk)

    encrypted_token = JWT(
        header = {
            "alg": "A256KW", 
            "enc": "A256CBC-HS512"
        },
        claims = signed_jwt
    )

    encrypted_token.make_encrypted_token(jwk)
    
    return encrypted_token

def create_encrypted_jwt(claims, jwk = get_jwk()):
    
    encrypted_token = create_encrypted_token(claims, jwk)

    if encrypted_token is None:
        return None
    
    return encrypted_token.serialize()


def decrypt_jwt(jwt, jwk = get_jwk()):

    if jwk is None:
        return None

    encrypted_token = JWT(key=jwk, jwt=jwt)

    signed_token = JWT(key=jwk, jwt=encrypted_token.claims)

    return json.loads(signed_token.claims)