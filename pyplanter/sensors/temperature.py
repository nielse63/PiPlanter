#!/usr/bin/env python
import adafruit_dht
import board

from typing import Union
from pyplanter.helpers import celcius_to_fahrenheit

device = adafruit_dht.DHT22(board.D4)


def get_temperature_data() -> Union[dict, None]:
    try:
        temperature_c = device.temperature
        temperature = celcius_to_fahrenheit(temperature_c)
        # timestamp = datetime.now(pytz.timezone(LOCAL_TIMEZONE))
        data = {
            "temperature": temperature,
            "humidity": device.humidity,
            # "timestamp": timestamp,
        }
        return data
    except RuntimeError:
        return None
    except Exception as error:
        device.exit()
        raise error
