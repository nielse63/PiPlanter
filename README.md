[![License](https://img.shields.io/pypi/l/PiPlanter.svg)](https://github.com/nielse63/PiPlanter)
[![codecov](https://codecov.io/gh/nielse63/PiPlanter/branch/master/graph/badge.svg?token=PXwocWyA3R)](https://codecov.io/gh/nielse63/PiPlanter)
[![Python app](https://github.com/nielse63/PiPlanter/actions/workflows/python.yml/badge.svg)](https://github.com/nielse63/PiPlanter/actions/workflows/python.yml)

# PiPlanter

Automate indoor plant care with a Raspberry Pi

## Install

```bash
git clone https://github.com/nielse63/PiPlanter.git
cd pyplanter
.bin/setup
```

## Usage

### Install Module

```bash
source activate
python setup.py develop
```

### Format Source

```bash
.bin/validate
```

_or_

```bash
isort .
black .
flake8 pyplanter
mypy pyplanter
```

### Run Tests

```bash
py.test
```

## Deploy to Raspberry Pi

```bash
# ssh into pi
ssh pi@<id_address>
cd ~

# update dependenies
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install build-essential python-dev python-smbus git libgpiod2

# clone the repo
git clone https://github.com/nielse63/PiPlanter.git
cd PiPlanter

# initialize the virtualenv and install dependencies
.bin/setup-prod

# run the app
source activate
python run.py
```

## License

[MIT](LICENSE)
