# 🧪 Playwright UI Automation Framework – OrangeHRM

![Python](https://img.shields.io/badge/python-3.10+-blue)
![Playwright](https://img.shields.io/badge/playwright-automation-green)
![Pytest](https://img.shields.io/badge/pytest-tested-orange)
![Status](https://img.shields.io/badge/status-active-success)
![CI](https://github.com/tarnayattila/playwright-orangehrm-framework/actions/workflows/playwright.yml/badge.svg)

Automated UI test framework built with **Playwright + Python + Pytest** for testing the OrangeHRM demo application.

This project demonstrates a scalable Page Object Model (POM) structure, test automation best practices, and CI-ready design.

---

## 📌 Tech Stack

- Python 3.10+
- Playwright
- Pytest
- Faker (test data generation)
- Page Object Model (POM)

---

## 📂 Project Structure


```bash
 playwright-orangehrm-framework/
│
├── pages/ # Page Object Models
│ ├── login_page.py
│ ├── dashboard_page.py
│ ├── pim_page.py
│ └── side_menu.py
│
├── tests/ # Test cases
│ ├── test_login.py
│ ├── test_logout.py
│ ├── test_dashboard.py
│ ├── test_add_employee.py
│ └── test_invalid_login.py
│
├── utils/
│ └── faker_utils.py
│
├── conftest.py
├── pytest.ini
└── README.md


---

## 🚀 Features Covered

- Login / Logout functionality
- Dashboard validation
- Add Employee (PIM module)
- Invalid login handling
- Navigation tests
- Dynamic test data generation (Faker)

---

## ▶️ How to Run Tests

### Install dependencies
```bash
pip install -r requirements.txt
Install Playwright browsers
playwright install
Run all tests
pytest -v
Run in headed mode
pytest --headed
🧪 Example Test
def test_add_employee(page):

    login = LoginPage(page)
    pim = PIMPage(page)

    login.open()
    login.login("Admin", "admin123")

    user = generate_employee()

    pim.add_employee(user["first_name"], user["last_name"])

    assert page.locator(".oxd-toast").is_visible()
🏗 Architecture

This framework follows the Page Object Model (POM) pattern:

Pages contain locators and actions
Tests contain assertions and test logic
Reusable and maintainable structure
🔧 Design Principles
Separation of concerns (tests vs pages)
No hardcoded test data
Stable selectors preferred (role-based locators)
Minimal flaky waits, rely on Playwright auto-wait
📊 Future Improvements
GitHub Actions CI pipeline
Allure reporting
Parallel execution (pytest-xdist)
API + UI hybrid tests
Session-based login fixtures
📸 Demo App

https://opensource-demo.orangehrmlive.com/

👨‍💻 Author

Automation Testing Portfolio Project
Built with Python + Playwright