import board

from .temperature import TemperatureSensor
from piplanter.logger import logger


class HumiditySensor(TemperatureSensor):
    def __init__(
        self,
        pin: board.pin.Pin = board.D4,
    ):
        super().__init__(pin)

    @property
    def value(self) -> float:
        try:
            self._value = self.sensor.humidity
        except RuntimeError as error:
            logger.warning(f"DHT22 (humidity): {error.args[0]}")
        except Exception as error:
            logger.error(f"DHT22 (humidity): {error.args[0]}")
        return self._value
