import logging
from multiprocessing.pool import ThreadPool
from typing import Callable
from socket import socket
from ..worker import SimpleWorker
from ..types import Preferences


logger = logging.getLogger(__name__)


class ThreadPoolServer:
    def __init__(self,
                 preferences: Preferences,
                 core_handler: Callable,
                 server_socket: socket) -> None:
        self.workers_pool = ThreadPool(preferences.threadpool_size)
        self.preferences = preferences
        self.core_handler = core_handler
        self.server_socket = server_socket

    def run(self):
        try:
            self.server_socket.listen()
            logger.info("Server listening on %s", self.preferences.destination)
            while True:
                connection, address = self.server_socket.accept()
                worker = SimpleWorker(connection, self.preferences, "JSON")
                self.workers_pool.apply_async(func=self.core_handler, args=(worker,))
        finally:
            self.server_socket.close()
