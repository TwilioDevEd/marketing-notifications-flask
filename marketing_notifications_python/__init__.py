from flask import Flask
from marketing_notifications_python.config import config_env_files


def configure_app(new_app, config_name='development'):
    # new_app = Flask(__name__)
    new_app.config.from_object(config_env_files[config_name])


app = Flask(__name__)
import marketing_notifications_python.views

configure_app(app)