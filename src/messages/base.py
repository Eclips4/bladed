from ..types import MessageType
from .json import serialize_data_json


def create_message(message: bytes,
                   message_type: MessageType,
                   encoding: str,
                   header_length: int):
    if message_type == "JSON":
        return serialize_data_json(message, encoding, header_length)
    raise NotImplementedError(
        "Message type %s isn't supported." % message_type
    )
