#!/usr/bin/env bash

# uvr mypy --strict example.py
# exit

# uvr pytest

# --cov-report xml - generate an XML report for CI/CD tools
# --cov-report html:coverage - generate an HTML report in directory 'coverage'
# --cov-report term - generate a terminal report
uvr pytest --cov=boxext --cov-report html:coverage --cov-report xml --cov-report term


