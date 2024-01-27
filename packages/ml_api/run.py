from api.app import create_app
from api.config import DevelopmentConfig


application = create_app(
    config_object=DevelopmentConfig)

# RUN WITH : FLASK_APP=run.py flask run