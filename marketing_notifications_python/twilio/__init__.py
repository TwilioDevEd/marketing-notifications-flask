from marketing_notifications_python import app


def auth_token():
    return app.config['TWILIO_AUTH_TOKEN']


def phone_number():
    return app.config['TWILIO_NUMBER']


def account_sid():
    return app.config['TWILIO_ACCOUNT_SID']
