#!/usr/bin/env python
import threading

from pyplanter.scripts.light import main as light_main
from pyplanter.scripts.temperature import main as temperature_main
from pyplanter.logger import logger


def main():
    """
    Run all scripts on separate threads.

    Usage: python pyplanter/scripts/all.py
    """
    logger.debug("running all scripts")
    threading.Thread(target=light_main).start()
    threading.Thread(target=temperature_main).start()


if __name__ == "__main__":
    main()
