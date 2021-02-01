from gpiozero import LED
from time import sleep

# source: https://gpiozero.readthedocs.io/en/stable/recipes.html

red = LED("BOARD12")  # gpio17, physical board pin #12

while True:
    print("on")
    red.on()
    sleep(1)
    print("off")
    red.off()
    sleep(1)
