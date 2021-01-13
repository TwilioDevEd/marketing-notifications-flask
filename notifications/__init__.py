from flask import Flask

from .database import db, migrate
from .views import init_views
from .config import config_classes

# create and configure the app
app = Flask(__name__, instance_relative_config=True)

# load the instance config, if it exists, when not testing
env = app.config.get("ENV")
app.config.from_object(config_classes[env])

db.init_app(app)
migrate.init_app(app, db)

import notifications.models  # noqa E402

init_views(app)
