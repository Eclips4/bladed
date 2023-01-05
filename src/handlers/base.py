import logging
from typing import Any
from ..worker import Worker


logger = logging.getLogger(__name__)


class BaseHandler:
    def __init__(self, worker: Worker):
        self.worker = worker
        self.worker.on_message = self.handle_message

    def handle_message(self, message: Any):
        logger.info("Collback got message: %s", message)
        self.worker.send_message(message)


def run_echo_handler(worker: Worker):
    worker.on_message = BaseHandler(worker).handle_message
    worker.run()
