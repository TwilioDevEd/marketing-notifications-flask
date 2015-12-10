from marketing_notifications_python import get_app, get_db
from flask.ext.testing import TestCase
from tests import initialize_test_environment

initialize_test_environment()
app = get_app()
db = get_db()


class BaseTestCase(TestCase):
    render_templates = False

    def create_app(self):
        return app

    def setUp(self):
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
