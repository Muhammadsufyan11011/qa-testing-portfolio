# BUG-002 — Cart total does not update after quantity change

**Related test case:** TC-008  
**Severity:** High  
**Priority:** High  
**Status:** Open  
**Environment:** Desktop / Chromium-based browser / DemoShop test scenario

## Summary

Changing a cart item's quantity updates the displayed quantity but leaves the line total and cart total at their previous values.

## Preconditions

- User has an in-stock product priced at €25 in the cart.
- Current quantity is 1.

## Steps to Reproduce

1. Open the cart.
2. Change the product quantity from 1 to 3.
3. Observe the line total and cart total.

## Expected Result

The quantity becomes 3 and both the line total and cart total update to €75 immediately.

## Actual Result

The quantity displays 3, but the totals remain €25 until the page is refreshed.

## Impact

The user can see an incorrect amount before checkout. In a real transaction flow, inconsistent totals can cause loss of trust and could create order-value discrepancies if stale values are submitted.

## Workaround

Refreshing the page recalculates the displayed total in this synthetic scenario.
