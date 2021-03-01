from typing import Callable
from pyplanter.devices.humidifier import Humidifier


def test_humidifier():
    humidifier = Humidifier()
    assert humidifier
    assert isinstance(humidifier.toggle, Callable)
    assert isinstance(humidifier.off, Callable)
