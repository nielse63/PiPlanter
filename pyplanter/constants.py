# from datetime import date
import pathlib

import pytz
from dotenv import load_dotenv

# load .env file
ENV_FILE_PATH = pathlib.Path(__file__).parent.parent / ".env"
load_dotenv(ENV_FILE_PATH)

# timezone
TIMEZONE_NAME = "America/Chicago"
TIMEZONE = pytz.timezone(TIMEZONE_NAME)

# environment keys
IFTTT_KEY = "IFTTT_KEY"
IFTTT_HEAT_ACTION = "toggle_heat"
IFTTT_HUMIDIFIER_ACTION = "toggle_humidifier"


# enum for the gpio pins
class GPIOPins:
    # temp/humidity
    DHT22 = 4

    # soil moisture
    soil_moisture_channel = 0
    soil_moisture_clock_pin = 11
    soil_moisture_mosi_pin = 10
    soil_moisture_miso_pin = 9
    soil_moisture_select_pin = 8

    # water pump
    water_pump = 26
