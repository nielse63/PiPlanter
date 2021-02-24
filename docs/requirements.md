# Rwequired steps before runnin app on Pi

## Upgrade system

```bash
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install build-essential python-dev python-smbus git libgpiod2
```

<!-- ## Install pigpiod daemon

```bash
sudo apt-get install pigpio python-pigpio python3-pigpio -y
sudo systemctl enable pigpiod

# verify status
sudo service pigpiod status
``` -->

<!--
## Install Adafruit Python

```bash
cd ~
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo apt-get update
sudo python setup.py install
sudo reboot
```
-->
