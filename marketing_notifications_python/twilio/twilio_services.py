from marketing_notifications_python.twilio import account_sid, auth_token, phone_number
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client


class TwilioServices:
    twilio_client = None

    def __init__(self):
        if TwilioServices.twilio_client is None:
            self.twilio_client = Client(account_sid(), auth_token())

    def send_message(self, to, message, image_url):
        self.twilio_client.messages.create(
            to=to,
            from_=phone_number(),
            body=message,
            media_url=image_url
        )

    def respond_message(self, message):
        response = MessagingResponse()
        response.message(message)
        return response
