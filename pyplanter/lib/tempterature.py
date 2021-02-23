import adafruit_dht
import adafruit_blinka.board.raspberrypi.raspi_40pin as board

from pyplanter.helpers import celcius_to_fahrenheit


class Temperature:
    def __init__(self) -> None:
        self.device = adafruit_dht.DHT22(board.D4, use_pulseio=False)

    def get_data(self) -> dict:
        temperature_c = self.device.temperature
        temperature_f = celcius_to_fahrenheit(temperature_c)
        humidity = self.device.humidity
        return {
            "temperature_c": temperature_c,
            "temperature_f": temperature_f,
            "humidity": humidity,
        }

    def exit(self) -> None:
        self.device.exit()
