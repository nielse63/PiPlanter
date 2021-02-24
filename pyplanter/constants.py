from datetime import date

LOCAL_TIMEZONE = "America/Chicago"
# LATITUDE = 14.628434
# LONGITUDE = -90.522713
TODAY = date.today().strftime("%Y-%m-%d")
# API_URL = f"https://api.sunrise-sunset.org/json?lat={LATITUDE}&lng={LONGITUDE}&date={TODAY}&formatted=0"
# DEFAULT_LIGHT_DATA_PATH = pathlib.Path("~/.pyplanter/data/light.json").expanduser()

# api
DB_API_URL = "https://us-central1-plants-13d3e.cloudfunctions.net/"

# temperature vars
TEMPERATURE_TIMEOUT = 60 * 5
TEMP_API_URL = "https://us-central1-plants-13d3e.cloudfunctions.net/temperature"
