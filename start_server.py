import logging
from src.config import load_config
from src.server import create_server


def main():
    logging.basicConfig(level=logging.INFO)
    config = load_config("./config.sample.ini")
    server = create_server(config)
    server.run()


if __name__ == '__main__':
    main()
