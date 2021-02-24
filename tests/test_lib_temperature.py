from pyplanter.lib.tempterature import Temperature
from unittest.mock import patch


def test_init():
    temperature = Temperature()
    assert temperature
    assert temperature.device


def test_get_data():
    temperature = Temperature()
    data = temperature.get_data()
    assert data["temperature"] and type(data["temperature"]) == float
    assert data["humidity"] and type(data["humidity"]) == float


@patch("adafruit_dht.DHT22")
def test_exit(mock_device):
    temperature = Temperature()
    temperature.exit()
    mock_device.assert_called_once()
