from socket import (
    socket,
    AF_INET,
    AF_INET6,
    SOCK_STREAM,
    SOCK_DGRAM,
    SOCK_RAW,
    SOCK_RDM,
    SOCK_SEQPACKET,
)
from typing import Union

Family = Union[
    AF_INET,
    AF_INET6]

Type = Union[
    SOCK_STREAM,
    SOCK_DGRAM,
    SOCK_RAW,
    SOCK_RDM,
    SOCK_SEQPACKET
]


class Client:
    def __init__(
            self,
            bufsize: int,
            ip: str = "localhost",
            port: int = 1234
    ):
        self.bufsize = bufsize
        self.ip = ip
        self.port = port

    def send(self, msg: bytes = b"Hello"):
        sock = socket()
        sock.connect((self.ip, self.port))
        sock.sendall(msg)
        data = sock.recv(self.bufsize)
        sock.close()
        return data


