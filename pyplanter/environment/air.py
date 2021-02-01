import adafruit_dht
import board

from pyplanter.helpers import celcius_to_fahrenheit
from pyplanter.logger import logger

# source: https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup
# source: https://github.com/adafruit/Adafruit_CircuitPython_DHT/blob/master/examples/dht_simpletest.py


class Air:
    def __init__(self) -> None:
        # board.D4 references physical board pin 7, GPIO4
        self.device = adafruit_dht.DHT22(board.D4, use_pulseio=False)

    def get_temperature(self) -> float:
        logger.debug("getting temperature")
        try:
            return celcius_to_fahrenheit(self.device.temperature)
        except RuntimeError as error:
            logger.error(error.args[0])
        except Exception as error:
            self.device.exit()
            raise error

    def get_humidity(self) -> float:
        logger.debug("getting humidity")
        try:
            return celcius_to_fahrenheit(self.device.humidity)
        except RuntimeError as error:
            logger.error(error.args[0])
        except Exception as error:
            self.device.exit()
            raise error
