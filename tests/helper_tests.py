import unittest
from notifications.view_helpers import redirect_to, view
from .base import BaseTestCase
from flask import render_template


class ViewHelperTests(BaseTestCase):
    # Ensures 'redirect_to' redirect you to the same place as 'redirect'
    def test_redirect_to_redirects_to_same_location_of_redirect(self):
        # assert
        self.assertEqual(
            redirect_to(
                'notifications',
            ).location,
            'http://server.test/notifications',
        )

    # Ensures 'view' renders the same template that 'render_template'
    def test_view_renders_the_same_template_as_render_template(self):
        # assert
        self.assertEqual(view('notifications'), render_template('notifications.html'))


if __name__ == '__main__':
    unittest.main()
