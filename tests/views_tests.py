import unittest
import xml.etree.ElementTree as ElementTree
from base import BaseTestCase


class ViewsTests(BaseTestCase):
    # Ensures route '/' renders notifications view
    def test_default_route_should_render_default_view(self):
        # act
        self.client.get('/')

        # assert
        self.assert_template_used('notifications.html')

    # Ensures post action to route '/notifications' with missing image url renders view errors
    def test_post_to_message_should_respond_with_message(self):
        # act
        response = self.client.post('/message', data=dict(
            From='+1555555555',
            Body=''
        ))
        twiml = ElementTree.fromstring(response.data)

        # assert
        assert len(twiml.findall("./Message")) == 1


if __name__ == '__main__':
    unittest.main()
