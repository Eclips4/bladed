import logging
from collections import deque
from socket import socket
from logging import getLogger
from .worker_types import Worker
from ..types import Preferences, MessageType
from ..messages import create_message, get_message_length, parse_data_json
from typing import Any, Optional, Callable


logger = getLogger(__name__)


class SimpleWorker(Worker):
    def __init__(self,
                 connection: socket,
                 preferences: Preferences,
                 message_type: MessageType,
                 on_message: Optional[Callable] = None
                 ) -> None:
        self.message_type = message_type
        self._connection = connection
        self.preferences = preferences
        self._buffer = deque()
        self._on_message = on_message

    def send_message(self, message: bytes) -> None:
        logger.info("Send message: %s", message)
        sended = 0
        to_send = create_message(message,
                                 self.message_type,
                                 self.preferences.encoding,
                                 self.preferences.header_length)

        while sended < len(to_send):
            sended += self._connection.send(to_send[sended:])
        logging.info("Message was successfully sent.")

    def _receive(self, length: int) -> bytes:
        collected = b""
        while len(collected) < length:
            if self._buffer:
                collected += self._buffer.popleft()
            else:
                collected += self._connection.recv(length - len(collected))
        if len(collected) > length:
            if self._buffer:
                self._buffer.appendleft(collected[length:])
            else:
                self._buffer.append(collected[length:])
        return collected

    def _get_next_message(self) -> Any:
        logger.info("Try to get next message")
        header = self._receive(self.preferences.header_length)
        msg_length = get_message_length(header, self.preferences.encoding)
        msg = self._receive(msg_length)
        message_parsed = parse_data_json(msg, self.preferences.encoding)
        return message_parsed

    def _disconnect(self):
        self._connection.shutdown(1)
        self._connection.close()
        logger.info("Connection was closed")

    def on_message(self, message: Any) -> None:
        self._on_message(message)

    def run(self):
        while True:
            try:
                msg = self._get_next_message()
                logger.info("Server got message: %s", msg)
                self.on_message(msg)
            finally:
                self._disconnect()
