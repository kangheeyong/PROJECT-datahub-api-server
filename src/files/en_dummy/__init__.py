from sanic import Blueprint

from .info import info

en_dummy = Blueprint.group(info, url_prefix='/en_dummy')
