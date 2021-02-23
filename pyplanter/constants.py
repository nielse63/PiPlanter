import pathlib
from datetime import date

LATITUDE = 14.628434

LONGITUDE = -90.522713

TODAY = date.today().strftime("%Y-%m-%d")

API_URL = f"https://api.sunrise-sunset.org/json?lat={LATITUDE}&lng={LONGITUDE}&date={TODAY}&formatted=0"

DEFAULT_LIGHT_DATA_PATH = (
    pathlib.Path(__file__).parent.parent.parent / "data/light.json"
)
