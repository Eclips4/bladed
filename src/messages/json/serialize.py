from json import dumps
from ..header import make_header


def serialize_data_json(data: str | bytes, encoding: str, header_length: int) -> bytes:
    if isinstance(data, bytes):
        data = data.decode()
    encoded_data = dumps(data).encode(encoding)
    header = make_header(len(encoded_data), encoding, header_length)
    return header + encoded_data
