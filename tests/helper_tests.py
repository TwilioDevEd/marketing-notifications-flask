import unittest
from marketing_notifications_python.view_helpers import redirect_to, view
from base import BaseTestCase
from flask import redirect, url_for, render_template


class ViewHelperTests(BaseTestCase):
    # Ensures 'redirect_to' redirect you to the same place as 'redirect'
    def test_redirect_to_redirects_to_same_location_of_redirect(self):
        # assert
        assert redirect_to('views.notifications').location == redirect(url_for('views.notifications')).location

    # Ensures 'redirect_to' redirect you to the same place as 'redirect' with routes params
    def test_redirect_to_redirects_to_same_location_of_redirect_with_route_params(self):
        # assert
        assert redirect_to('views.notifications').location == redirect(
            url_for('views.notifications')).location

    # Ensures 'view' renders the same template that 'render_template'
    def test_view_renders_the_same_template_as_render_template(self):
        # assert
        assert view('notifications') == render_template('notifications.html')


if __name__ == '__main__':
    unittest.main()
