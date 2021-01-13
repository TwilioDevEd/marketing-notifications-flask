import unittest
from xml.etree import ElementTree

from .base import BaseTestCase
from notifications.twilio.twilio_services import TwilioServices


class TwilioServicesTests(BaseTestCase):
    # Ensures respond a message will contain a response with a message back
    def test_respond_message_contains_message_element(self):
        # arrange
        twilio_services = TwilioServices('fake account', 'fake token')
        # act
        message = "Message"
        response = str(twilio_services.respond_message(message))
        twiml = ElementTree.fromstring(response)

        # assert
        self.assertEqual(twiml.findall("./Message")[0].text, message)


if __name__ == '__main__':
    unittest.main()
