# # read from moisture sensor

# # Source https://tutorials-raspberrypi.com/measuring-soil-moisture-with-raspberry-pi/
# import time
# from typing import Any

# import spidev

# delay = 0.2

# spi = spidev.SpiDev()
# spi.open(0, 0)
# spi.max_speed_hz = 1000000


# def readChannel(channel: int) -> Any:
#     val = spi.xfer2([1, (8 + channel) << 4, 0])
#     data = ((val[1] & 3) << 8) + val[2]
#     return data


# if __name__ == "__main__":
#     try:
#         while True:
#             val = readChannel(0)
#             if val != 0:
#                 print(val)
#             time.sleep(delay)

#     except KeyboardInterrupt:
#         print("Cancel.")
