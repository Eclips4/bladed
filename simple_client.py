import socket


def send_message_to_server(host: str = "localhost",
                           port: int = 8080,
                           data: bytes = b"It's data! \r\n\r\n") -> None:

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.send(data)


if __name__ == '__main__':
    send_message_to_server()