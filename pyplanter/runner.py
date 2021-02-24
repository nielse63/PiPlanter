#!/usr/bin/env python
import threading

from pyplanter.temperature.script import main as temperature_main
from pyplanter.logger import logger


def main():
    """
    Run all scripts on separate threads.

    Usage: python pyplanter/scripts/all.py
    """
    logger.debug("running all scripts")
    threading.Thread(target=temperature_main).start()


if __name__ == "__main__":
    main()
