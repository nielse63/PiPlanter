class BaseSensor:
    def __init__(self):
        self.name = None
        self.status = None
        self.value = None
        self.voltage = None

    def get_value(self):
        pass

    def get_status(self):
        pass

    def get_voltage(self):
        pass
