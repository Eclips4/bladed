from json import loads
from typing import Any


def parse_data_json(data: bytes, encoding: str) -> Any:
    decoded_data = data.decode(encoding)
    return loads(decoded_data)
