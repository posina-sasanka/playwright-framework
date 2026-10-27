# Playwright Python Test Automation Framework

End-to-end test automation framework using Playwright and pytest, covering UI and API tests.

## Tech stack
Python, Playwright, pytest, pytest-xdist, pytest-html, GitHub Actions

## Features
- Page Object Model
- UI tests (SauceDemo): login, inventory sorting, cart, checkout
- API tests (Restful-Booker): create, read, update, delete bookings
- Fixtures for login and API authentication
- Parallel execution and cross-browser support
- HTML report, screenshots, video and traces on failure
- CI with GitHub Actions

## Project structure
pages/   tests/ui/   tests/api/   utils/   conftest.py   pytest.ini

## Setup
pip install -r requirements.txt
playwright install

## Run
pytest                      # all tests
pytest -m smoke             # smoke tests
pytest -n 3                 # parallel
pytest --browser firefox    # another browser
