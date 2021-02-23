import pytz
from datetime import datetime

import pytz

def celcius_to_fahrenheit(temp_c: float) -> float:
    return temp_c * (9 / 5) + 32


def parse_datetime(
    datetime_string: str,
    timezone: str = "America/Chicago",
) -> datetime:
    datetime_obj = datetime.fromisoformat(datetime_string)
    datetime_obj = datetime_obj.astimezone(pytz.timezone(timezone))
    return datetime_obj
