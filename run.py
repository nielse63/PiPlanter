#!/usr/bin/env python
# import threading
import time

from pyplanter.sensors.air_sensor import get_temperature_data, get_humidity_data
from pyplanter.sensors.soil_moisture_sensor import get_soil_moisture_value
from pyplanter.logger import logger

# from pyplanter.constants import (
#     RUNNER_TIMEOUT,
#     MIN_MOISTURE_LEVEL,
#     MIN_TEMPERATURE,
#     MIN_HUMIDITY,
# )


def calculate_optimal_value(value_min: float, value_max: float) -> float:
    difference = value_max - value_min
    return value_min + (difference / 2)


class Flower:
    # soil_moisture_min: float = 0.1
    # soil_moisture_max: float = 0.3
    # temperature_min: float = 65
    # temperature_max: float = 75
    # humidity_min: float = 80
    # humidity_max: float = 100
    # light_value: float = 0.5
    def __init__(self):
        self.soil_moisture_min: float = 0.1
        self.soil_moisture_max: float = 0.3
        self.temperature_min: float = 65
        self.temperature_max: float = 75
        self.humidity_min: float = 80
        self.humidity_max: float = 100
        self.light_value: float = 0.5

        self.optimal_soil_moisture = calculate_optimal_value(
            self.soil_moisture_min, self.soil_moisture_max
        )
        self.optimal_temperature = calculate_optimal_value(
            self.temperature_min, self.temperature_max
        )
        self.optimal_humidity = calculate_optimal_value(
            self.humidity_min, self.humidity_max
        )


def check_humidity(flower: Flower) -> float:
    humidity = get_humidity_data()
    # logger.debug(f"humidity value: {humidity}")

    if humidity < flower.humidity_min:
        logger.warning(f"humidity is too low: {humidity}")
    return humidity


def check_temperature(flower: Flower) -> float:
    temperature = get_temperature_data()
    # logger.debug(f"temperature value: {temperature}")

    if temperature < flower.temperature_min:
        logger.warning(f"temperature is too low: {temperature}")
    return temperature


def check_soil_moisture(flower: Flower) -> float:
    soil_moisture = get_soil_moisture_value()
    # logger.debug(f"soil moisture value: {soil_moisture}")

    if soil_moisture < flower.soil_moisture_min:
        logger.warning(f"low soil moisture: {soil_moisture}")
    return soil_moisture


def main() -> None:
    """
    Run all scripts on separate threads.

    Usage: python pyplanter/runner.py
    """
    logger.debug("starting piplanter runner")
    flower = Flower()

    while True:
        humidity = check_humidity(flower)
        temperature = check_temperature(flower)
        soil_moisture = check_soil_moisture(flower)
        logger.debug(
            f"humidity: {humidity} / temperature: {temperature} / soil_moisture: {soil_moisture}"
        )
        time.sleep(2)


if __name__ == "__main__":
    main()
