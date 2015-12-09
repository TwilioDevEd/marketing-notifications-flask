from marketing_notifications_python.twilio import account_sid, auth_token, phone_number
from twilio.rest import TwilioRestClient


class MessageSender:
    twilio_client = None

    def __init__(self):
        if MessageSender.twilio_client is None:
            MessageSender.twilio_client = TwilioRestClient(account_sid(), auth_token())

    def send(self, to, message, image_url):
        MessageSender.twilio_client.messages.create(
            to=to,
            from_=phone_number(),
            body=message,
            media_url=image_url
        )
