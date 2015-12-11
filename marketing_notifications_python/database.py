from flask.ext.sqlalchemy import SQLAlchemy
from marketing_notifications_python import get_env

dbs = {
    'test': None,
    'development': None,
}


def get_db():
    config_name = get_env()

    if dbs[config_name] is None:
        dbs[config_name] = SQLAlchemy()
    return dbs[config_name]
