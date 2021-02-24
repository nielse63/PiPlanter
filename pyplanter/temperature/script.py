#!/usr/bin/env python
import time
from pyplanter.temperature.data import TemperatureData
from pyplanter.logger import logger
from pyplanter.constants import TEMPERATURE_TIMEOUT

temp = TemperatureData()


def main():
    """
    Get the temperature and humidity every two seconds.

    Usage: python pyplanter/scripts/temperature.py
    """
    while True:
        try:
            # Print the values to the serial port
            temp.get_data()
            temp.save()

        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            logger.error(error.args[0])
            time.sleep(TEMPERATURE_TIMEOUT)
            continue
        except Exception as error:
            temp.exit()
            raise error

        time.sleep(TEMPERATURE_TIMEOUT)


if __name__ == "__main__":
    main()
