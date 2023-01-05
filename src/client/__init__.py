from socket import socket, AF_INET, SOCK_STREAM
from .base import Client
from ..types import Preferences


__all__ = [
    "Client",
    "create_client"
]


def _create_and_setup_client_socket(preferences: Preferences) -> socket:
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.settimeout(preferences.timeout)
    return client_socket


def create_client(preferences: Preferences) -> Client:
    client_socket = _create_and_setup_client_socket(preferences)
    client = Client(client_socket, preferences, "JSON")
    return client
