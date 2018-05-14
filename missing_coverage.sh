#!/bin/bash
# Run all tests, report coverage and missing lines
pytest --cov=. --cov-report term-missing:skip-covered

