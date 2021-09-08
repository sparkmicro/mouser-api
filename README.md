# Mouser Python API

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/sparkmicro/mouser-api/blob/main/LICENSE)
[![Python Versions](https://raw.githubusercontent.com/sparkmicro/Ki-nTree/master/images/python_versions.svg)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/mouser)](https://pypi.org/project/mouser/)
[![Style | Tests](https://github.com/sparkmicro/mouser-api/actions/workflows/tests.yaml/badge.svg)](https://github.com/sparkmicro/mouser-api/actions)

## Setup

### Requirements

* Tested with Python 3.7+
* Dependencies: [click](https://click.palletsprojects.com/en/8.0.x/) and [requests](https://docs.python-requests.org/en/master/) packages

### Mouser API Keys

Mouser provides two separate API keys:
* one for the cart and orders
* one for part searches.

Go to [Mouser's API hub](https://www.mouser.com/api-hub/) to request the keys.

To store the keys, two options:
* create two environmental variables `MOUSER_ORDER_API_KEY` and `MOUSER_PART_API_KEY` with the respective values of each key
* create a file named `mouser_api_keys.yaml` with the order API key on the first line and the part API key on a second line.

The keys will be automatically loaded for each API request.

### Install

#### Pip

``` bash
pip install mouser
```

#### Manually

1. Create virtual environment and activate it
2. Run `pip install -r requirements.txt`

#### Poetry

1. Install `poetry` package: `pip install poetry`
2. Run `poetry install`

### Run

#### Pip

```bash
mouser
```

#### Manually

```bash
python mouser_cli.py
```

#### Poetry

```bash
poetry run mouser
```

## Usage

This command line tool reflects the usage from Mouser's API structure [documented here](https://api.mouser.com/api/docs/ui/index#/).  
The first positional argument is the category of the request: cart (for MouserCart), order, history (for MouserOrderHistory) and search (for SearchAPI).
The second argument is the type of operation from the list of operations for each category.

Run `mouser --help` for more information about the usage.

### Examples
> The examples below assume this package was installed using Pip (for more options, see [above](#run))

#### Part Number Search
```bash
mouser search partnumber --number XXX
```

#### Export order to CSV
``` bash
mouser order get --number XXX --export
```
