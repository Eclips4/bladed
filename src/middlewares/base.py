import logging
from ..events import Event
from ..context import Context


logger = logging.getLogger(__name__)


class Middleware:
    def pre_event(self,
                  event: Event,
                  ctx: Context) -> None:
        ...

    def post_event(self,
                   event: Event,
                   ctx: Context) -> None:
        ...


class LoggingMiddleware(Middleware):
    def pre_event(self,
                  event: Event,
                  ctx: Context) -> None:
        logger.info("Message: %s, ctx: %s", event.message, ctx.data)
