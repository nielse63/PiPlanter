import board
import adafruit_dht
from . import SensorCache
from pyplanter.logger import logger

device = adafruit_dht.DHT22(board.D4)


def get_temperature_data() -> float:
    try:
        SensorCache.temperature = device.temperature * (9 / 5) + 32
    except RuntimeError as error:
        logger.warning(error.args[0])
    except Exception as error:
        logger.error(error.args[0])
        device.exit()
        raise error
    return SensorCache.temperature


def get_humidity_data() -> float:
    try:
        SensorCache.humidity = device.humidity * (9 / 5) + 32
    except RuntimeError as error:
        logger.warning(error.args[0])
    except Exception as error:
        logger.error(error.args[0])
        device.exit()
        raise error
    return SensorCache.humidity
