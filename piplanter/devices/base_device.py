class BaseDevice:
    def __init__(self):
        self.is_on = None
        self.value = None
        self.state = None
        self.errors = None
        self.on_error = None

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
