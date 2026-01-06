# Optibet Automation Framework (Python/Pytest)

## Project Overview
This project implements automated UI tests for Optibet.ee as part of a technical assignment.

## Tech Stack
-Language: Python 3.12 
-Framework: Pytest + SeleniumBase (UC Mode) [cite: 5, 6]
-Reporting: Allure 
-Environment: Docker 

## How to Run Tests Locally
-Install dependencies: `pip install -r requirements.txt` 
-Execute tests: `pytest tests/ --uc --headless --alluredir=allure-results` 
-View Report: `allure serve allure-results` 

## Docker Execution
-Build: `docker build -t optibet-automation .` 
-Run: `docker run optibet-automation` 

## Scenarios Covered
-Header/Language*: Verified logo presence and language switching.
-Promotions: Content validation and category filtering.
-Registration: Negative validation with Pytest parametrization.
-Login: Verified error handling for invalid credentials.
-Bonus: Help Center navigation and contact verification.

## Test Rationale
-Scenarios were selected based on the most critical user entry points: account creation, logging in, and exploring offers. 
-Note: Search functionality was omitted as the trigger is absent on the `.ee` production environment.
