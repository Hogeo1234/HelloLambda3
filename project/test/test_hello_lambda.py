import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from hello_lambda import handler


def test_handler_returns_200():
    event = {}
    context = None
    result = handler(event, context)
    assert result['statusCode'] == 200


def test_handler_body_is_ok():
    event = {}
    context = None
    result = handler(event, context)
    body = json.loads(result['body'])
    assert body == 'OK'
