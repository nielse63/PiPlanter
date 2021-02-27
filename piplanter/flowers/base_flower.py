from piplanter.sensors import BaseSensor
from piplanter.devices.base_device import BaseDevice
from piplanter.logger import logger


class BaseFlower:
    # soil_moisture_min: float = 0.0
    # soil_moisture_max: float = 0.0
    # temperature_min: int = 0
    # temperature_max: int = 0
    # humidity_min: float = 0.0
    # humidity_max: float = 0.0
    # light_value: float = 0.0

    def __init__(
        self,
        name: str,
        # sensor: BaseSensor,
        device: BaseDevice,
        soil_moisture_min: float = 0.0,
        soil_moisture_max: float = 0.0,
        temperature_min: int = 0,
        temperature_max: int = 0,
        humidity_min: float = 0.0,
        humidity_max: float = 0.0,
        light_value: float = 0.0,
        # **kwargs,
    ):
        self.name = name
        self.environment = None

        # sensors
        self.temperature_sensor = None
        self.humidity_sensor = None
        self.soil_moisture_sensor = None
        self.light_sensor = None

        self.device = device
        self.soil_moisture_min = soil_moisture_min
        self.soil_moisture_max = soil_moisture_max
        self.temperature_min = temperature_min
        self.temperature_max = temperature_max
        self.humidity_min = humidity_min
        self.humidity_max = humidity_max
        self.light_value = light_value

        # for key, value in kwargs.items():
        #     self[key] = value

    @property
    def needs_water(self) -> bool:
        """
        Determine if the soil has a high enough moisture content.

        :return: Whether or not the flower needs water.
        """
        return self.sensor.value < self.soil_moisture_min

    @property
    def needs_humidity(self) -> bool:
        """
        Determine if the soil has a high enough moisture content.

        :return: Whether or not the flower needs water.
        """
        return self.sensor.value < self.soil_moisture_min

    @property
    def needs_heat(self) -> bool:
        """
        Whether or not the plant has enough heat.

        :return: True when the temperature sensor value is below the minimum temperature required by the plant.
        :rtype: bool
        """
        return self.sensor

    def watch_environment(self):
        """Start a runner to watch the plant's environment.

        Get the value of each sensor passed to the plan in an infinite loop, sleeping for 1 second after each iteration, and using those values we determine if we need to turn on/off the devices that manage that part of the environment.

        For example: if the soil moisture sensor says that the value is below the minimum desire amount of water, the flower is going to turn on the water pump. Each sensor has an associated device.

        """
        pass
