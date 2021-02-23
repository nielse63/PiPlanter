import requests
import os
import pathlib
import datetime
import json

from pyplanter.helpers import parse_datetime

LATITUDE = 14.628434
LONGITUDE = -90.522713
TODAY = datetime.date.today().strftime("%Y-%m-%d")
API_URL = f"https://api.sunrise-sunset.org/json?lat={LATITUDE}&lng={LONGITUDE}&date={TODAY}&formatted=0"
JSON_PATH = pathlib.Path(__file__).parent.parent.parent / "data/light.json"


def get_from_api() -> dict:
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()
    sunrise = parse_datetime(data["results"]["sunrise"]).isoformat()
    sunset = parse_datetime(data["results"]["sunset"]).isoformat()
    return {"date": TODAY, "sunrise": sunrise, "sunset": sunset}


def write_to_file(object):
    with open(JSON_PATH, "r") as f:
        json_content = f.read()
        if not json_content:
            json_content = "[]"
        data = json.loads(json_content)
        data.append(object)
        data_string = json.dumps(data, indent=2)
        f.close()
    fh = open(JSON_PATH, "w")
    fh.write(data_string)
    fh.close()
    return data


def from_file() -> list:
    if not os.path.exists(JSON_PATH.parent):
        os.mkdir(JSON_PATH.parent)
    if not os.path.exists(JSON_PATH):
        with open(JSON_PATH, "w"):
            pass
        return []
    with open(JSON_PATH) as f:
        json_content = f.read()
    data = json.loads(json_content)
    return data


def get_todays_data():
    data_array = from_file()
    if len(data_array) and data_array[-1]["date"] == TODAY:
        return data_array[-1]
    data_object = get_from_api()
    write_to_file(data_object)
    return data_object


def get_is_light_on(data_object: dict):
    now = parse_datetime(datetime.datetime.now().isoformat())
    sunrise = parse_datetime(data_object["sunrise"])
    sunset = parse_datetime(data_object["sunset"])
    is_light_one = now > sunrise and now < sunset
    return is_light_one
