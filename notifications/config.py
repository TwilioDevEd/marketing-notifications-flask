import os

from dotenv import load_dotenv

load_dotenv()


class DefaultConfig(object):
    SECRET_KEY = '%^!@@*!&$8xdfdirunb52438#(&^874@#^&*($@*(@&^@)(&*)Y_)((+'
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
    TWILIO_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')


class DevelopmentConfig(DefaultConfig):
    DEBUG = True


class TestConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SERVER_NAME = 'server.test'


config_classes = {
    'testing': TestConfig,
    'development': DevelopmentConfig,
    'production': DefaultConfig,
}
