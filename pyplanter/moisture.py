#!/usr/bin/python
import time
import pytz

from datetime import datetime
from gpiozero import MCP3008
from pyplanter.logger import logger
from pyplanter.constants import LOCAL_TIMEZONE, RUNNER_TIMEOUT


def get_moisture_value() -> float:
    results = MCP3008(channel=0, clock_pin=11, mosi_pin=10, miso_pin=9, select_pin=8)
    return results.value


def to_dict(value: float) -> dict:
    timestamp = datetime.now(pytz.timezone(LOCAL_TIMEZONE))
    return {
        "timestamp": timestamp,
        "percent": float("{:.2f}".format(value * 100)),
        "value": value,
    }


def main() -> dict:
    value = get_moisture_value()
    data = to_dict(value)
    return data


def soil_moisture_runner() -> None:
    while True:
        try:
            data = main()
            logger.debug(f"current soil moisture: {data['percent']}% ({data['value']})")
        except Exception as error:
            logger.error(error.args[0])
        time.sleep(RUNNER_TIMEOUT)


if __name__ == "__main__":
    soil_moisture_runner()
