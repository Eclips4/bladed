from typing import List
from ..events import Event
from ..context import Context
from ..middlewares import Middleware


class EventLoop:
    def __init__(self) -> None:
        self.middlewares: List[Middleware] = []

    def pre_event(self, event: Event, ctx: Context) -> None:
        for middleware in self.middlewares:
            if hasattr(middleware, "pre_event"):
                pre_event = getattr(middleware, "pre_event")
                pre_event(event, ctx)

    def post_event(self, event: Event, ctx: Context) -> None:
        for middleware in self.middlewares:
            if hasattr(middleware, "post_event"):
                post_event = getattr(middleware, "post_event")
                post_event(event, ctx)

    def register_middleware(self, middleware: Middleware) -> None:
        self.middlewares.append(middleware)

    def unregister_middleware(self, middleware: Middleware) -> None:
        self.middlewares.remove(middleware)
