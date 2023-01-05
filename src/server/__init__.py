from socket import socket, AF_INET, SOCK_STREAM
from .base import ThreadPoolServer
from ..types import Preferences
from ..handlers import run_echo_handler


__all__ = [
    "ThreadPoolServer",
    "create_server"
]


def _create_and_setup_server_socket(preferences: Preferences) -> socket:
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.settimeout(preferences.timeout)
    server_socket.bind(preferences.destination)
    return server_socket


def create_server(preferences: Preferences) -> ThreadPoolServer:
    server_socket = _create_and_setup_server_socket(preferences)
    threadpool_server = ThreadPoolServer(
        preferences,
        run_echo_handler,
        server_socket
    )
    return threadpool_server

