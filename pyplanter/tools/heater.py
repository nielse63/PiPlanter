from pyplanter.enums import StateEnum


class Heater:
    def __init__(self):
        self.state = StateEnum.STOPPED

    def turn_on(self):
        self.state = StateEnum.RUNNING

    def turn_off(self):
        self.state = StateEnum.STOPPED
