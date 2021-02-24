#!/usr/bin/env python
import threading

from pyplanter.temp_and_humidity import temperature_runner
from pyplanter.moisture import soil_moisture_runner
from pyplanter.logger import logger


def main():
    """
    Run all scripts on separate threads.

    Usage: python pyplanter/scripts/all.py
    """
    logger.debug("running all scripts")
    threading.Thread(target=temperature_runner).start()
    threading.Thread(target=soil_moisture_runner).start()


if __name__ == "__main__":
    main()
