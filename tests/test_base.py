from src import Client
from unittest import TestCase


class TestCommon(TestCase):
    def test_hello_world(self):
        client = Client()
        assert client.send(b"hello") == b"Hello"
