from time import sleep

from pyplanter.enums import StateEnum
from pyplanter.logger import logger


class Pump:
    def __init__(self):
        self.state = StateEnum.STOPPED

    def start(self):
        logger.debug("pump starting")
        # sleep(3)
        # self.state = StateEnum.RUNNING
        # logger.debug("pump started")

    def stop(self):
        logger.debug("pump stopping")
        self.state = StateEnum.STOPPED
        sleep(2)
        logger.debug("pump stopped")
