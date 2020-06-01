from sanic import Sanic
from sanic.response import json
from sanic_openapi import doc, swagger_blueprint

from util import authorized


app = Sanic(__name__)

app.config["API_TITLE"] = "My-DataHub-OpenAPI"
app.config["API_VERSION"] = "0.1.0"
app.config["API_DESCRIPTION"] = "An example Swagger from Sanic-OpenAPI"
app.config["API_CONTACT_EMAIL"] = "cagojeiger@naver.com"
app.config["API_TERMS_OF_SERVICE"] = "https://github.com/kangheeyong/PROJECT-datahub-api-server.git"
app.config["API_LICENSE_NAME"] = "MIT LICENSE"
app.blueprint(swagger_blueprint)


class Test_status:
    status = doc.String()


@app.route('/test')
@doc.tag('test')
@doc.summary('test koken')
@doc.description('This is a test route with detail description.')
@doc.consumes(doc.String(name='token'), location='header', required=True)
@doc.response(200, Test_status, description='한글도 되나?')
@doc.response(403, Test_status, description='123aaa')
@authorized(token='12')
async def test(request):
    return json({'status': 'success'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8070)



