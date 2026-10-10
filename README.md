# QA Testing Portfolio

A practical **manual software testing portfolio** demonstrating test planning, requirements-based test design, bug reporting, exploratory testing and defect tracking.

The project uses a fictional e-commerce application called **DemoShop** so that every test case has explicit requirements and every reported defect has a defined expected result.

> All application behaviour, test results and defects in this repository are synthetic and created for learning and portfolio purposes. They do not describe a real company's production system.

## What this project demonstrates

- Manual functional testing
- Positive and negative test cases
- Boundary-value testing
- Requirements-based testing
- Bug reporting
- Severity vs priority assessment
- Exploratory testing
- Regression thinking
- Test summary reporting
- GitHub Issues for defect tracking

## Repository structure

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
└── README.md
```

## Test scenario

DemoShop is a fictional online store covering four core areas:

1. Authentication
2. Product catalogue
3. Shopping cart
4. Checkout and order submission

The functional specification is available in [`requirements/demo-shop-requirements.md`](requirements/demo-shop-requirements.md).

## Test execution

The manual suite contains **16 test cases** across login, catalogue, cart and checkout.

| Result | Count |
|---|---:|
| Passed | 13 |
| Failed | 3 |
| Blocked | 0 |
| Pass rate | 81.25% |

The complete suite is documented in [`test-cases/manual-test-cases.md`](test-cases/manual-test-cases.md).

## Defects found

Three synthetic defects are documented in detail:

### BUG-001 — Invalid email format accepted on login

**Severity:** Medium · **Priority:** Medium  
The login form attempts authentication for an obviously invalid email instead of blocking the request with clear validation.

[Bug report](bug-reports/BUG-001-invalid-login-email-accepted.md) · [GitHub Issue #1](https://github.com/PetrosChatz/qa-testing-portfolio/issues/1)

### BUG-002 — Cart total does not update after quantity change

**Severity:** High · **Priority:** High  
The quantity changes correctly, but the cart total remains stale until page refresh.

[Bug report](bug-reports/BUG-002-cart-total-not-updated.md) · [GitHub Issue #2](https://github.com/PetrosChatz/qa-testing-portfolio/issues/2)

### BUG-003 — Double-clicking Place order creates duplicate orders

**Severity:** Critical · **Priority:** High  
Two rapid submissions can create two orders, demonstrating a transaction-integrity and idempotency problem.

[Bug report](bug-reports/BUG-003-duplicate-order-on-double-click.md) · [GitHub Issue #3](https://github.com/PetrosChatz/qa-testing-portfolio/issues/3)

## Exploratory testing

A time-boxed exploratory session focuses on cart and checkout state consistency, including repeated actions, navigation, quantity boundaries and duplicate submission.

See [`exploratory-testing/session-notes.md`](exploratory-testing/session-notes.md).

## Test summary

The test summary consolidates execution metrics, open defects, release risk and regression recommendations.

See [`test-summary/test-summary-report.md`](test-summary/test-summary-report.md).

## Key QA concepts demonstrated

### Severity vs priority

**Severity** describes how strongly a defect affects the system or user. **Priority** describes how urgently the team wants the defect fixed. They are related, but they are not the same measurement.

### Expected vs actual result

Each defect is tied back to an explicit requirement. This avoids calling unexpected behaviour a bug without first defining what the system is supposed to do.

### Exploratory vs scripted testing

Scripted test cases provide repeatability and coverage. Exploratory testing gives the tester freedom to follow risks and unexpected behaviour. The two approaches complement each other.

### Regression testing

A defect fix can unintentionally affect working functionality. The summary report therefore identifies the cart and checkout areas that should be retested after fixes.

## Possible next improvements

- Add API testing with Postman or Python requests.
- Add SQL validation examples.
- Add browser/device compatibility coverage.
- Create a traceability matrix linking requirements to test cases.
- Add automated UI tests after the manual testing foundation is established.

## Author

**Petros Chatzistefanou**  
BSc Applied Informatics — Information Systems, University of Macedonia  
[LinkedIn](https://www.linkedin.com/in/petros-chatzistefanou/)
