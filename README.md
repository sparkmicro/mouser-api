# Mouser Python API

## Setup
### Mouser API Keys

Mouser provides two separate API keys:
* one for the cart and orders
* one for part searches.

Go to [Mouser's API hub](https://www.mouser.com/api-hub/) to request the keys.

To store the keys, two options:
* create two environmental variables `MOUSER_ORDER_API_KEY` and `MOUSER_PART_API_KEY` with the respective values of each key
* create a file named `mouser_api.keys` with the order API key on the first line and the part API key on a second line.

The keys will be automatically loaded for each API request.

### Install

#### Manually

1. Create virtual environment and activate it
2. Run `pip install -r requirements.txt`

#### Poetry

1. Install `poetry` package: `pip install poetry`
2. Run `poetry install`

#### Pip

> WARNING: This procedure installs from TestPyPI (PyPI is pending)

``` bash
pip install --index-url https://test.pypi.org/simple/ mouser
```

### Run

#### Manually

```bash
python mouser_cli.py
```

#### Poetry

```bash
poetry run mouser
```

#### Pip

```bash
mouser
```

## Usage

> The examples below assume this package was installed using Pip (for more options, see [above](#run))

### Part Number Search
```bash
mouser search partnumber --number XXX
```

### Export order to CSV
``` bash
mouser order get --number XXX --export
```
