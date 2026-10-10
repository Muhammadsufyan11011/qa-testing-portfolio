# Manual Test Cases

Status values in this portfolio are based on the fictional DemoShop scenario defined in the requirements.

| ID | Area | Test case | Preconditions | Steps | Expected result | Status |
|---|---|---|---|---|---|---|
| TC-001 | Login | Login with valid credentials | Registered user exists | Enter valid email and password; select Sign in | User is authenticated and redirected to catalogue | Pass |
| TC-002 | Login | Login with invalid password | Registered user exists | Enter valid email and incorrect password; select Sign in | Generic authentication error is shown; user remains signed out | Pass |
| TC-003 | Login | Reject invalid email format | Login page open | Enter `petros@`; enter any password; select Sign in | Submission is blocked and email validation message is shown | Fail |
| TC-004 | Login | Password is case-sensitive | Registered user exists | Enter valid email; change password letter casing; select Sign in | Authentication fails | Pass |
| TC-005 | Catalogue | Out-of-stock product cannot be added | Product is marked out of stock | Open product and attempt Add to cart | Add action is disabled or rejected with clear message | Pass |
| TC-006 | Cart | Add product to empty cart | Cart empty | Add one in-stock product | Cart shows correct product, unit price, quantity 1 and total | Pass |
| TC-007 | Cart | Add same product twice | Product already in cart with quantity 1 | Add same product again | Existing line changes to quantity 2; no duplicate line is created | Pass |
| TC-008 | Cart | Recalculate total after quantity update | Cart contains product priced €25 with quantity 1 | Change quantity to 3 | Line total and cart total become €75 immediately | Fail |
| TC-009 | Cart | Prevent quantity below 1 | Cart contains one product | Attempt to change quantity to 0 | Quantity 0 is rejected or product is removed through explicit remove action | Pass |
| TC-010 | Cart | Recalculate total after removing product | Cart contains at least two products | Remove one product | Removed line disappears and cart total recalculates immediately | Pass |
| TC-011 | Checkout | Block checkout with empty cart | Cart empty | Navigate to checkout | Checkout is blocked and user is prompted to add an item | Pass |
| TC-012 | Checkout | Required fields validation | Cart contains item | Leave required delivery fields empty; submit | Submission is blocked; clear field-level validation is shown | Pass |
| TC-013 | Checkout | Reject invalid checkout email | Cart contains item | Enter all valid data except email `test@`; submit | Order submission is blocked with email validation message | Pass |
| TC-014 | Checkout | Order review matches cart | Cart contains multiple items | Continue to order review | Products, quantities and total exactly match cart | Pass |
| TC-015 | Checkout | Prevent duplicate order on double click | Valid order ready for final submission | Double-click Place order quickly | Only one order is created and one confirmation/reference is shown | Fail |
| TC-016 | Checkout | Successful order confirmation | Valid order ready | Select Place order once | Confirmation message and unique order reference are displayed | Pass |

## Coverage Notes

The cases include positive flows, negative validation, boundary behaviour and transaction-safety checks. Failed cases are documented as synthetic defects in the `bug-reports/` directory and GitHub Issues.
