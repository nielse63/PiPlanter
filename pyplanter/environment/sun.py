from datetime import datetime
from typing import Optional

import pytz
import requests

from pyplanter.helpers import parse_datetime
from pyplanter.logger import logger

LATITUDE = 14.628434
LONGITUDE = -90.522713
API_URL = f"https://api.sunrise-sunset.org/json?lat={LATITUDE}&lng={LONGITUDE}&date=today&formatted=0"


class Sun:
    def __init__(self) -> None:
        self.sunrise: Optional[datetime] = None
        self.sunset: Optional[datetime] = None

    def get_sunrise(self) -> None:
        logger.debug("Getting sunrise/sunset data")
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        self.sunrise = parse_datetime(data["results"]["sunrise"])
        self.sunset = parse_datetime(data["results"]["sunset"])
        logger.debug(f"sunrise: {self.sunrise}; sunset: {self.sunset}")

    def is_daytime(self) -> bool:
        if not self.sunrise:
            self.get_sunrise()
        now = datetime.now()
        local_datetime = now.astimezone(pytz.timezone("America/Chicago"))
        is_daytime = (
            local_datetime > self.sunrise and local_datetime < self.sunset
        )
        # logger.debug(f"is daytime: {is_daytime}")
        return is_daytime
