from gpiozero import MCP3008
from pyplanter.sensors import SensorCache
from pyplanter.logger import logger
from pyplanter.constants import GPIOPins


def get_soil_moisture_value() -> float:
    try:
        results = MCP3008(
            channel=GPIOPins.soil_moisture_channel,
            clock_pin=GPIOPins.soil_moisture_clock_pin,
            mosi_pin=GPIOPins.soil_moisture_mosi_pin,
            miso_pin=GPIOPins.soil_moisture_miso_pin,
            select_pin=GPIOPins.soil_moisture_select_pin,
        )
        SensorCache.soil_moisture = results.value
    except Exception as error:
        logger.error(error)
    return SensorCache.soil_moisture
