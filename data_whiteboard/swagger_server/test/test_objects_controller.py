# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.whiteboard_item import WhiteboardItem  # noqa: E501
from swagger_server.test import BaseTestCase


class TestObjectsController(BaseTestCase):
    """ObjectsController integration test stubs"""

    def test_add_object(self):
        """Test case for add_object

        adds a whiteboard item
        """
        body = WhiteboardItem()
        response = self.client.open(
            '/angrygoat/data_whiteboard/1.0.0/objects',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
