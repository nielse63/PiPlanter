#!/usr/bin/env python
import threading
import time

from pyplanter.sensors.air_sensor import get_temperature_data, get_humidity_data
from pyplanter.sensors.soil_moisture_sensor import get_soil_moisture_value
from pyplanter.logger import logger
from pyplanter.constants import (
    RUNNER_TIMEOUT,
    MIN_MOISTURE_LEVEL,
    MIN_TEMPERATURE,
    MIN_HUMIDITY,
)


def temperature_runner() -> None:
    while True:
        time.sleep(RUNNER_TIMEOUT)
        data = get_temperature_data()
        if not data:
            continue
        temperature = data["temperature"]
        humidity = data["humidity"]
        # logger.debug(f"temperature data: {data}")
        if temperature < MIN_TEMPERATURE:
            # TODO: when temp is below MIN_TEMPERATURE, turn on heater and run it until
            # the temp is right between the min and max thresholds
            logger.warning(f"temperature is too low: {temperature}")
        if humidity < MIN_HUMIDITY:
            # TODO: see the comment above, but apply the same actions to running a humidifier
            logger.warning(f"humidity is too low: {humidity}")


def soil_moisture_runner() -> None:
    soil_moisture = get_soil_moisture_value()
    # if data["voltage"] < 1:
    #     logger.warning("low sensor voltage ({:.2f}V)".format(data["voltage"]))
    if soil_moisture < MIN_MOISTURE_LEVEL:
        # TODO: when the value is too low, turn on the pump until the soil moisture
        # meets an acceptable level
        logger.warning(f"low soil moisture: {soil_moisture}")


def main() -> None:
    """
    Run all scripts on separate threads.

    Usage: python pyplanter/runner.py
    """
    logger.debug("running all scripts")
    threading.Thread(target=temperature_runner).start()
    threading.Thread(target=soil_moisture_runner).start()


if __name__ == "__main__":
    main()
