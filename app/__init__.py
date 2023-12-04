from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
app = Flask(__name__)

# SWAGGER_URL = '/swagger'

# API_URL = '../static/swagger.json'
# swaggerui_blueprint = get_swaggerui_blueprint(
#     SWAGGER_URL,
#     API_URL,
#     config={
#         "app_name":"DayCare API"
#     },
#     oauth_config=None,

# )

# app.register_blueprint(swaggerui_blueprint)

from app import routes