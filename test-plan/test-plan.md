# DemoShop Manual Test Plan

## Objective

Validate the core customer journey of the fictional DemoShop application, with emphasis on authentication, cart calculations and checkout reliability.

## In Scope

- Login and logout
- Email and password validation
- Product catalogue basics
- Add/remove cart actions
- Quantity updates and total calculations
- Checkout field validation
- Order review and submission
- Duplicate-order prevention

## Out of Scope

- Payment gateway integration
- Performance and load testing
- Accessibility certification
- Cross-browser automation
- Back-office/admin features
- Security penetration testing

## Test Approach

The portfolio uses a combination of:

- Positive functional testing
- Negative testing
- Boundary-value checks
- Validation testing
- Exploratory testing
- Regression-oriented test cases

## Test Environment

Because DemoShop is a fictional application, the environment is represented as a controlled test scenario rather than a live production service.

Assumed environment:

- Desktop browser
- Modern Chromium-based browser
- Test user account
- Stable internet connection

## Entry Criteria

- Functional requirements are available.
- Core login, catalogue, cart and checkout flows are testable.
- Test data is prepared.

## Exit Criteria

- All high-priority test cases have been executed.
- Critical and high-severity defects are documented.
- Core purchase flow has no unresolved blocker.
- Test summary documents pass/fail status and outstanding risk.

## Defect Severity

| Severity | Meaning |
|---|---|
| Critical | Prevents a core business flow or causes serious data/transaction failure. |
| High | Major feature fails with no reasonable workaround. |
| Medium | Feature behaves incorrectly but a workaround exists or impact is limited. |
| Low | Minor usability, visual or wording issue with little functional impact. |

## Defect Priority

Priority is kept separate from severity. Severity describes user/system impact; priority describes how urgently the team should fix the issue.
