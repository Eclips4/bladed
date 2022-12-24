from select import select
from socket import socket, AF_INET, SOCK_STREAM
from typing import List


def create_new_socket(protocol: int = AF_INET,
                      stream: int = SOCK_STREAM) -> socket:
    return socket(protocol, stream)


class Server:
    def __init__(self,
                 server_socket: socket,
                 protocol: int = AF_INET,
                 stream: int = SOCK_STREAM,
                 host: str = "localhost",
                 port: int = 8000,
                 bufsize: int = 1024) -> None:
        self._protocol = protocol
        self._stream = stream
        self.host = host
        self.port = port
        self.bufsize = bufsize
        self._sockets: List[socket] = []
        self._server_socket = server_socket

    def _accept(self, server_socket: socket) -> None:
        client_socket, client_address = server_socket.accept()
        print("Handle and accept connection from", client_address)
        self._sockets.append(client_socket)

    def _send(self, client_socket: socket) -> None:
        try:
            data = client_socket.recv(self.bufsize)
        except ConnectionError:
            data = None

        if data is not None:
            client_socket.send(data)
        else:
            self._sockets.remove(client_socket)
            client_socket.close()

    def _setup_server_socket(self) -> None:
        self._server_socket.bind((self.host, self.port))
        self._server_socket.setblocking(False)
        self._server_socket.listen()
        self._sockets.append(self._server_socket)

    def _run_polling(self) -> None:
        while True:
            readable_scokets, _, _ = select(self._sockets, [], [])
            for sock in readable_scokets:
                if sock is self._server_socket:
                    self._accept(sock)
                else:
                    self._send(sock)

    def start(self) -> None:
        self._setup_server_socket()
        try:
            self._run_polling()
        finally:
            self._server_socket.close()
            print("Server socket closed")
