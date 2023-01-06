import json


def parse_data_json(data: bytes, encoding: str) -> bytes:
    decoded_data = data.decode(encoding)
    return str(json.loads(decoded_data)).encode()
