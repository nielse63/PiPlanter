import time
from datetime import datetime

from gpiozero import OutputDevice

from pyplanter.constants import GPIOPins
from pyplanter.logger import logger

"""
resources:

- https://gpiozero.readthedocs.io/en/stable/api_output.html#outputdevice
- https://github.com/ankitr42/gardenpi/blob/master/pumpcontroller.py
- https://www.randomgarage.com/2018/12/raspberry-pi-automated-irrigation-system.html

"""


class WaterPump:
    def __init__(self):
        # our relay module that controls the pump
        self.device = OutputDevice(
            GPIOPins.water_pump, active_high=True, initial_value=False
        )

    @property
    def is_running(self) -> bool:
        return self.device.value == 1

    def start(self):
        logger.info("Starting water pump")
        if self.is_running:
            return
        try:
            self.device.on()
        except Exception as error:
            logger.error(error)
            raise error

    def stop(self):
        logger.info("Stopping water pump")
        try:
            self.device.off()
        except Exception as error:
            logger.error(error)
            raise error

    def run(self, timeout: int = 15) -> None:
        if self.is_running:
            return
        self.start()
        time.sleep(timeout)
        self.stop()
        now = datetime.now()
        logger.info(f"Watered plants at {now}")


if __name__ == "__main__":
    water_pump = WaterPump()
    water_pump.start()
