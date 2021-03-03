import datetime
import json
import pathlib

import requests

from pyplanter.constants import API_URL, DEFAULT_LIGHT_DATA_PATH, TODAY
from pyplanter.helpers import parse_datetime
from pyplanter.logger import logger


class Light:
    def __init__(self, filepath: pathlib.Path = DEFAULT_LIGHT_DATA_PATH):
        self.today = TODAY
        self.now = parse_datetime(datetime.datetime.now().isoformat())
        self.filepath = filepath
        self.setup()
        self.light_data = self.read()

    def setup(self) -> None:
        logger.debug("setting up light data")
        parent = self.filepath.parent
        parent.mkdir(parents=True, exist_ok=True)
        if not self.filepath.exists():
            fh = open(self.filepath, "w")
            fh.write("[]")
            fh.close()

    def fetch_data(self) -> dict:
        logger.debug("fetching light data")
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        sunrise = parse_datetime(data["results"]["sunrise"]).isoformat()
        sunset = parse_datetime(data["results"]["sunset"]).isoformat()
        object = {"date": self.today, "sunrise": sunrise, "sunset": sunset}
        self.append_data(object)
        return object

    def append_data(self, new_data: dict) -> list:
        for object in self.light_data:
            object_date = object["date"]
            date = new_data["date"]
            if object_date == date:
                return self.light_data
        self.light_data.append(new_data)
        return self.light_data

    def read(self) -> list:
        logger.debug(f"reading from file {self.filepath}")
        with open(self.filepath) as f:
            json_content = f.read()
            if not json_content:
                json_content = "[]"
        self.light_data = json.loads(json_content)
        return self.light_data

    def save(self) -> bool:
        logger.debug(f"saving to {self.filepath}")
        if not self.filepath.exists():
            return False
        with open(self.filepath, "w") as f:
            json.dump(self.light_data, f)
        return True

    def get_latest_data(self) -> dict:
        logger.debug("getting latest light data")
        data = self.light_data
        if len(data) and data[-1]["date"] == self.today:
            return data[-1]
        return self.fetch_data()

    def get_is_light_on(self) -> bool:
        data_object = self.get_latest_data()
        sunrise = parse_datetime(data_object["sunrise"])
        sunset = parse_datetime(data_object["sunset"])
        is_light_one = self.now > sunrise and self.now < sunset
        return is_light_one
