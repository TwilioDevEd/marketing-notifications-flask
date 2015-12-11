from flask import Flask
from marketing_notifications_python import get_env
from marketing_notifications_python.config import config_env_files
from marketing_notifications_python.database import get_db
from marketing_notifications_python.views import construct_view_blueprint

apps = {
    'test': None,
    'development': None,
}


def get_app():
    config_name = get_env()

    if apps[config_name] is None:
        apps[config_name] = init_app(config_name, get_db())
    return apps[config_name]


def init_app(config_name, db):
    flask_app = Flask(__name__)
    _configure_app(flask_app, db, config_name)
    return flask_app


def _configure_app(flask_app, app_db=None, config_name='development'):
    flask_app.config.from_object(config_env_files[config_name])
    if app_db is not None:
        app_db.init_app(flask_app)

    flask_app.register_blueprint(construct_view_blueprint(flask_app, app_db))
