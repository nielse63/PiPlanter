#!/usr/bin/env bash
set -e

mkdir piplanter
mkdir piplanter/flowers
mkdir piplanter/sensors
mkdir piplanter/devices
mkdir piplanter/environment
touch piplanter/__init__.py
touch piplanter/helpers.py
touch piplanter/constants.py
touch piplanter/logger.py

touch piplanter/flowers/__init__.py
touch piplanter/flowers/base_flower.py
touch piplanter/flowers/pineapple.py
touch piplanter/flowers/orchid.py

touch piplanter/sensors/__init__.py
touch piplanter/sensors/base_sensor.py
touch piplanter/sensors/soil_moisture.py
touch piplanter/sensors/base_air_sensor.py
touch piplanter/sensors/temperature.py
touch piplanter/sensors/humidity.py
touch piplanter/sensors/light.py

touch piplanter/environment/__init__.py
touch piplanter/environment/base_environment.py
touch piplanter/environment/soil_moisture.py
touch piplanter/environment/temperature.py
touch piplanter/environment/humidity.py
touch piplanter/environment/light.py

touch piplanter/devices/__init__.py
touch piplanter/devices/base_device.py
touch piplanter/devices/humidifer.py
touch piplanter/devices/heater.py
touch piplanter/devices/light.py
touch piplanter/devices/water_pump.py
