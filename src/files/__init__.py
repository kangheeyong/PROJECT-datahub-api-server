from sanic import Blueprint

from .en_dummy import en_dummy

files = Blueprint.group(en_dummy, url_prefix='/files')
