import pytz

from datetime import datetime
from pyplanter.constants import LOCAL_TIMEZONE


def celcius_to_fahrenheit(temp_c: float) -> float:
    return temp_c * (9 / 5) + 32


def parse_datetime(
    datetime_string: str,
    timezone: str = LOCAL_TIMEZONE,
) -> datetime:
    datetime_obj = datetime.fromisoformat(datetime_string)
    datetime_obj = datetime_obj.astimezone(pytz.timezone(timezone))
    return datetime_obj
