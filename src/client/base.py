from contextlib import contextmanager
from socket import socket
from typing import Optional
from ..worker import SimpleWorker
from ..types import Preferences, MessageType


class Client(SimpleWorker):
    def __init__(self,
                 connection: socket,
                 preferences: Preferences,
                 message_type: MessageType,
                 ):
        super().__init__(connection, preferences, message_type)
        self.worker: Optional[SimpleWorker] = None

    @contextmanager
    def connect(self):
        try:
            self._connection.connect(self.preferences.destination)
            self.worker = SimpleWorker(self._connection, self.preferences, "JSON")
            yield self
        finally:
            self.worker._disconnect()
            self._connection.close()

    def send(self, msg: bytes):
        self.worker.send_message(msg)

    def receive_one_message(self):
        return self.worker._get_next_message()
