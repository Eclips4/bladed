from typing import Tuple
from dataclasses import dataclass

Destination = Tuple[str, int]


@dataclass
class Preferences:
    destination: Destination
    encoding: str
