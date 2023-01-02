from dataclasses import dataclass
from typing import Tuple, Literal


Destination = Tuple[str, int]
MessageType = Literal["JSON"]


@dataclass
class Preferences:
    destination: Destination
    encoding: str
    header_length: int
    threadpool_size: int
