# Optibet Automation Framework (Python/Pytest)

## Project Overview
This project implements automated UI tests for Optibet.ee as part of a technical assignment. It focuses on critical user flows and ensures cross-platform reliability through containerization.

## Tech Stack
- Language: Python 3.12
- Framework: Pytest + SeleniumBase (UC Mode)
- Reporting: Allure
- Environment: Docker
- CI/CD: GitHub Actions

## How to Run Tests Locally
- Install dependencies: `pip install -r requirements.txt`
- Execute tests: `pytest tests/ --uc --headless --alluredir=allure-results`
- View Report: `allure serve allure-results`

## Docker Execution
This is the recommended method to ensure a clean, consistent environment.
- Build image: `docker build -t optibet-automation .`
- Run container: `docker run --rm --shm-size="2gb" optibet-automation`

## Scenarios Covered
- Header/Language: Verified logo presence and functionality of the language switcher.
- Promotions: Content validation and testing of category filtering logic.
- Registration: Extensive negative validation using Pytest parametrization for edge cases.
- Login: Verified robust error handling for invalid or empty credentials.
- Help/Support: Navigation to the Help Center and verification of contact channels.

## Test Rationale
- Scenarios were selected based on high-impact user entry points: account creation, authentication, and core product discovery (Promotions).
- Undetected Chromedriver (UC Mode) was utilized to mimic real user behavior and prevent false negatives from bot-detection services.
- Search functionality was omitted from this suite as the search trigger is currently absent on the .ee production environment.
- CI/CD Note: GitHub Actions may show failures due to data center IP geoblocking by the target site; however, the suite is fully verified in the local Docker environment.
