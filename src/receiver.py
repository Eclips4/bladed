from socket import socket
from dataclasses import dataclass
from typing import Callable, Protocol
from logging import getLogger

type Connector = socket


logger = getLogger(__name__)


@dataclass
class Rule:
    message_len: int
    delimiter: bytes
    extra_step: Callable[[bytes], bytes] | None = None


class Receiver(Protocol):
    rule: Rule
    connector: Connector

    def recv(self) -> bytes:
        ...


default_rule = Rule(
    message_len=512,  # Perhaps it isn't enough?
    delimiter=b"\r\n\r\n",
)
# TODO: Create an issue to discuss more appropriate delimiter. Probably, restructure
# mechanism of message separating


class DefaultReceiver(Receiver):
    def __init__(self, rule: Rule, connector: Connector) -> None:
        self.rule = rule
        self.connector = connector

    def recv(self) -> bytes:
        self.connector.listen()
        connection, address = self.connector.accept()
        logger.debug(f"Accepted connection from {connection}")
        chunks: list[bytes] = []
        while True:
            data = connection.recv(self.rule.message_len)
            if not data:
                continue
            if self.rule.delimiter in data:
                chunks.append(data[:data.find(self.rule.delimiter)])
                break
            chunks.append(data)
        connection.close()
        if self.rule.extra_step is not None:
            return self.rule.extra_step(b"".join(chunks))
        return b"".join(chunks)
