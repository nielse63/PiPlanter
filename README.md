[![](https://codecov.io/gh/nielse63/piplanter/branch/master/graph/badge.svg)](https://codecov.io/gh/nielse63/piplanter)
[![](https://img.shields.io/pypi/l/piplanter.svg)](https://github.com/nielse63/piplanter)

# piplanter

Automate indoor plant care with a Raspberry Pi

## Install

Create a new project from this template by clicking the ["Use this template"](https://github.com/nielse63/piplanter/generate) button in GitHub

_or_

```bash
git clone https://github.com/nielse63/piplanter.git
cd piplanter
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

## Deploy

```bash
# ssh into pi
ssh pi@123.0.0.12
cd ~

# update dependenies
sudo apt-get update -y
sudo apt-get install libgpiod2 -y

# clone the repo
git clone https://github.com/nielse63/piplanter.git
cd piplanter

# setup and run the app
.bin/setup
```

## License

[MIT](LICENSE)
