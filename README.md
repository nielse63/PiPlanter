[![](https://codecov.io/gh/nielse63/pyplanter/branch/master/graph/badge.svg)](https://codecov.io/gh/nielse63/pyplanter)
[![](https://img.shields.io/pypi/l/pyplanter.svg)](https://github.com/nielse63/pyplanter)

# pyplanter

Automate indoor plant care with a Raspberry Pi

## Install

Create a new project from this template by clicking the ["Use this template"](https://github.com/nielse63/pyplanter/generate) button in GitHub

_or_

```bash
git clone https://github.com/nielse63/pyplanter.git
cd pyplanter
.bin/setup
```

## Usage

```bash
make setup      # install venv and depdencies
make install    # install pip depdencies
make lint       # run mypy, flake8, and black
make test       # pytest
make report     # generate codecov repo
make build      # compile source
make publish    # publish build artifact
make docs       # regenerate docs
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
python pyplanter/runner.py
```

## License

[MIT](LICENSE)
