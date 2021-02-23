#!/usr/bin/python
import time
from pyplanter.lib.tempterature import Temperature

temp = Temperature()

while True:
    try:
        # Print the values to the serial port
        data = temp.get_data()
        temperature_c = data["temperature_c"]
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = data["humidity"]
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(f"ERROR: {error.args[0]}")
        # time.sleep(2.0)
        # continue
    except Exception as error:
        temp.exit()
        raise error

    time.sleep(2.0)
