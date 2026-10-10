# DemoShop — Functional Requirements

This fictional e-commerce application is used as the test target for this QA portfolio.

## Authentication

- Users can sign in with a valid email address and password.
- Invalid credentials must display a clear error message without revealing whether the email exists.
- Email input must reject clearly invalid formats.
- Passwords are case-sensitive.
- A signed-in user can log out and return to the login page.

## Product Catalogue

- The product list displays product name, price and an **Add to cart** action.
- Opening a product displays the same price shown in the catalogue.
- Products marked out of stock cannot be added to the cart.

## Shopping Cart

- Adding a product creates a cart line with the correct product, unit price and quantity.
- Adding the same product again increases its quantity rather than creating a duplicate line.
- Quantity cannot be lower than 1.
- The line total equals `unit price × quantity`.
- The cart total equals the sum of all line totals.
- Removing a product recalculates the cart total immediately.

## Checkout

- Checkout requires at least one item in the cart.
- First name, last name, delivery address and email are required.
- Invalid email formats must block order submission.
- The order review must show the same products, quantities and total as the cart.
- A successful order displays a confirmation message and unique order reference.
- Double-clicking the final order button must not create duplicate orders.

## Quality Expectations

- Validation messages should explain what the user needs to correct.
- Critical user actions should not fail silently.
- The application should preserve consistent totals from cart through order confirmation.

> This specification and all defects in this repository are synthetic and were created for portfolio and learning purposes. They do not represent defects in a real company or production system.
