from configparser import ConfigParser
from .types import Preferences


def load_config(path: str) -> Preferences:
    config = ConfigParser()
    config.read(path)
    config_data = config['preferences']
    return Preferences(
        destination=(config_data['ip'],
                     int(config_data['port'])
                     ),
        encoding=config_data['encoding'],
        header_length=int(config_data['header_length'])
    )
