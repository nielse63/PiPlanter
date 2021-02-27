import adafruit_dht
import board

from piplanter.sensors import BaseSensor
from piplanter.logger import logger


class TemperatureSensor(BaseSensor):
    def __init__(
        self,
        pin: board.pin.Pin = board.D4,
    ):
        super().__init__()
        self.pin = pin

        # cache the value to return old data if reading throws and error
        self._value: float = 0.0

        # save the sensor object on the class
        self.sensor = adafruit_dht.DHT22(pin)

    @property
    def value(self) -> float:
        try:
            # convert c to f
            self._value = self.sensor.temperature * (9 / 5) + 32
        except RuntimeError as error:
            logger.warning(f"DHT22: {error.args[0]}")
        except Exception as error:
            logger.error(f"DHT22: {error.args[0]}")
        return self._value
