# Test Automation Framework

This project implements a hybrid automation framework using:

- Selenium WebDriver (UI Automation)
- Requests (API Automation)
- Pytest (Test Runner)
- Allure (Reporting)
- Pytest-xdist (Parallel Execution)
- Pytest-rerunfailures (Flaky Test Handling)

The framework validates both UI workflows and API responses without hardcoded test data.

--- REPORT CONTAINS SS ALSO ADDING THE SS FOLDER IN GIT .GITIGNORE NOT USED SO SS AND ALL FOLDERS CAN BE SEE MANDE INTENTIONALLY
REPORT WITH PASS ----https://jazzy-paprenjak-006d5b.netlify.app/#suites/1d37fba13ac1d4ece6f943a21776221c/ad7402f53714162/
 
REPORT FAILED ------ https://wondrous-sundae-f14816.netlify.app/#behaviors/b1a8273437954620fa374b796ffaacdd/2429eb3050e1b313/
## 1. Technology Stack

- Python 3.x
- Selenium
- Pytest
- Requests
- Allure
- Pytest-xdist
- Pytest-rerunfailures

---

## 2. Project Structure

SuperProcure/
│
├── pages/ # Page Object Model classes
├── api/ # API client layer
├── tests/ # UI and API test cases
├── utils/ # Configuration reader and utilities
├── Drivers/ # WebDriver factory
├── config/
│ └── config.yaml # Environment configuration
├── conftest.py # Pytest fixtures and hooks
├── pytest.ini # Pytest configuration
└── README.md


---

## 3. Framework Design

### Page Object Model (POM)
Each page is implemented as a separate class to:
- Improve maintainability
- Promote reusability
- Reduce code duplication

### API Layer
A separate API client handles:
- Fetching product data
- Parsing JSON responses
- Returning structured data for validation

### Configuration Driven Execution
All environment-specific values such as:
- Browser type
- Headless mode
- Base URL

are maintained in `config.yaml`.

### Reporting
Allure is integrated for:
- Step-level visibility
- JSON attachment support
- Screenshot on failure

### Stability Measures
- Explicit waits implemented
- Rerun mechanism for flaky tests
- Screenshot capture on failure

---

## 4. Setup Instructions

### Step 1: Clone Repository


### Step 2: Create Virtual Environment


### Step 3: Install Dependencies


### Step 3: Install Dependencies

pip install -r requirements.txt



This will retry failed tests up to two additional times.

Example: pytest --reruns 2

The browser will run in background without opening UI.The browser will run in background without opening UI. pytest -v

## 8. Parallel Execution

Using pytest-xdist:  pytest -n 2 

yo increase workers :pytest -n 4

Allure Reporting

### Generate Allure Results  pytest --alluredir=reports



pytest -s -ra -n 1 --reruns 2 --alluredir=reports


This includes:
- Console logs
- Summary reporting
- Parallel execution
- Rerun mechanism
- Allure result generation

---

## 11. API + UI Validation Flow

1. Fetch product list using API.
2. Select a random product dynamically.
3. Open the same product in UI.
4. Validate:
   - Product Name
   - Price
   - Category
   - Availability (UI based)

No hardcoded test data is used.

---

## 12. Screenshot on Failure

If a test fails:
- Screenshot is saved in the screenshots folder.
- Screenshot is attached automatically in Allure report.

---

## 13. Known Limitations

- Website response time may cause delays.
- API does not provide availability field explicitly.
- UI locators depend on visible text structure.
- Occasional flakiness due to network latency.

---

## 14. Author

Manoj Kumar  
Automation Test Engineer
