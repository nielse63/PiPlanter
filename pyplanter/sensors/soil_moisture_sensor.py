from gpiozero import MCP3008
from . import SensorCache
from pyplanter.logger import logger


def get_soil_moisture_value() -> float:
    try:
        results = MCP3008(
            channel=0, clock_pin=11, mosi_pin=10, miso_pin=9, select_pin=8
        )
        SensorCache.soil_moisture = results.value
    except Exception as error:
        logger.error(error)
    return SensorCache.soil_moisture
