import adafruit_dht
import board

from pyplanter.logger import logger
from pyplanter.sensors import SensorCache

# import dumper


device = adafruit_dht.DHT22(board.D4)
# cache = SensorCache()


# def get_sensor_data(key: str) -> float:
#     try:
#         dumper.dump(device)
#         if key not in device:
#             raise RuntimeError(f"Invalid DHT22 data key: {key}")
#         value = device[key]
#         if value is None:
#             raise RuntimeError(f"Invalid response from device: {key} is None")
#     except RuntimeError as error:
#         logger.warning(error.args[0])
#     except Exception as error:
#         logger.error(error.args[0])
#         device.exit()
#         raise error
#     return value


def get_temperature_data() -> float:
    try:
        value = device.temperature * (9 / 5) + 32
        if value is None:
            logger.error("Invalid response from device: temperature is None")
            if SensorCache.temperature is not None:
                return SensorCache.temperature
        return value
    except RuntimeError as error:
        logger.warning(error.args[0])
    except Exception as error:
        logger.error(error.args[0])
        device.exit()
        raise error
    return SensorCache.temperature


def get_humidity_data() -> float:
    try:
        value = device.humidity
        if value is None:
            logger.error("Invalid response from device: humidity is None")
            if SensorCache.humidity is not None:
                return SensorCache.humidity
        return value
    except RuntimeError as error:
        logger.warning(error.args[0])
    except Exception as error:
        logger.error(error.args[0])
        device.exit()
        raise error
    return SensorCache.humidity
