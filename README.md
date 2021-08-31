# Exchanger Python Demo App

This repository contains a demo application meant to demonstrate CLI application development with Python based on type hints and OOP, including useful modules/libraries/syntax/etc.

## Exchanger app specification

The Exchanger app has a simple purpose: it's a CLI app for converting amounts of money from one currency to another. The inputs are provided in a file, and the ouputs are printed to the console.

**Input file format**

    <first line is "from" currency>
    <second line is "to" currency>
    <amount of money to convert (positive decimal > 0)>
    <amount of money to convert (positive decimal > 0)>
    <amount of money to convert (positive decimal > 0)>
    ...

An example input file converting from US Dollar to Euro is provided [here](exchanger_conversion_spec.txt), and the full list of currency codes can be found [here](https://iban.com/currency-codes).
For simplicity sake it's assumed inputs are valid and any issues, e.g. money isn't positive decimal, will raise and propagate exceptions as-is.

## Running the Exchanger app

1. Clone this repo
2. Setup a Python virtual environment with all the Python dependencies based on [requirements.txt](requirements.txt). Real Python has a [useful article for virtual environments](https://realpython.com/python-virtual-environments-a-primer/).
3. Run **src/main.py** and provide the file path to the input file. To use the example input file provided with repo run in your terminal (cmd/bash/etc.) from repo root: 
    
    `python src/main.py exchanger_conversion_spec.txt`

## Implementation references

Exchange rate from one currency to another is discovered by using the free API https://exchangerate.host/#/docs.

The Python implementation was written for Python 3.9.6, tested with CPython, and relies on the following:

**Important built-in modules**

* *typing* module - for type hints support, specialized strongly typed classes and using advanced typing features
* *abc* module - implementing Abstract Classes
* *asyncio* module - support for async IO, futures, coroutines and tasks
* *pathlib* module - utilities for file system paths, particularly useful `Path` type

**Important Python libraries**

* [*typer*](https://typer.tiangolo.com/) - create CLI applications with type hints support
* [*lagom*](https://lagom-di.readthedocs.io/en/latest/) - a DI container that enables DI design principle with auto-wiring of dependencies based on type hints
* [*pydantic*](https://pydantic-docs.helpmanual.io/) - represent system entities as typed data models using type hints with many features that improve upon the built-in *dataclasses* module. Can also read application settings into data models from environment variables, secret files, and any other custom settings source, e.g. JSON files.
* [*orjson*](https://github.com/ijl/orjson) - fast library for working with JSON - serialization & deserialization
* [*aiohttp*](https://docs.aiohttp.org/en/stable/) - used as HTTP client to send HTTP requests using async IO
* [*aiofiles*](https://pythonrepo.com/repo/Tinche-aiofiles-python-files) - file system access using async IO
* [*asyncstdlib*](https://asyncstdlib.readthedocs.io/en/latest/) - async versions of built-in functions; this repo uses its `tuple` function to transorm the input file lines provided by *aiofiles* into a tuple.

## Code Quality and Linting

The following code quality and linting solutions are used:

* [*MyPy*](https://mypy.readthedocs.io/en/stable/introduction.html) - type hints checker. *pydantic* integrates with it to type check data models.
* [*black*](https://github.com/psf/black) - code formatter.
* [*isort*](https://github.com/PyCQA/isort) - sorting import statements.
* [*flake8*](https://flake8.pycqa.org/en/latest/) - Style guide enforcement. Here are some useful plugins:
  * [*flake8-builtins*](https://github.com/gforcada/flake8-builtins) - checks for accidental use of builtin functions as names
  * [*flake8-comprehensions*](https://github.com/adamchainz/flake8-comprehensions) - checks for misuse or lack of use of comprehensions
  * [*flake8-mutable*](https://github.com/ebeweber/flake8-mutable) - checks for mutable default parameter values Python issue
  * [*pep8-naming*](https://github.com/PyCQA/pep8-naming) - checks that names follow Python standards defined in PEP8
  * [*flake8-simplify*](https://github.com/MartinThoma/flake8-simplify) - checks for general Python best practices for simpler code
  * [*flake8-pytest-style*](https://github.com/m-burst/flake8-pytest-style) - check that *pytest* unit tests are written according to style; **this plugin isn't relevant for this repo**
  * [*flake8-logging-format*](https://github.com/globality-corp/flake8-logging-format) - ensures logs use extra arguments and exception(); **this plugin isn't relevant for this repo**

Note *MyPy* and *flake8* are configured with [setup.cfg](setup.cfg).

## Contributions

This repo doesn't accept contributions since it's acting as a demo.

