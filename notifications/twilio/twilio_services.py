# from .twilio import account_sid, auth_token, phone_number
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client


class TwilioServices:
    twilio_client = None

    def __init__(self, account_sid, auth_token):
        if TwilioServices.twilio_client is None:
            TwilioServices.twilio_client = Client(account_sid, auth_token)

    def send_message(self, to, from_, message, image_url):
        self.twilio_client.messages.create(
            to=to, from_=from_, body=message, media_url=image_url
        )

    @staticmethod
    def respond_message(message):
        response = MessagingResponse()
        response.message(message)
        return response
