from ..exceptions import TooSmallCapacity


def make_header(length: int,
                encoding: str,
                header_length: int
                ) -> bytes:
    encoded_length = str(length).encode(encoding)
    free_space = header_length - len(encoded_length)
    if free_space >= 0:
        return encoded_length + b" " * free_space
    raise TooSmallCapacity


def get_message_length(header: bytes, encoding: str) -> int:
    header_decoded = header.decode(encoding)
    return int(header_decoded)
