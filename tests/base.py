from unittest import TestCase

from notifications import app, db


class BaseTestCase(TestCase):
    render_templates = False

    def setUp(self):
        self.client = app.test_client()
        app.app_context().push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def assert_flashes(self, expected_message, expected_category='message'):
        with self.client.session_transaction() as session:
            try:
                category, message = session['_flashes'][0]
            except KeyError:
                raise AssertionError('nothing flashed')
            assert expected_message in message
            assert expected_category == category
