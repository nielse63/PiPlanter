from pyplanter.constants import IFTTT_HEAT_ACTION
from pyplanter.devices import iftt_webhook_action


def toggle_heater() -> None:
    iftt_webhook_action(IFTTT_HEAT_ACTION)


if __name__ == "__main__":
    toggle_heater()
