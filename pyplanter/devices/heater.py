# from pyplanter.constants import IFTTT_HEAT_ACTION
# from pyplanter.devices import iftt_webhook_action
from pyplanter.logger import logger


def toggle_heater() -> None:
    logger.info("Toggling heater")
    # iftt_webhook_action(IFTTT_HEAT_ACTION)


if __name__ == "__main__":
    toggle_heater()
