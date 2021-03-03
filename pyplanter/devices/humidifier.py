from pyplanter.constants import IFTTT_HUMIDIFIER_ACTION
from pyplanter.devices import iftt_webhook_action
from pyplanter.logger import logger


class Humidifier:
    def __init__(self):
        self.is_running = False

    def toggle(self) -> None:
        logger.info(
            f"Toggling humidifier state (is_running = {self.is_running})"
        )
        self.is_running = False if self.is_running else True
        iftt_webhook_action(IFTTT_HUMIDIFIER_ACTION)

    def off(self) -> None:
        if self.is_running:
            logger.info("Turning off humidifier")
            self.toggle()
