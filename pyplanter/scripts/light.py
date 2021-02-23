#!/usr/bin/env python
import time

from pyplanter.logger import logger
from pyplanter.lib.light import Light


def main():
    """
    Get the sunrise and sunset data for the day

    Usage: python pyplanter/scripts/light.py
    """
    while True:
        logger.debug("Updating light data")
        light = Light()
        light.get_latest_data()
        light.save()

        time.sleep(60)


if __name__ == "__main__":
    main()
