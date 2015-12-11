import os
from marketing_notifications_python.boostrap import get_app
from marketing_notifications_python.database import get_db

twilio_settings = {
    'app': None,
    'db': None,
}


def init_test_environment():
    os.environ["ENV"] = 'test'
    twilio_settings['app'] = get_app()
    twilio_settings['db'] = get_db()


def test_app():
    return twilio_settings['app']


def test_db():
    return twilio_settings['db']
