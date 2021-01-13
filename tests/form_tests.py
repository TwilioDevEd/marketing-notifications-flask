from notifications.forms import SendMessageForm
from .base import BaseTestCase


class FormTests(BaseTestCase):
    # Ensures populate SenMessageForm with missing message filed give an error
    def test_populate_SendMessageForm_with_missing_message_should_produce_error(self):
        # arrange
        form = SendMessageForm(message='', imageUrl='')

        # assert
        self.assertFalse(form.validate())
        self.assertIn('Message is required', form.message.errors)

    # Ensures populate SenMessageForm with missing imageUrl filed give an error
    def test_populate_SendMessageForm_with_missing_imageUrl_should_produce_error(self):
        # arrange
        form = SendMessageForm(message='Test', imageUrl='')

        # assert
        self.assertFalse(form.validate())
        self.assertIn('Image URL is required', form.imageUrl.errors)
