from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from marketing_notifications_python.config import config_env_files

SUBSCRIBE_COMMAND = "subscribe"
UNSUBSCRIBE_COMMAND = "unsubscribe"


def configure_app(flask_app, app_db, config_name='development'):
    flask_app.config.from_object(config_env_files[config_name])
    app_db.init_app(flask_app)


app = Flask(__name__)
db = SQLAlchemy()
import marketing_notifications_python.views

configure_app(app, db)
