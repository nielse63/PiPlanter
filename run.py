#!/usr/bin/env python
import time
from threading import Thread

import dumper

from pyplanter.devices.heater import toggle_heater
from pyplanter.devices.humidifier import Humidifier
from pyplanter.devices.water_pump import WaterPump
from pyplanter.logger import logger
from pyplanter.sensors.air_sensor import get_humidity_data, get_temperature_data
from pyplanter.sensors.soil_moisture_sensor import get_soil_moisture_value


def calculate_optimal_value(value_min: float, value_max: float) -> float:
    difference = value_max - value_min
    return value_min + (difference / 2)


class Flower:
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


flower = Flower()


def humidity_runner() -> None:
    humidifier = Humidifier()
    while True:
        humidity = get_humidity_data()
        logger.debug(f"humidity: {humidity}")

        if not humidifier.is_running and humidity < flower.humidity_min:
            humidifier.toggle()
        elif humidifier.is_running and humidity > flower.optimal_humidity:
            humidifier.toggle()

        time.sleep(3)


def temperature_runner() -> None:
    while True:
        temperature = get_temperature_data()
        logger.debug(f"temperature: {temperature}")

        if temperature < flower.temperature_min:
            toggle_heater()

        time.sleep(3)


def soil_moisture_runner() -> None:
    water_pump = WaterPump()
    dumper.dump(water_pump)
    logger.debug("starting soil moisture runner")
    while True:
        soil_moisture = get_soil_moisture_value()
        logger.debug(f"soil moisture: {soil_moisture}")
        if soil_moisture < flower.soil_moisture_min:
            water_pump.run()
        time.sleep(3)


def main() -> None:
    """
    Run all scripts on separate threads.

    Usage: python pyplanter/runner.py
    """
    logger.info("Starting piplanter runner")

    # try:
    #     # Thread(name="soil_moisture", target=soil_moisture_runner).start()
    #     # Thread(name="temperature", target=temperature_runner).start()
    #     Thread(name="humidity", target=humidity_runner).start()
    # except Exception as error:
    #     logger.error(error)

    Thread(name="soil_moisture", target=soil_moisture_runner).start()
    Thread(name="temperature", target=temperature_runner).start()
    Thread(name="humidity", target=humidity_runner).start()


if __name__ == "__main__":
    main()
# if __name__ == "__main__":
#     try:
#         main()
#     except KeyboardInterrupt:
#         logger.info("User is exiting")
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)
