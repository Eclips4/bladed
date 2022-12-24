import logging


from src.server import Server, create_new_socket


logging.basicConfig(level=logging.INFO)


server = Server(create_new_socket())
server.start()