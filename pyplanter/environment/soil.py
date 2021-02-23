# import RPi.GPIO as GPIO
# import time

# #GPIO SETUP
# channel = 21
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(channel, GPIO.IN)

# def callback(channel):
#         if GPIO.input(channel):
#                 print "no  water detected"
#         else:
#                 print "Water Detected!"

# GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
# GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

import time

# # infinite loop
# while True:
#         time.sleep(1)
# source: https://www.instructables.com/Soil-Moisture-Sensor-Raspberry-Pi/
# source: https://learn.sparkfun.com/tutorials/soil-moisture-sensor-hookup-guide
# !!source: https://pypi.org/project/mcp3008/
import RPi.GPIO as GPIO


class Soil:
    def __init__(self) -> None:
        self.channel = 21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.channel, GPIO.IN)
        pass

    def get_moisture(self) -> None:
        pass
