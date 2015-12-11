from marketing_notifications_python.twilio import account_sid, auth_token, phone_number
from twilio import twiml
from twilio.rest import TwilioRestClient


class TwilioServices:
    twilio_client = None

    def __init__(self):
        if TwilioServices.twilio_client is None:
            TwilioServices.twilio_client = TwilioRestClient(account_sid(), auth_token())

    def send_message(self, to, message, image_url):
        TwilioServices.twilio_client.messages.create(
            to=to,
            from_=phone_number(),
            body=message,
            media_url=image_url
        )

    def respond_message(self, message):
        response = twiml.Response()
        response.message(message)
        return response
