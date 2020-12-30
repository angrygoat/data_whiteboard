import connexion
import six

from ..models.whiteboard_item import WhiteboardItem  # noqa: E501
from swagger_server import util


def add_object(body=None):  # noqa: E501
    """adds a whiteboard item

    Adds an item to the system # noqa: E501

    :param body: whiteboard item to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = WhiteboardItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
