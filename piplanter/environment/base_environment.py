class BaseEnvironment:
    def __init__(self):
        self.sensor_value = None
        self.min_value = None
        self.max_value = None
        self.optimal_value = None
        self.is_in_range = None
        self.on_error = None
        self.input_sensor = None
        self.output_device = None
        self.device_state = None

    def read_value(self):
        pass

    def start_device(self):
        pass

    def stop_device(self):
        pass

    def save_to_log(self):
        pass

    def read_logs(self):
        pass

    def handle_error(self):
        pass
