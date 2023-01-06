import json
from ..header import make_header


def serialize_data_json(data: bytes,
                        encoding: str,
                        header_length: int) -> bytes:
    encoded_data = json.dumps(data.decode(encoding)).encode(encoding)
    header = make_header(len(encoded_data), encoding, header_length)
    return header + encoded_data
