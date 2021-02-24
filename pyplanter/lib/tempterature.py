import adafruit_dht
import adafruit_blinka.board.raspberrypi.raspi_40pin as board
import pytz

from datetime import datetime
from pyplanter.lib.collection import Collection
from pyplanter.constants import LOCAL_TIMEZONE
from pyplanter.helpers import celcius_to_fahrenheit
from pyplanter.logger import logger

collection = Collection("temperature")


class Temperature:
    def __init__(self) -> None:
        self.device = adafruit_dht.DHT22(board.D4, use_pulseio=False)
        self.data = {}

    def get_data(self) -> dict:
        temperature_c = self.device.temperature
        temperature = celcius_to_fahrenheit(temperature_c)
        timestamp = datetime.now(pytz.timezone(LOCAL_TIMEZONE))
        self.data = {
            "temperature": temperature,
            "humidity": self.device.humidity,
            "timestamp": timestamp,
        }
        return self.data

    def exit(self) -> None:
        self.device.exit()

    def save(self) -> None:
        logger.debug("saving temperature data")
        collection.create(self.data)
