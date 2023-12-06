from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
app = Flask(__name__)
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, version='1.0', title='DayCare API', description='Description of your API')
# swagger = Swagger(app)
@api.route('/hello')
class HelloResource(Resource):
    def get(self):
        return {'message': 'Hello, World!'}


# Enable Swagger documentation
swagger = api.namespace('Swagger', description='Swagger Documentation')

from app import routes

# api.add_resource(routes.RegisterUsers, '/register')