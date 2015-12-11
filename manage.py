from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from marketing_notifications_python.bootstrap import get_app
from marketing_notifications_python.database import get_db

app = get_app()
db = get_db()

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
