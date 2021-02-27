from pyplanter.constants import IFTTT_HUMIDIFIER_ACTION
from pyplanter.devices import iftt_webhook_action


class Humidifier:
    def __init__(self):
        self.is_running = False

    def toggle(self) -> None:
        self.is_running = False if self.is_running else True
        iftt_webhook_action(IFTTT_HUMIDIFIER_ACTION)


# if __name__ == "__main__":
#     toggle_humidifier()
