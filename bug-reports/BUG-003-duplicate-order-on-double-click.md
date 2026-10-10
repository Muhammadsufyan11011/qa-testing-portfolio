# BUG-003 — Double-clicking Place order creates duplicate orders

**Related test case:** TC-015  
**Severity:** Critical  
**Priority:** High  
**Status:** Open  
**Environment:** Desktop / Chromium-based browser / DemoShop test scenario

## Summary

Rapidly double-clicking the final **Place order** button creates two orders instead of one.

## Preconditions

- Cart contains at least one item.
- All checkout fields are valid.
- User is on the final order submission step.

## Steps to Reproduce

1. Complete checkout with valid data.
2. On the final step, double-click **Place order** quickly.
3. Observe the confirmation result and generated order records.

## Expected Result

The application accepts only one submission, disables or locks the action after the first click, and creates one order with one unique reference.

## Actual Result

Two order submissions are processed and two order references are created.

## Impact

In a real commerce system, this could lead to duplicate charges, duplicate fulfilment or duplicate customer orders. Because the defect affects transaction integrity, it is treated as critical in this portfolio scenario.

## Suggested Investigation

Review front-end submit-state handling and backend idempotency protections. A robust fix should not rely only on disabling the button in the browser; the backend should also prevent duplicate transaction processing.
