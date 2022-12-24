from socket import socket


class Client:
    def __init__(
            self,
            bufsize: int = 1024,
            ip: str = "localhost",
            port: int = 8000
    ):
        self.bufsize = bufsize
        self.ip = ip
        self.port = port

    def send(self, msg: bytes = b"Hello") -> bytes:
        sock = socket()
        try:
            sock.connect((self.ip, self.port))
            sock.sendall(msg)
            data = sock.recv(self.bufsize)
            return data
        except ConnectionError:
            return b"Connection Erorr"
        finally:
            sock.close()
