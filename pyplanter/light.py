# get sunrise and sunset times in guatamala
# turn light on and off at those times
from datetime import datetime
from typing import Callable, Optional

import pytz
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from loguru import logger

LATITUDE = 14.628434
LONGITUDE = -90.522713
API_URL = f"https://api.sunrise-sunset.org/json?lat={LATITUDE}&lng={LONGITUDE}&date=today&formatted=0"


class Light:
    @staticmethod
    def parse_datetime(datetime_string: str) -> datetime:
        datetime_obj = datetime.fromisoformat(datetime_string)
        local_datetime = datetime_obj.astimezone(
            pytz.timezone("America/Guatemala")
        )
        return local_datetime

    def __init__(self) -> None:
        self.sunrise: Optional[datetime] = None
        self.sunset: Optional[datetime] = None
        logger.info("Init Light class")
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        logger.info("Light jobs started")

    def on(self) -> None:
        print("lights on")

    def off(self) -> None:
        print("lights off")

    def get_data(self) -> None:
        logger.info("Getting sunrise/sunset data")
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        self.sunrise = Light.parse_datetime(data["results"]["sunrise"])
        self.sunset = Light.parse_datetime(data["results"]["sunset"])

    def schedule_job(
        self, name: str, prop: Optional[datetime], callable: Callable
    ) -> None:
        if not prop:
            # raise ValueError("prop is not defined")
            logger.error(f"prop is not defined for {name}")
            return
        self.scheduler.add_job(
            callable,
            trigger="date",
            next_run_time=prop,
            id=name,
            replace_existing=True,
        )

    def schedule_jobs(self) -> None:
        if not self.sunrise or self.sunset:
            self.get_data()
        self.schedule_job(name="sunrise", prop=self.sunrise, callable=self.on)
        self.schedule_job(name="sunset", prop=self.sunrise, callable=self.off)
        logger.info("Light jobs scheduled")
