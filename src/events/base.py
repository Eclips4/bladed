from ..types import Destination


class Event:
    def __init__(self,
                 message: bytes,
                 destination: Destination) -> None:
        self._message = message
        self._destination = destination

    @property
    def message(self):
        return self._message

    @property
    def destination(self):
        return f"ip: {self._destination[0]} port: {self._destination[1]}"
