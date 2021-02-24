#!/usr/bin/env python
import adafruit_dht
import board
import pytz
import time

from datetime import datetime
from pyplanter.constants import LOCAL_TIMEZONE, RUNNER_TIMEOUT
from pyplanter.helpers import celcius_to_fahrenheit
from pyplanter.logger import logger

device = adafruit_dht.DHT22(board.D4)


def get_temperature_data():
    temperature_c = device.temperature
    temperature = celcius_to_fahrenheit(temperature_c)
    timestamp = datetime.now(pytz.timezone(LOCAL_TIMEZONE))
    return {
        "temperature": temperature,
        "humidity": device.humidity,
        "timestamp": timestamp,
    }


def temperature_runner():
    """
    Get the temperature and humidity on an interval

    Usage: python pyplanter/scripts/temperature.py
    """
    while True:
        try:
            # Print the values to the serial port
            data = get_temperature_data()
            logger.debug(
                f"temperature (f): {data['temperature']}; humidity: {data['humidity']}"
            )

        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            logger.error(error.args[0])
            # time.sleep(RUNNER_TIMEOUT)
            # continue
        except Exception as error:
            device.exit()
            raise error
        time.sleep(RUNNER_TIMEOUT)


if __name__ == "__main__":
    temperature_runner()
