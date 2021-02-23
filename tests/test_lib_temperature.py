from pyplanter.lib.tempterature import Temperature
from unittest.mock import patch


def test_init():
    temperature = Temperature()
    assert temperature
    assert temperature.device


def test_get_data():
    temperature = Temperature()
    data = temperature.get_data()
    assert data["temperature_c"]
    assert data["temperature_f"]
    assert data["humidity"]
    assert type(data["temperature_c"]) == float
    assert type(data["temperature_f"]) == float
    assert type(data["humidity"]) == float


@patch("adafruit_dht.DHT22")
def test_exit(mock_device):
    temperature = Temperature()
    temperature.exit()
    mock_device.assert_called_once()
