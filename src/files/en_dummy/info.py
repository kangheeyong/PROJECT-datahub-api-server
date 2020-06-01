import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from sanic import Blueprint
from sanic.response import json, file_stream
from sanic_openapi import doc

from lib_custom import authorized

info = Blueprint('file_en_dummy')

ABS_PATH = os.path.abspath(os.path.dirname(__file__))


@info.route('/info')
@doc.consumes(doc.String(name='token'), location='header', required=True)
@authorized(token='12')
async def route(request):
    return json({'status': 'success'})


@info.route('/data.tsv', methods=['POST'])
@doc.consumes(doc.String(name='token'), location='header', required=True)
@authorized(token='12')
async def test(request):
    file_path = os.path.join(ABS_PATH, 'data.tsv')
    return await file_stream(file_path)



