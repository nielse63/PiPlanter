from typing import Any


class BaseSensor(object):
    """
    Abstraction of a sensor. This is the super class for the sensors.
    """

    def __init__(self) -> None:
        self.value: float = 0
        self.voltage: float = 0
        self.sensor: Any = None
