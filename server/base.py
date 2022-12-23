from socket import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
from typing import Any, Union


class Server:
    def __init__(self,
                 _socket: socket,
                 _selector: DefaultSelector,
                 bufsize: int,
                 event: Union[EVENT_READ, EVENT_WRITE],
                 ip: str = "localhost",
                 port: int = 1234) -> None:
        self._socket = _socket
        self._selector = _selector
        self.bufsize = bufsize
        self.event = event
        self.ip = ip
        self.port = port

    def read(self, conn: socket, _: Any) -> None:
        data = conn.recv(self.bufsize)
        if data:
            print("Echoing", repr(data), "to", conn)
            conn.send(data)
        else:
            print("Closing", conn)
            self._selector.unregister(conn)
            conn.close()

    def accept(self, sock: socket, _: Any):
        conn, addr = sock.accept()
        print("Accepted", conn, "from", addr)
        conn.setblocking(False)
        self._selector.register(conn, self.event, self.read)

    def setup_server(self) -> None:
        self._socket.bind((self.ip, self.port))
        self._socket.listen(100)
        self._socket.setblocking(False)
        self._selector.register(self._socket, self.event, self.accept)

    def start(self):
        self.setup_server()
        while True:
            events = self._selector.select()
            for key, mask in events:
                callback = key.data
                callback(key.fileobj, mask)


s = Server(
    socket(),
    DefaultSelector(),
    1024,
    EVENT_READ,
)
s.start()
_=  "sssddedddddsswwwwwwwwsz"