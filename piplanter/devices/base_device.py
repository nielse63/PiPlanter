from typing import Callable


class BaseDevice:
    def __init__(self):
        self.is_on: bool = None
        self.value: float = None
        self.state = None
        self.errors: list = None
        self.on_error: Callable = None

    def start(self):
        pass

    def stop(self):
        pass

    def save_log(self):
        pass

    def read_log(self):
        pass

    def handle_error(self):
        pass
