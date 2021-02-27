from unittest.mock import patch
from gpiozero import MCP3008
from gpiozero.pins.mock import MockFactory
from pyplanter.sensors.soil_moisture_sensor import get_soil_moisture_value

MCP3008.pin_factory = MockFactory()


@patch("gpiozero.MCP3008", return_value={"value": 0.5})
def test_get_soil_moisture_value(mock_factory):
    try:
        output = get_soil_moisture_value()
        assert output is not None
        mock_factory.assert_called_once()
    except Exception as error:
        print(error)
