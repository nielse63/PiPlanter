import requests_mock
import pathlib
import tempfile

from pyplanter.lib.light import Light
from pyplanter.constants import TODAY, API_URL
from pyplanter.helpers import parse_datetime


def before_each():
    tmp_dir = tempfile.mkdtemp()
    tmp_file = pathlib.Path(tmp_dir) / "light_data.json"
    if tmp_file.exists():
        tmp_file.unlink()
    light = Light(filepath=tmp_file)
    return light


def test_init():
    light = before_each()
    assert light
    assert light.today == TODAY
    assert light.filepath
    assert type(light.light_data) is list


def test_setup():
    light = before_each()
    if light.filepath.exists():
        light.filepath.unlink()
        light.filepath.parent.rmdir()
    light.setup()
    assert light.filepath.parent.exists()
    assert light.filepath.exists()


def test_append_data():
    light = before_each()
    object = {"date": TODAY, "sunrise": "", "sunset": ""}
    # validate that the new object was appended to the list
    light.light_data = []
    assert len(light.light_data) == 0
    light.append_data(object)
    assert len(light.light_data) == 1

    # validate that objects with the same date are not appended
    light.light_data = [object]
    assert len(light.light_data) == 1
    light.append_data(object)
    assert len(light.light_data) == 1


def test_read():
    light = before_each()
    # create an empty file to test empty data handling
    if light.filepath.exists():
        light.filepath.unlink()
        light.filepath.touch()
    results = light.read()
    assert type(results) is list
    assert not len(results)


def test_save():
    light = before_each()
    assert light.filepath.exists()
    results = light.save()
    assert results
    assert light.filepath.exists()

    # handles no file found
    light.filepath.unlink()
    results = light.save()
    assert results is False


def test_get_latest_data():
    light = before_each()
    with requests_mock.Mocker() as m:
        mock_response = """{"results":{"sunrise":"2021-02-22T12:22:06+00:00","sunset":"2021-02-23T00:08:44+00:00","solar_noon":"2021-02-22T18:15:25+00:00","day_length":42398,"civil_twilight_begin":"2021-02-22T12:00:32+00:00","civil_twilight_end":"2021-02-23T00:30:17+00:00","nautical_twilight_begin":"2021-02-22T11:35:30+00:00","nautical_twilight_end":"2021-02-23T00:55:19+00:00","astronomical_twilight_begin":"2021-02-22T11:10:33+00:00","astronomical_twilight_end":"2021-02-23T01:20:17+00:00"},"status":"OK"}"""
        m.get(API_URL, text=mock_response)
        object = {"date": TODAY, "sunrise": "", "sunset": ""}
        # get the last element of the list when populated
        light.light_data = [object]
        assert len(light.light_data) == 1
        data = light.get_latest_data()
        assert data["date"] is object["date"]
        assert data["sunrise"] is object["sunrise"]
        assert data["sunset"] is object["sunset"]

        # when unpopulated, fetch new data
        light.light_data = []
        assert len(light.light_data) == 0
        data = light.get_latest_data()
        assert data["date"] is object["date"]
        assert data["sunrise"]
        assert data["sunset"]


def test_get_is_light_on():
    light = before_each()
    object = {
        "date": TODAY,
        "sunrise": f"{TODAY}T06:00:00-06:00",
        "sunset": f"{TODAY}T18:00:00-06:00",
    }
    light.light_data = [object]

    # set "now" to a time we know is valid
    light.now = parse_datetime(f"{TODAY}T07:00:00-06:00")
    is_light_on = light.get_is_light_on()
    assert is_light_on is True

    # set "now" a time before sunrise
    light.now = parse_datetime(f"{TODAY}T03:00:00-06:00")
    is_light_on = light.get_is_light_on()
    assert is_light_on is False

    # set "now" a time after sunset
    light.now = parse_datetime(f"{TODAY}T20:00:00-06:00")
    is_light_on = light.get_is_light_on()
    assert is_light_on is False
