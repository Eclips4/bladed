from abc import ABC, abstractmethod
from typing import NoReturn, Any


class Worker(ABC):
    @abstractmethod
    def send_message(self, message: bytes) -> None:
        raise NotImplementedError

    @abstractmethod
    def run(self) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    def on_message(self, message: Any) -> None:
        raise NotImplementedError
