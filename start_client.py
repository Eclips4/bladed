import logging
from src import create_client
from src.config import load_config


def main():
    logging.basicConfig(level=logging.INFO)
    config = load_config("./config.sample.ini")
    client = create_client(config)
    with client.connect() as connected_client:
        connected_client.send("""{1: 1}""")
        response = connected_client.receive_one_message()
        logging.info("Message: %s", response)
        print("Response:", response)


if __name__ == '__main__':
    main()
