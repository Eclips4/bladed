from typing import Hashable, Any, Dict


class Context:
    def __init__(self, data: Dict[Hashable, Any]) -> None:
        self.data = data

    def __getattr__(self, key: Hashable) -> Any:
        return self.data[key]

    def __setattr__(self, key: Hashable, value: Any) -> None:
        self.data[key] = value

    def __delattr__(self, key: Hashable) -> None:
        self.data.pop(key)
