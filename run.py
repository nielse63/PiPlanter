#!/usr/bin/env python
import time
import atexit
from threading import Thread, Timer

from pyplanter.devices.heater import toggle_heater
from pyplanter.devices.humidifier import Humidifier
from pyplanter.devices.water_pump import WaterPump
from pyplanter.logger import logger
from pyplanter.plants.base_plant import BasePlant
from pyplanter.plants.orchid import Orchid
from pyplanter.sensors.air_sensor import get_humidity_data, get_temperature_data
from pyplanter.sensors.soil_moisture_sensor import get_soil_moisture_value

humidifier = Humidifier()


def on_exit():
    humidifier.off()


atexit.register(on_exit)


def humidity_runner(plant: BasePlant) -> None:
    while True:
        humidity = get_humidity_data()
        logger.debug(
            f"humidity: {humidity} / humidifier.is_running: {humidifier.is_running}"
        )

        if not humidifier.is_running and humidity < plant.humidity_min:
            humidifier.toggle()
        elif humidifier.is_running and humidity > plant.optimal_humidity:
            humidifier.toggle()

        time.sleep(3)


def temperature_runner(plant: BasePlant) -> None:
    while True:
        temperature = get_temperature_data()
        logger.debug(f"temperature: {temperature}")

        if temperature < plant.temperature_min:
            toggle_heater()

        time.sleep(3)


def soil_moisture_runner(plant: BasePlant) -> None:
    water_pump = WaterPump()
    logger.debug("starting soil moisture runner")
    while True:
        soil_moisture = get_soil_moisture_value()
        logger.debug(f"soil moisture: {soil_moisture}")
        if soil_moisture < plant.soil_moisture_min:
            water_pump.run()
        time.sleep(3)


def main() -> None:
    """
    Run all scripts on separate threads.

    Usage: python pyplanter/runner.py
    """
    logger.info("Starting piplanter runner")

    plant = Orchid()
    Thread(target=soil_moisture_runner, args=[plant]).start()
    Timer(1, function=temperature_runner, args=[plant]).start()
    Timer(2, function=humidity_runner, args=[plant]).start()


if __name__ == "__main__":
    main()
