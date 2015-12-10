import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from marketing_notifications_python.config import config_env_files

SUBSCRIBE_COMMAND = "subscribe"
UNSUBSCRIBE_COMMAND = "unsubscribe"

apps = {
    'test': None,
    'development': None,
}

dbs = {
    'test': None,
    'development': None,
}


def get_env():
    return os.getenv('ENV', 'development')


def get_db():
    config_name = get_env()

    if dbs[config_name] is None:
        dbs[config_name] = SQLAlchemy()
    return dbs[config_name]


def get_app():
    config_name = get_env()

    if apps[config_name] is None:
        apps[config_name] = Flask(__name__)
    db = get_db()
    _configure_app(apps[config_name], db, config_name)
    return apps[config_name]


def _configure_app(flask_app, app_db=None, config_name='development'):
    flask_app.config.from_object(config_env_files[config_name])
    if app_db is not None:
        app_db.init_app(flask_app)

    import marketing_notifications_python.views
