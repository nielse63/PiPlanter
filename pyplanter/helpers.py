import os

from datetime import datetime
from pyplanter.constants import TIMEZONE, IFTTT_KEY


def celcius_to_fahrenheit(temp_c: float) -> float:
    return temp_c * (9 / 5) + 32


def parse_datetime(datetime_string: str) -> datetime:
    datetime_obj = datetime.fromisoformat(datetime_string)
    datetime_obj = datetime_obj.astimezone(TIMEZONE)
    return datetime_obj


def ifttt_endpoint(action: str):
    key = os.getenv(IFTTT_KEY)
    return "https://maker.ifttt.com/trigger/{}/with/key/{}".format(action, key)
