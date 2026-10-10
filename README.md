# QA Testing & Automation Portfolio

A practical Software Quality Assurance (QA) portfolio demonstrating manual testing, test case design, bug reporting, exploratory testing, and browser automation using Python and Selenium WebDriver.

This repository contains manual testing documentation for a fictional e-commerce application called **DemoShop** and automated UI tests for the publicly available **SauceDemo** practice website. These are separate practice projects and are documented independently.

## About This Portfolio

This portfolio demonstrates my understanding of software testing principles and practical QA workflows, including:

- Manual Functional Testing
- Positive and Negative Testing
- Test Case Design and Execution
- Requirements-Based Testing
- Bug Reporting and Defect Documentation
- Severity and Priority Assessment
- Exploratory Testing
- Regression Testing Concepts
- Test Planning and Test Summary Reporting
- Python Test Automation
- Selenium WebDriver
- Explicit Waits and Element Locators
- Assertions and PASS/FAIL Reporting
- Git and GitHub

## Technologies and Tools

| Technology | Purpose |
|---|---|
| Python | Writing automation scripts |
| Selenium WebDriver | Browser automation |
| Google Chrome | Running automated UI tests |
| VS Code | Writing and managing test code |
| Git | Version control |
| GitHub | Source code hosting and portfolio presentation |
| Markdown | QA documentation |

## Repository Structure

```text
qa-testing-portfolio/
├── requirements/
│   └── demo-shop-requirements.md
├── test-plan/
│   └── test-plan.md
├── test-cases/
│   └── manual-test-cases.md
├── bug-reports/
│   ├── BUG-001-invalid-login-email-accepted.md
│   ├── BUG-002-cart-total-not-updated.md
│   └── BUG-003-duplicate-order-on-double-click.md
├── exploratory-testing/
│   └── session-notes.md
├── test-summary/
│   └── test-summary-report.md
├── test_login.py
├── test_invalid_login.py
├── test_saucedemo.py
├── .gitignore
└── README.md
```

## Project 1: Manual Testing — DemoShop

**Application:** Fictional e-commerce application

The DemoShop project focuses on structured manual testing and QA documentation. Its requirements, test cases, defect reports, and test summary are practice materials created for portfolio purposes.

### Testing activities

- Reviewed application requirements.
- Designed positive and negative test cases.
- Covered authentication, product catalogue, cart, and checkout scenarios.
- Documented expected and actual results.
- Prepared sample bug reports with severity and priority.
- Recorded exploratory testing observations.
- Prepared a test summary and regression recommendations.

### Documentation

- [Requirements](requirements/demo-shop-requirements.md)
- [Test Plan](test-plan/test-plan.md)
- [Manual Test Cases](test-cases/manual-test-cases.md)
- [Bug Reports](bug-reports/)
- [Exploratory Testing Notes](exploratory-testing/session-notes.md)
- [Test Summary Report](test-summary/test-summary-report.md)

**Important:** DemoShop is fictional. Its documented defects and test results are synthetic practice examples, not verified defects in a live production application.

## Project 2: Selenium Automation — SauceDemo

**Practice website:** https://www.saucedemo.com/

This project uses Python and Selenium WebDriver to automate selected browser-based test scenarios on SauceDemo.

### Automated test scenarios

1. **Valid Login:** Verify that valid credentials open the products page.
2. **Invalid Login:** Verify that an incorrect password displays an error message.
3. **Add to Cart:** Verify that adding a product updates the shopping cart badge.
4. **Checkout:** Add a product to the cart, enter checkout information, and verify that the checkout overview page opens.

The automation scripts use Selenium element locators, explicit waits, assertions, and browser cleanup.

### Automation files

- `test_login.py` — Standalone valid-login test.
- `test_invalid_login.py` — Standalone invalid-login test.
- `test_saucedemo.py` — Combined automation suite.

### Prerequisites

- Python 3
- Google Chrome
- Visual Studio Code or another code editor
- Git

### Setup Instructions on Ubuntu/Linux

**1. Open the project directory**

```bash
cd ~/Downloads/qa-testing-portfolio-main
```

**2. Create a virtual environment**

```bash
python3 -m venv .venv
```

**3. Activate the virtual environment**

```bash
source .venv/bin/activate
```

**4. Install Selenium**

```bash
python -m pip install selenium
```

Selenium Manager can help manage the browser driver automatically. A compatible browser installation and network access may be required.

### Run the automation suite

With the virtual environment activated, run:

```bash
python test_saucedemo.py
```

The script runs the test functions listed in its test list and prints a summary of passed and failed tests.

Run an individual script when needed:

```bash
python test_login.py
```

```bash
python test_invalid_login.py
```

### Test results

Test results should be reported from actual test execution. The combined suite prints a PASS or FAIL message for each executed test and a final summary.

Do not interpret the fictional DemoShop manual-testing metrics as SauceDemo automation results. Update any portfolio metrics only after confirming the relevant test run.

## QA Concepts Demonstrated

### Expected Result vs. Actual Result

The expected result describes the intended application behaviour. The actual result records what happened during testing. Comparing the two helps determine whether further investigation is needed.

### Severity vs. Priority

- **Severity** describes the impact of a defect on the application or user.
- **Priority** describes how urgently the defect should be addressed.

### Manual vs. Automation Testing

Manual testing helps explore workflows and evaluate behaviour. Automation helps repeat selected checks consistently and can support regression testing.

### Assertions and Explicit Waits

Assertions verify expected conditions. Explicit waits help Selenium wait for a specific page condition or element state instead of relying only on fixed delays.

## Future Improvements

- Add more automated cart and checkout scenarios.
- Add negative checkout validation tests.
- Introduce pytest fixtures and parameterized tests.
- Generate structured HTML test reports.
- Add API testing with Postman or Python requests.
- Add SQL validation examples.
- Set up GitHub Actions for automated test execution.
- Create a requirements-to-test-case traceability matrix.

## Author

**Muhammad Sufyan**

Aspiring QA Engineer | Manual Testing | Python | Selenium WebDriver

GitHub: [Muhammadsufyan11011](https://github.com/Muhammadsufyan11011)

---

This portfolio is intended for learning and demonstrating practical software testing skills. Test results and findings should be interpreted according to the specific practice application and test execution described in each project.
