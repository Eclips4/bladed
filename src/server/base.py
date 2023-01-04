from multiprocessing.pool import ThreadPool
from typing import Callable
from socket import socket, SHUT_RDWR
from ..worker import SimpleWorker
from ..types import Preferences


class ThreadPoolServer:
    def __init__(self,
                 preferences: Preferences,
                 core_handler: Callable,
                 socket_server: socket) -> None:
        self.workers_pool = ThreadPool(preferences.threadpool_size)
        self.preferences = preferences
        self.core_handler = core_handler
        self.socket_server = socket_server

    def run(self):
        try:
            self.socket_server.listen()
            while True:
                connection, address = self.socket_server.accept()
                worker = SimpleWorker(connection, self.preferences, "JSON")
                self.workers_pool.apply_async(func=self.core_handler, args=(worker,), kwds={"preferences": self.preferences})
        finally:
            self.socket_server.shutdown(SHUT_RDWR)
            self.socket_server.close()
