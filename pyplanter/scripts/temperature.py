#!/usr/bin/env python
import time
from pyplanter.lib.tempterature import Temperature
from pyplanter.logger import logger
from pyplanter.constants import TEMPERATURE_TIMEOUT

temp = Temperature()


def main():
    """
    Get the temperature and humidity every two seconds.

    Usage: python pyplanter/scripts/temperature.py
    """
    while True:
        try:
            # Print the values to the serial port
            data = temp.get_data()
            temperature_c = data["temperature_c"]
            temperature_f = data["temperature_f"]
            humidity = data["humidity"]
            logger.debug(
                "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                    temperature_f, temperature_c, humidity
                )
            )

        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            logger.error(f"ERROR: {error.args[0]}")
            time.sleep(TEMPERATURE_TIMEOUT)
            continue
        except Exception as error:
            temp.exit()
            raise error

        time.sleep(TEMPERATURE_TIMEOUT)


if __name__ == "__main__":
    main()
