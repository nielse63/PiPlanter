from unittest.mock import patch

from pyplanter.lib.tempterature import TemperatureData


def test_init():
    temperature = TemperatureData()
    assert temperature
    assert temperature.device


def test_get_data():
    temperature = TemperatureData()
    data = temperature.get_data()
    assert data["temperature"] and type(data["temperature"]) == float
    assert data["humidity"] and type(data["humidity"]) == float


@patch("adafruit_dht.DHT22")
def test_exit(mock_device):
    temperature = TemperatureData()
    temperature.exit()
    mock_device.assert_called_once()
