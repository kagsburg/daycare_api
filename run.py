from flask_swagger_ui import get_swaggerui_blueprint
from app import app
SWAGGER_URL = '/swagger'

API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name":"DayCare API"
    },
    oauth_config=None,

)
app.register_blueprint(swaggerui_blueprint)
if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')