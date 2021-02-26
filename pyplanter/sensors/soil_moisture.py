#!/usr/bin/python
from gpiozero import MCP3008


def read_moisture_sensor() -> MCP3008:
    results = MCP3008(
        channel=0, clock_pin=11, mosi_pin=10, miso_pin=9, select_pin=8
    )
    return results


def to_dict(results: MCP3008) -> dict:
    # timestamp = datetime.now(pytz.timezone(LOCAL_TIMEZONE))
    value = results.value
    return {
        # "timestamp": timestamp,
        # "percent": value * 100,
        "value": value,
        "raw_value": results.raw_value,
        "voltage": results.voltage,
    }


def get_soil_moisture_data() -> dict:
    results = read_moisture_sensor()
    return to_dict(results)
