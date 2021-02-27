from piplanter.environment.base_environment import BaseEnvironment


class Humidity(BaseEnvironment):
    def __init__(self):
        super().__init__()

        self.sensor_value = None
        self.min_value = None
        self.max_value = None
        self.optimal_value = None
        self.is_in_range = None
        self.on_error = None
        self.input_sensor = None
        self.output_device = None
        self.device_state = None

    def start_humidifier(self):
        pass

    def stop_humidifier(self):
        pass
