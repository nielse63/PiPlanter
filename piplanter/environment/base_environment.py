# from typing import Any
# from piplanter.flowers.base_flower import BaseFlower
from piplanter.sensors import BaseSensor
from piplanter.devices.base_device import BaseDevice
from piplanter.logger import logger


class BaseEnvironment:
    def __init__(
        self, name: str, sensor: BaseSensor, device: BaseDevice, value_range: list
    ):
        self.name = name
        self.sensor = sensor
        self.device = device
        self.value_range = value_range
        self.value_min = value_range[0]
        self.value_min = value_range[1]

        # self.sensor_value = None
        # self.min_value = None
        # self.max_value = None
        # self.optimal_value = None
        # self.is_in_range = None
        # self.on_error = None
        # self.input_sensor = None
        # self.output_device = None
        # self.device_state = None

    @property
    def sensor_value(self) -> float:
        return self.sensor.value

    @property
    def device_value(self) -> float:
        return self.device.value

    @property
    def value_below_range(self) -> bool:
        return self.sensor_value < self.value_min

    @property
    def value_above_range(self) -> bool:
        return self.sensor_value > self.value_min

    # def read_value(self):
    #     pass

    def turn_device_on(self):
        logger.
        pass

    def turn_device_off(self):
        pass

    # def save_to_log(self):
    #     pass

    # def read_logs(self):
    #     pass

    def handle_error(self):
        pass
