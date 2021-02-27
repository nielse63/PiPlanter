# type: ignore
from piplanter.sensors import *


def test_base_sensor():
    sensor = BaseSensor()
    assert sensor
    assert sensor.value == 0
    assert sensor.voltage == 0
    assert sensor.sensor is None
