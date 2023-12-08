import socket
from src import DefaultReceiver, default_rule


def create_server(host: str = "localhost",
                  port: int = 8080) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))

        receiver = DefaultReceiver(rule=default_rule, connector=sock)
        print(receiver.recv())


if __name__ == '__main__':
    create_server()
